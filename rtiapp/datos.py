from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Grupo, Alumno, Evaluacion, Evaluador
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
import rtiapp.encabezados as Encabezados
from django.contrib.auth.models import User
import itertools
import csv
from datetime import datetime

from .models import \
    Evaluacion_IPAL_INFANTIL, Evaluacion_IPAL_PRIMERO, Evaluacion_IPAL_SEGUNDO,\
    Evaluacion_IPAM_INFANTIL, Evaluacion_IPAM_PRIMERO, Evaluacion_IPAM_SEGUNDO, Evaluacion_IPAM_TERCERO, \
    Evaluacion_IPAE_PRIMERO, Evaluacion_IPAE_SEGUNDO, Evaluacion_IPAE_TERCERO

clases = {
    'IPAL-INFANTIL': Evaluacion_IPAL_INFANTIL,
    'IPAL-PRIMERO': Evaluacion_IPAL_PRIMERO,
    'IPAL-SEGUNDO': Evaluacion_IPAL_SEGUNDO,
    'IPAM-INFANTIL': Evaluacion_IPAM_INFANTIL,
    'IPAM-PRIMERO': Evaluacion_IPAM_PRIMERO,
    'IPAM-SEGUNDO': Evaluacion_IPAM_SEGUNDO,
    'IPAM-TERCERO': Evaluacion_IPAM_TERCERO,
    'IPAE-PRIMERO': Evaluacion_IPAE_PRIMERO,
    'IPAE-SEGUNDO': Evaluacion_IPAE_SEGUNDO,
    'IPAE-TERCERO': Evaluacion_IPAE_TERCERO,
}


def importar_csv(request, server_url):

    importar_tipo = request.GET['tipo'] # evaluadores, alumnos, grupos (tipo del fichero csv)
    usuario = request.user
    print('>>> Importando datos de tipo ' + importar_tipo )

    data = {}
    if "GET" == request.method:
        return render(request, 'importar_evaluadores.html', {'index': server_url, 'tipo':importar_tipo})

    # if not GET, then proceed
    try:
        csv_file = request.FILES["csv_file"]

        #if file is too large, return
        if csv_file.multiple_chunks():
            print('>>> Fichero CSV demasiado grande')
            return render(request, "error.html")

        file_data = csv_file.read().decode("utf-8")

        lines = file_data.split("\n")

        for line in lines:

            if importar_tipo == 'ALUMNOS':
                fields = line.split(";")
                alumno = Alumno(codigo=fields[0], curso=fields[3], curso_academico=fields[4],
                                centro_pilotaje=fields[5],sexo=fields[6])
                # fecha
                fechaNacimiento = fields[1]
                date = datetime.strptime(fechaNacimiento, "%d/%m/%Y")
                alumno.fecha_nacimiento = date

                # obtener el grupo desde su codigo
                codigoGrupo = fields[2]
                grupoAlumno = Grupo.objects.get(codigo=codigoGrupo)
                alumno.grupo = grupoAlumno

                # forzar el evaluador
                alumno.evaluador = request.user
                alumno.save()
                print('>>> Nuevo alumno subido:' + fields[0] + ', ' + fields[1] + ', ' +
                      fields[2] + ', ' + fields[3] + ', ' + fields[4] + ', ' + fields[5] + ', ' + fields[6])

            if importar_tipo == 'GRUPOS':
                fields = line.split(";")
                grupo = Grupo(codigo=fields[0],centro_pilotaje=fields[1], curso=fields[2],
                              nombre=fields[3], centro=fields[4], curso_academico=fields[5])
                grupo.evaluador = usuario
                grupo.save()
                grupo.evaluadores.add(usuario)
                grupo.save()
                print('>>> Nuevo grupo subido:' + fields[0] + ', ' + fields[1] + ', ' +
                      fields[2] + ', ' + fields[3] + ', ' + fields[4] + ', ' + fields[5])

            if importar_tipo == 'EVALUADORES':
                fields = line.split(";")
                codigo=fields[0]
                clave=fields[1]
                nombre=fields[2]
                email=fields[5]
                evaluador = Evaluador(codigo=codigo, clave=clave,
                    nombre=nombre, centro_pilotaje=fields[3],
                    centro=fields[4], email=fields[5])

                # el resto de campos se rellena por los docentes
                print(fields[0] + ', ' + fields[1] + ', ' + fields[2] + ', ' + fields[3]
                      + ', ' + fields[4] + ', ' + fields[5])

                # crear el usuario y asignarlo
                # TODO comprobar si ya existe!
                nuevoUsuario = User.objects.create_user(
                    username=codigo,email=email,password=clave,first_name=nombre)

                evaluador.usuario = nuevoUsuario

                # asignar el grupo
                grupoParticipantes = Group.objects.get(name='participantes')
                grupoParticipantes.user_set.add(nuevoUsuario)

                evaluador.save()


    except Exception as e:
        print('>>> Error subiendo CSV: ' + repr(e))
        return render(request, 'error.html', {'error': repr(e)})

    return redirect(server_url)




def exportar_CSV(request):
    print('>>> Exportando CSV mediante el modulo datos.py')
    tipo_datos = request.GET['tipo']

    # respuesta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="datos.csv"'
    writer = csv.writer(response, delimiter=',')

    if tipo_datos == 'grupos':
        print('>>> Exportando grupos')
        grupos = Grupo.objects.all()
        writer.writerow(['nombre', 'centro_pilotaje', 'codigo,''curso', 'curso_academico'])
        for grupo in grupos:
            writer.writerow([grupo.nombre, grupo.centro_pilotaje, grupo.codigo, grupo.curso, grupo.curso_academico])

    if tipo_datos == 'alumnos':
        print('>>> Exportando alumnos')
        # obtenemos todos los alumnos
        alumnos = Alumno.objects.all()
        # cabecera y fichero

        writer.writerow(['codigo', 'genero', 'curso', 'fecha nacimiento',
                         'pais', 'centro', 'grupo', 'id grupo', 'curso academico'])
        for alumno in alumnos:
            writer.writerow([alumno.codigo, alumno.sexo, alumno.curso,
                             alumno.fecha_nacimiento, alumno.pais, alumno.centro_pilotaje, alumno.grupo.nombre,
                             alumno.grupo.pk,  alumno.curso_academico
                             ])


    if tipo_datos == 'evaluadores':
        print('>>> Exportando evaluadores')
        # obtenemos todos los evaluadores
        evaluadores = Evaluador.objects.all()
        writer.writerow(['codigo', 'nombre', 'centro', 'centro pilojate',
                         'genero', 'nivel academico', 'pais', 'email', 'zona'])
        for evaluador in evaluadores:
            writer.writerow([evaluador.codigo, evaluador.nombre, evaluador.centro,
                             evaluador.centro_pilotaje, evaluador.sexo, evaluador.nivel_academico,
                             evaluador.pais, evaluador.email, evaluador.zona])

    if tipo_datos == 'IPAL':
        curso = request.GET['curso']
        print('>>> Exportando IPAL-' + curso)
        # obtener el modelo
        nombre_modelo = 'IPAL-' + curso
        modelo = clases[nombre_modelo]
        evaluaciones = modelo.objects.all()

        if curso == 'INFANTIL':
            writer.writerow(Encabezados.encabezado_IPAL_INFANTIL)
            for e in evaluaciones:
                writer.writerow([
                    e.alumno, e.evaluador, e.alumno.grupo, e.alumno.evaluador, e.alumno.centro_pilotaje, e.curso_academico, e.ultima_modificacion, e.prueba, e.mes,
                    e.tipo,
                    e.ADIVINANZAS, e.CSL, e.CNL, e.CLE_IMAGEN, e.CLE_TEXTO, e.CFA, e.evaluado
                ])

        if curso == 'PRIMERO':
            writer.writerow(Encabezados.encabezado_IPAL_PRIMERO)
            for e in evaluaciones:
                writer.writerow([
                    e.alumno, e.evaluador,e.alumno.grupo, e.alumno.evaluador, e.alumno.centro_pilotaje, e.curso_academico, e.ultima_modificacion, e.prueba, e.mes,
                    e.tipo,
                    e.TM, e.LP, e.CSL, e.CNL, e.FLO, e.CLE_TEXTO, e.CFS, e.evaluado
                ])

        if curso == 'SEGUNDO':
            writer.writerow(Encabezados.encabezado_IPAL_SEGUNDO)
            for e in evaluaciones:
                writer.writerow([
                    e.alumno, e.evaluador, e.alumno.grupo, e.alumno.evaluador,e.alumno.centro_pilotaje, e.curso_academico, e.ultima_modificacion, e.prueba, e.mes,
                    e.tipo,
                    e.TM, e.LP, e.CSL, e.CNL, e.FLO, e.CLE_TEXTO, e.CFS, e.PRO, e.VOC, e.evaluado
                ])

    if tipo_datos == 'IPAM':
        curso = request.GET['curso']
        print('>>> Exportando IPAM-' + curso)
        # obtener el modelo
        nombre_modelo = 'IPAM-' + curso
        modelo = clases[nombre_modelo]
        evaluaciones = modelo.objects.all()
        if curso == 'INFANTIL':
            writer.writerow(Encabezados.encabezado_IPAM_INFANTIL)
            for e in evaluaciones:
                writer.writerow([
                    e.alumno, e.evaluador,e.alumno.grupo, e.alumno.evaluador, e.alumno.centro_pilotaje, e.curso_academico, e.ultima_modificacion, e.prueba, e.mes,
                    e.tipo,
                    e.CN, e.EC, e.SN, e.IN, e.CVA, e.CM, e.evaluado
                ])
        if curso == 'PRIMERO' or curso == 'SEGUNDO' or curso == 'TERCERO':
            writer.writerow(Encabezados.encabezado_IPAM_PRIMERO)
            for e in evaluaciones:
                writer.writerow([
                    e.alumno, e.evaluador, e.alumno.grupo, e.alumno.evaluador,e.alumno.centro_pilotaje, e.curso_academico, e.ultima_modificacion, e.prueba, e.mes,
                    e.tipo,
                    e.CN, e.ODD, e.SN, e.OUD, e.VP, e.evaluado
                ])

    if tipo_datos == 'IPAE':
        curso = request.GET['curso']
        print('>>> Exportando IPAE-' + curso)
        # obtener el modelo
        nombre_modelo = 'IPAE-' + curso
        modelo = clases[nombre_modelo]
        evaluaciones = modelo.objects.all()
        if curso == 'PRIMERO' or curso == 'SEGUNDO':
            writer.writerow(Encabezados.encabezado_IPAE_PRIMERO)
            for e in evaluaciones:
                writer.writerow([
                    e.alumno, e.evaluador,e.alumno.grupo, e.alumno.evaluador, e.alumno.centro_pilotaje, e.curso_academico, e.ultima_modificacion, e.prueba, e.mes,
                    e.tipo,
                    e.TLC_1, e.DICTADO_ORTOGRAFIA_ARBITRARIA, e.DICTADO_ORTOGRAFIA_REGLADA, e.DICTADO_PSEUDOPALABRAS,
                    e.DICTADO_FRASES, e.evaluado
                ])
        if curso == 'TERCERO':
            writer.writerow(Encabezados.encabezado_IPAE_TERCERO)
            for e in evaluaciones:
                writer.writerow([
                    e.alumno, e.evaluador,e.alumno.grupo, e.alumno.evaluador, e.alumno.centro_pilotaje, e.curso_academico, e.ultima_modificacion, e.prueba, e.mes,
                    e.tipo,
                    e.DICTADO_ORTOGRAFIA_ARBITRARIA, e.DICTADO_ORTOGRAFIA_REGLADA, e.DICTADO_FRASES,
                    e.SEC_5, e.SEC_SEI_5, e.PDC_5, e.evaluado
                ])

    # devolver el fichero para descargar
    return response



