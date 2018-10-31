from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Grupo, Alumno, Evaluacion, Evaluador
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from datetime import datetime

from .forms import FormGrupo, FormAlumno, FormAlumnoPOST, FormEvaluador, FormAlumnoGrupoForzado,\
    Form_Evaluacion_IPAL_INFANTIL, Form_Evaluacion_IPAL_PRIMERO, Form_Evaluacion_IPAL_SEGUNDO, \
    Form_Evaluacion_IPAM_INFANTIL, Form_Evaluacion_IPAM_PRIMERO, Form_Evaluacion_IPAM_SEGUNDO, \
    Form_Evaluacion_IPAM_TERCERO, Form_Evaluacion_IPAE_PRIMERO, Form_Evaluacion_IPAE_SEGUNDO, \
    Form_Evaluacion_IPAE_TERCERO,SignUpForm,FormAlumnoConsejeria, FormAlumnoConsejeriaPOST

from .models import \
    Evaluacion_IPAL_INFANTIL, Evaluacion_IPAL_PRIMERO, Evaluacion_IPAL_SEGUNDO,\
    Evaluacion_IPAM_INFANTIL, Evaluacion_IPAM_PRIMERO, Evaluacion_IPAM_SEGUNDO, Evaluacion_IPAM_TERCERO, \
    Evaluacion_IPAE_PRIMERO, Evaluacion_IPAE_SEGUNDO, Evaluacion_IPAE_TERCERO




import rtiapp.omnibus_ipal as OmnibusIPAL
import rtiapp.omnibus_ipam as OmnibusIPAM
import rtiapp.omnibus_ipae as OmnibusIPAE
import rtiapp.riesgo_ipal as RiesgoIPAL
import rtiapp.riesgo_ipam as RiesgoIPAM
import rtiapp.riesgo_ipae as RiesgoIPAE
import rtiapp.constantes as Globales
import rtiapp.encabezados as Encabezados
from django.db.models import Q
import itertools
import csv

#server_url = 'http://127.0.0.1:8000/'
server_url = 'http://193.145.96.31/'

lista_grupos_url = 'lista-grupos'
editar_grupo_url = 'editar-grupo'
lista_alumnos_grupo_url = 'lista-alumnos-grupo'
lista_evaluaciones = 'lista-evaluaciones'

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
formularios = {
    'IPAL-INFANTIL': Form_Evaluacion_IPAL_INFANTIL,
    'IPAL-PRIMERO': Form_Evaluacion_IPAL_PRIMERO,
    'IPAL-SEGUNDO': Form_Evaluacion_IPAL_SEGUNDO,
    'IPAM-INFANTIL': Form_Evaluacion_IPAM_INFANTIL,
    'IPAM-PRIMERO': Form_Evaluacion_IPAM_PRIMERO,
    'IPAM-SEGUNDO': Form_Evaluacion_IPAM_SEGUNDO,
    'IPAM-TERCERO': Form_Evaluacion_IPAM_TERCERO,
    'IPAE-PRIMERO': Form_Evaluacion_IPAE_PRIMERO,
    'IPAE-SEGUNDO': Form_Evaluacion_IPAE_SEGUNDO,
    'IPAE-TERCERO': Form_Evaluacion_IPAE_TERCERO,
}
colores_riesgo = {
  "NOEV": "#ffffff",
  "ALTR": "#850202",
  "RIES": "#f00",
  "BAJO": "#ffa500",
  "NORM": "#009fff",
  "OPTI": "#1ae36e"
}


ERROR_ALUMNO_YA_TIENE_EVALUACION_ANUAL = 'Este alumno ya tiene registros de evaluación para el curso'
ERROR_INFORME_IPAE_INFANTIL = 'La prueba IPAE no tiene una versión para Infantil'
ERROR_EVALUADOR_NO_EXISTE = 'El número de identificación del otro evaluador es incorrecto'
ERROR_LISTADO_GRUPOS = 'No ha creado ningun grupo'
ERROR_NO_HAY_EVALUACIONES = 'No existen evaluaciones para este alumno'
ERROR_NO_HAY_ALUMNOS_EN_GRUPO = 'El grupo no contiene alumnos'
ERROR_PROPIETARIO_GRUPO = 'No es el propietario de este grupo'
ERROR_PROPIETARIO_ALUMNO = 'No es el propietario de este alumno'
ERROR_PROPIETARIO_EVALUACION = 'No es el propietario de esta evaluacion'
ERROR_ROL_INVESTIGADOR = 'No tiene el rol de investigador'
ERROR_ELIMINAR_ALUMNO = 'No tiene permiso para eliminar un alumno'

from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group



def es_investigador(request):
    print('>>> Comprobando si el rol es investigador')
    return True if request.user.groups.filter(name='investigadores').exists() else False

def es_participante(request):
   return True if request.user.groups.filter(name='participantes').exists() else False

def puede_eliminar_alumnos(request):
    print('>>> Comprobando permisos para eliminar alumno')
    # solo investigadores o usuarios normales de la plataforma pueden
    # eliminar. No esta permitido para el profesorado participante
    return True if es_investigador(request) or not es_participante(request) else False

def es_creador_grupo(request, grupo):
    print('>>> Comprobando si es el creador del grupo')
    return grupo.evaluador == request.user # el grupo es del usuario

def es_propietario_grupo(request, grupo):
    print('>>> Comprobando propietario del grupo')
    evaluadores = grupo.evaluadores.all()
    return request.user in evaluadores
    # return True
    #
    # return request.user in evaluadores
    #return grupo.evaluador == request.user # el grupo es del usuario

def es_propietario_alumno(request, alumno):
    print('>>> Comprobando propietario del alumno')
    evaluadores = alumno.grupo.evaluadores.all()
    return request.user in evaluadores
    # return alumno.evaluador == request.user # el alumno es del usuario

def es_propietario_evaluacion(request, evaluacion):
    print('>>> Comprobando propietario de la evaluacion')
    return evaluacion.evaluador == request.user # la evaluacion es del usuario


def cerrar_sesion(request):
    print('>>> Cerrando sesion de usuario')
    logout(request)
    return redirect(server_url)

def index(request):
    return render(request,'principal.html')

def ayuda(request):
    return render(request, 'ayuda.html', {'index': server_url})

def documentos(request):
    return render(request,'documentos.html', {'index':server_url})

def exportar(request):
    print('>>> Menu de exportar datos')
    if es_investigador(request):
        return render(request, 'exportar_datos.html', {'server_url': server_url, 'index': server_url})
    else:
        return render(request, 'error.html', {'error': ERROR_ROL_INVESTIGADOR})

def eliminar_alumno(request):
    print('>>> Eliminar alumno')
    id_alumno = request.GET['idAlumno']
    id_grupo = request.GET['idGrupo']
    alumno = Alumno.objects.get(pk=id_alumno)

    # comprobar si el usuario tiene permisos por su rol
    if not puede_eliminar_alumnos(request):
        return render(request, 'error.html', {'error': ERROR_ELIMINAR_ALUMNO})

    # comprobar los permisos en este ALUMNO
    if not es_propietario_grupo(request, alumno.grupo):
        return render(request, 'error.html', {'error': ERROR_PROPIETARIO_ALUMNO})

    alumno.delete()
    url_retorno = server_url + lista_alumnos_grupo_url + '/?idGrupo=' + id_grupo
    return redirect(url_retorno)



def elimina_grupo(request):
    print('>>> Grupo eliminado')
    id_grupo = request.GET['idGrupo']
    grupo = Grupo.objects.get(pk=id_grupo)
    grupo.delete()
    return render(request, 'error.html', {
        'index': server_url,
        'server_url': server_url, 'grupo': grupo})


def eliminar_grupo(request):
    print('>>> Eliminar grupo?')
    id_grupo = request.GET['idGrupo']
    grupo = Grupo.objects.get(pk=id_grupo)
    return render(request, 'eliminar_grupo.html', {
        'index':server_url,
        'server_url': server_url, 'grupo': grupo})

def compartir_grupo(request):
    print('>>> Compartiendo grupo con otro evaluador')
    id_grupo = request.GET['idGrupo']
    grupo = Grupo.objects.get(pk=id_grupo)
    return render(request, 'compartir_grupo.html', {
        'index':server_url,
        'server_url': server_url, 'grupo': grupo})



def actualizar_grupo_compartido(request):
    # obtenemos el evaluador seleccionado y
    # comprobamos que es valido
    id_evaluador = request.GET['idEvaluador']
    id_grupo = request.GET['idGrupo']

    try:
        evaluador = Evaluador.objects.get(pk=id_evaluador)
        grupo = Grupo.objects.get(pk=id_grupo)
        # agregar al grupo un nuevo evaluador
        grupo.evaluadores.add(evaluador.usuario)
        grupo.save()
        print('>>> Nuevo grupo ' + grupo.nombre + ' compartido con ' + evaluador.nombre)
        return redirect(server_url)

    except ObjectDoesNotExist:
        return render(request,
                      'error.html', {'error': ERROR_EVALUADOR_NO_EXISTE})


def establecer_curso(request):
    print('>>> Estableciendo curso academico')
    # obtener el curso actual desde el
    # perfil del evaluador y pasarlo como parametro
    evaluador = Evaluador.objects.get(usuario=request.user)
    curso = evaluador.curso_academico
    # url_retorno = server_url + lista_alumnos_grupo_url + '/?idGrupo=' + id_grupo
    return render(request, 'establecer_curso.html', {
        'index': server_url,
        'server_url': server_url, 'curso': curso})


# almacena el nuevo curso academico establecido
# en la base de datos
def actualizar_curso(request):
    evaluador = Evaluador.objects.get(usuario=request.user)
    curso = request.GET['curso']
    evaluador.curso_academico = curso
    evaluador.save()
    print('>>> Guardando nuevo curso academico: ' + curso)
    return redirect(server_url)


# generar datos y mostrar informe individual
def informe_individual(request):
    print('>>> Informe individual')
    id_alumno = request.GET['idAlumno']
    id_grupo = request.GET['idGrupo']
    prueba = request.GET['prueba']
    alumno = Alumno.objects.get(pk=id_alumno)
    curso = alumno.curso

    # comprobar los permisos en este ALUMNO
    if not es_propietario_grupo(request, alumno.grupo):
        return render(request,'error.html', {'error': ERROR_PROPIETARIO_ALUMNO})

    # plabtilla html y url de retorno
    plantilla = 'informe_individual_' + prueba + '_' + curso + '.html'
    url_retorno = server_url + lista_alumnos_grupo_url + '/?idGrupo=' + id_grupo

    # para el informe individual se necesitan las evaluaciones
    # de la tarea

    try:

        print('>>> Recuperando evaluaciones de ' + alumno.codigo + ' para prueba ' + prueba + ' ' + curso)
        evaluaciones = [] # lista de evaluaciones

        # obtener la clase
        nombre_modelo = prueba + '-' + curso
        modelo = clases[nombre_modelo]

        consulta_evaluaciones = modelo.objects.filter(
            alumno=alumno, curso_academico=alumno.curso_academico)

        # introducimos en el diccionario de evaluaciones
        for registro_evaluacion in consulta_evaluaciones:
            print(registro_evaluacion.alumno.codigo + ' ' +
                  registro_evaluacion.mes_leible + ' ' +
                  registro_evaluacion.riesgo + ' ' +
                  registro_evaluacion.get_tipo_display())

            evaluaciones.append(registro_evaluacion) # introducimos la evaluacion

        # pasamos a la plantillas las evaluaciones inicio, medio, fin
        return render(request, plantilla,
                      {'grupo': alumno.grupo,
                       'alumno': alumno,
                       'curso': alumno.curso,
                       'evaluaciones': evaluaciones,
                       'evaluacion_inicio': consulta_evaluaciones.get(mes=1).omnibus,
                       'evaluacion_medio': consulta_evaluaciones.get(mes=4).omnibus,
                       'evaluacion_fin': consulta_evaluaciones.get(mes=7).omnibus,
                       'colores_riesgo': colores_riesgo,
                       'index': server_url,
                       'server_url': url_retorno}
                      )

    except ObjectDoesNotExist:
        return render(request, 'error.html', {'error': ERROR_NO_HAY_EVALUACIONES})





# generar datos y mostrar el informe general
# de grupo
def informe_grupo(request):

    print('>>> Informe de grupo')
    # obtener el grupo y recuperar los alumnos
    id_grupo = request.GET['idGrupo']
    grupo = Grupo.objects.get(pk=id_grupo)
    curso = grupo.curso
    prueba = request.GET['prueba']
    url_retorno = server_url + lista_alumnos_grupo_url + '/?idGrupo=' + id_grupo
    print('>>> Grupo ' + grupo.nombre + ' ' + grupo.curso + ' ' + prueba)


    # comprobar los permisos en este grupo
    if not es_propietario_grupo(request, grupo):
        return render(request,'error.html', {'error': ERROR_PROPIETARIO_GRUPO})



    # no hay pruebas de IPAE INFANTIL

    if prueba == Globales.IPAE and curso == Globales.INFANTIL:
        return render(request, 'error.html', {'error': ERROR_INFORME_IPAE_INFANTIL,
        'server_url':url_retorno})

    try:

        # obtener alumnos solo de ese grupo y curso
        # alumnos = Alumno.objects.filter(evaluador=request.user, grupo=grupo, curso=grupo.curso)
        # nota: he desconectado evaluador=request.user para que funcione el sistema de
        # aulas compartidas.
        alumnos = Alumno.objects.filter(grupo=grupo, curso=grupo.curso)

        # obtener las evaluaciones inicio-medio-fin de todos los
        # alumnos recuperados

        print('>>> Recuperando evaluaciones')
        todas_evaluaciones = []# lista de evaluaciones

        # obtener la clase
        nombre_modelo = prueba + '-' + curso
        modelo = clases[nombre_modelo]
        for alumno in alumnos:

            consulta_evaluaciones = modelo.objects.filter(
                alumno=alumno).filter(
                Q(mes=Globales.NOVIEMBRE) |
                Q(mes=Globales.FEBRERO) |
                Q(mes=Globales.MAYO)
            )
            # recorrer la queryset recuperando cada registro
            # de evaluacion
            for registro_evaluacion in consulta_evaluaciones:
                print(registro_evaluacion.alumno.codigo + ' ' +
                      registro_evaluacion.mes_leible + ' ' +
                      registro_evaluacion.riesgo + ' ' +
                      registro_evaluacion.get_tipo_display())
                todas_evaluaciones.append(registro_evaluacion)


        plantilla = 'informe_grupo.html'

        return render(request, plantilla,
                      {'grupo': grupo,
                       'alumnos': alumnos,
                       'evaluaciones': todas_evaluaciones,
                       'colores_riesgo': colores_riesgo,
                       'prueba': prueba,
                       'curso': curso,
                       'index': server_url,
                       'server_url': url_retorno}
                      )

    except ObjectDoesNotExist:
        return render(request, 'error.html', {'error': "No tiene alumnos"})





def alta_evaluador(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # crear el nuevo usuario
            form.save()

            # obtener el usuario
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            usuario = authenticate(username=username, password=raw_password)

            # crear el registro de Evaluador
            nombre = form.cleaned_data.get('nombre')
            email = form.cleaned_data.get('email')
            centro = form.cleaned_data.get('centro')
            pais = form.cleaned_data.get('pais')
            sexo = form.cleaned_data.get('sexo')
            nivel_academico = form.cleaned_data.get('nivel_academico')
            profesion = form.cleaned_data.get('profesion')
            zona = form.cleaned_data.get('zona')

            evaluador = Evaluador(
                nombre=nombre,
                email=email,
                centro=centro,
                pais=pais,
                sexo=sexo,
                nivel_academico=nivel_academico,
                profesion=profesion,
                zona=zona,
                usuario=usuario
            )

            evaluador.save()

            login(request, usuario)
            return redirect(server_url)
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form, 'server_url': server_url})



# devuelve verdadero si es cribado
def evaluacion_es_cribado(evaluacion):
    mes = evaluacion.mes
    return mes == Globales.NOVIEMBRE or mes == Globales.FEBRERO or mes == Globales.MAYO


# devuelve el momento de evaluacion dependiendo del mes
def momento_evaluacion(evaluacion):
    mes = evaluacion.mes
    if mes == Globales.NOVIEMBRE:
       return Globales.INICIO
    if mes == Globales.FEBRERO:
        return Globales.MEDIO
    if mes == Globales.MAYO:
        return Globales.FIN
    return Globales.INICIO


#
# nuevas evaluaciones
#


def nueva_evaluacion(request):
    print('>>> Nueva evaluacion anual')
    id_alumno = request.GET['idAlumno']
    tipo = request.GET['tipo']
    alumno = Alumno.objects.get(pk=id_alumno)
    evaluador = Evaluador.objects.get(usuario=request.user)
    grupo = alumno.grupo
    curso = alumno.curso
    id_grupo = str(alumno.grupo.pk)
    url_retorno = server_url + lista_evaluaciones + \
                  '/?idGrupo=' + id_grupo + '&idAlumno=' + id_alumno + \
                  '&tipo=' + tipo

    print('>>> Nueva evaluacion ' + str(evaluador.curso_academico) + ' ' + tipo + ' ' + curso)

    # nombre del modelo a instanciar
    nombre_modelo = tipo + '-' + curso

    # buscamos un registro que contenga una evaluacion
    # de este alumno que coincida con la fecha del curso
    # configurada en el perfil del evaluador, si existe
    # no se permite crear mas
    reg_evaluacion = clases[nombre_modelo].objects.filter(
        alumno=alumno, curso_academico=evaluador.curso_academico)

    if not reg_evaluacion:
        print('>>> Comenzando a crear el registro anual para esta prueba')
    else:
        print(' >>> Ya existe un registro anual de esta prueba para este alumno: ABORTANDO')
        return render(request, 'error.html',
            {'error': ERROR_ALUMNO_YA_TIENE_EVALUACION_ANUAL +
                      str(evaluador.curso_academico),'server_url': url_retorno})


    # al crear una evaluacion anual para el alumno
    # tenemos que crear 7 registros de evaluacion de la prueba
    # correspondiente

    meses_evaluacion = [
        Globales.NOVIEMBRE,
        Globales.DICIEMBRE,
        Globales.ENERO,
        Globales.FEBRERO,
        Globales.MARZO,
        Globales.ABRIL,
        Globales.MAYO
    ]


    # creamos la nueva evaluacion para el mes correspondiente
    for mes in meses_evaluacion:

        evaluacion = clases[nombre_modelo](
            mes=mes,
            evaluador=request.user,
            alumno=alumno,
            curso_academico=grupo.curso_academico
            # obsoleto: curso_academico=evaluador.curso_academico
        )

        # comprobar si es de tipo cribado o progreso
        cribado_progreso = Globales.PROGRESO
        if mes == Globales.NOVIEMBRE or mes == Globales.FEBRERO or mes == Globales.MAYO:
            cribado_progreso = Globales.CRIBADO
        evaluacion.tipo = cribado_progreso

        # asignar la prueba
        evaluacion.prueba = tipo
        # momento de evaluacion
        evaluacion.mes_leible = evaluacion.get_mes_display()
        momento = momento_evaluacion(evaluacion)
        evaluacion.momento = momento
        evaluacion.save()
        print('>>> Creada evaluacion para ' + evaluacion.get_mes_display() )

    return redirect(url_retorno)




#
# procesa una evaluacion al guardarla
#

def procesar_evaluacion(evaluacion):

    alumno = evaluacion.alumno
    prueba = evaluacion.prueba
    curso = alumno.curso
    cribado = evaluacion_es_cribado(evaluacion)

    print('>>> Procesando evaluacion: ' + prueba + '-' + curso)

    # calcular los valores de las subpruebas
    # complementarias de IPAL segundo
    if prueba == Globales.IPAL and curso == Globales.SEGUNDO:

        '''
        print('>>> Evaluacion IPAL de SEGUNDO, procesando SUBPRUEBAS COMPLEMENTARIAS')
        evaluacion.CSL = OmnibusIPAL.subprueba_complementaria_CSL(evaluacion)
        evaluacion.CLE_TEXTOS = OmnibusIPAL.subprueba_complementaria_CLE_TEXTOS(evaluacion)
        evaluacion.CFS = OmnibusIPAL.subprueba_complementaria_CFS(evaluacion)
        evaluacion.VOC = OmnibusIPAL.subprueba_complementaria_VOC(evaluacion)
        print('- CSL: ' + str(evaluacion.CSL))
        print('- CLE TEXTOS: ' + str(evaluacion.CLE_TEXTOS))
        print('- CFS: ' + str(evaluacion.CFS))
        print('- VOC: ' + str(evaluacion.VOC))
        '''

    # comprobar si es de cribado progreso
    if cribado:

        print('>>> Evaluacion de cribado')

        evaluacion.tipo = Globales.CRIBADO
        momento = momento_evaluacion(evaluacion)
        evaluacion.momento = momento

        # calculo del OMNIBUS dependiendo del tipo de prueba

        if prueba == Globales.IPAL:
            if curso == Globales.INFANTIL:
                omnibus = OmnibusIPAL.omnibus_INFANTIL(evaluacion, momento)
            if curso == Globales.PRIMERO:
                omnibus = OmnibusIPAL.omnibus_PRIMERO(evaluacion, momento)
            if curso == Globales.SEGUNDO:
                omnibus = OmnibusIPAL.omnibus_SEGUNDO(evaluacion, momento)

        if prueba == Globales.IPAM:
            if curso == Globales.INFANTIL:
                omnibus = OmnibusIPAM.omnibus_INFANTIL(evaluacion, momento)
            if curso == Globales.PRIMERO:
                omnibus = OmnibusIPAM.omnibus_PRIMERO(evaluacion, momento)
            if curso == Globales.SEGUNDO:
                omnibus = OmnibusIPAM.omnibus_SEGUNDO(evaluacion, momento)
            if curso == Globales.TERCERO:
                omnibus = OmnibusIPAM.omnibus_TERCERO(evaluacion, momento)

        if prueba == Globales.IPAE:
            if curso == Globales.PRIMERO:
                omnibus = OmnibusIPAE.omnibus_PRIMERO(evaluacion, momento)
            if curso == Globales.SEGUNDO:
                omnibus = OmnibusIPAE.omnibus_SEGUNDO(evaluacion, momento)
            if curso == Globales.TERCERO:
                omnibus = OmnibusIPAE.omnibus_TERCERO(evaluacion, momento)

        # asignamos el omnibus
        evaluacion.omnibus = omnibus

        print('>>> Calculo OMNIBUS ' + momento + ' del mes ' + evaluacion.get_mes_display())
        print(omnibus)

        # calculo del RIESGO dependiendo del tipo de prueba
        # siempre despues del calculo de omibus

        if prueba == Globales.IPAL:
            if curso == Globales.INFANTIL:
                riesgo = RiesgoIPAL.riesgo_INFANTIL(omnibus, momento)
            if curso == Globales.PRIMERO:
                riesgo = RiesgoIPAL.riesgo_PRIMERO(omnibus, momento)
            if curso == Globales.SEGUNDO:
                riesgo = RiesgoIPAL.riesgo_SEGUNDO(omnibus, momento)


        if prueba == Globales.IPAM:
            if curso == Globales.INFANTIL:
                riesgo = RiesgoIPAM.riesgo_INFANTIL(omnibus, momento)
            if curso == Globales.PRIMERO:
                riesgo = RiesgoIPAM.riesgo_PRIMERO(omnibus, momento)
            if curso == Globales.SEGUNDO:
                riesgo = RiesgoIPAM.riesgo_SEGUNDO(omnibus, momento)
            if curso == Globales.TERCERO:
                riesgo = RiesgoIPAM.riesgo_TERCERO(omnibus, momento)

        if prueba == Globales.IPAE:
            if curso == Globales.PRIMERO:
                riesgo = RiesgoIPAE.riesgo_PRIMERO(omnibus, momento)
            if curso == Globales.SEGUNDO:
                riesgo = RiesgoIPAE.riesgo_SEGUNDO(omnibus, momento)
            if curso == Globales.TERCERO:
                riesgo = RiesgoIPAE.riesgo_TERCERO(omnibus, momento)


        # el riesgo en el objeto evaluacion siempre se actualiza
        evaluacion.riesgo = riesgo


        evaluacion.alumno.save()

        print('>>> Calculo RIESGO:')
        print('>>> ' + evaluacion.get_riesgo_display())

    else:

        print('>>> Evaluacion de progreso de ' + evaluacion.get_mes_display())
        evaluacion.tipo = Globales.PROGRESO


    # si no esta activada la opccion de evaluado,
    # el riesgo se sobreescrbe como SIN_EVALUAR
    if evaluacion.evaluado == False:
        evaluacion.riesgo = Globales.SIN_EVALUAR

    # actualizamos el campo. TODO: VER SI ESTE CAMPO ES NECESARIO
    # PORQUE REALMENTE PODEMOS USAR SIEMPRE get_mes_display()
    evaluacion.mes_leible = evaluacion.get_mes_display()
    evaluacion.save()





#
# editar evaluaciones
#

def editar_evaluacion(request):
    print('>>> Editando evaluacion')
    id_evaluacion = request.GET['idEvaluacion']
    tipo = request.GET['tipo']
    curso = request.GET['curso']
    nombre_clase = tipo + '-' + curso
    evaluacion = get_object_or_404(clases[nombre_clase], pk=id_evaluacion)

    url_retorno = server_url + 'lista-evaluaciones/?idAlumno=' + str(evaluacion.alumno.pk) + '&tipo=' + tipo
    print('>>> Evaluacion de ' + nombre_clase)

    # comprobar los permisos en este alumno
    if not es_propietario_evaluacion(request, evaluacion):
        return render(request, 'error.html', {'error': ERROR_PROPIETARIO_EVALUACION})

    if request.method == "POST":
        print('>>> Enviando puntuaciones directas')
        form = formularios[nombre_clase](request.POST, instance=evaluacion)
        if form.is_valid():
            evaluacion = form.save(commit=False)
            procesar_evaluacion(evaluacion)
            return redirect(url_retorno)
        else:
            print('>>> ERROR EN LOS DATOS DEL FORMULARIO')
            return redirect(url_retorno)
    else:
        print('>>> Mostrando formulario de puntuaciones directas para ' + nombre_clase)
        form = formularios[nombre_clase](instance=evaluacion)

    plantilla = 'form_editar_evaluacion_' + tipo + '_' + curso + '.html'
    return render(request, plantilla, {
        'form': form, 'evaluacion': evaluacion, 'index':server_url, 'server_url': url_retorno})









def listar_evaluaciones(request):
    print('>>> Lista generica de evaluaciones')
    id_alumno = request.GET['idAlumno']
    tipo = request.GET['tipo']
    alumno = Alumno.objects.get(pk=id_alumno)
    curso = alumno.curso
    print('>>> Mostrando lista para ' + tipo + ' ' + curso)

    # comprobar los permisos en este alumno
    if not es_propietario_alumno(request, alumno):
        return render(request, 'error.html', {'error': ERROR_PROPIETARIO_ALUMNO})

    # TODO SOLO MOSTRAMOS LAS DEL PRESENTE AÑO ACADEMICO: VER COMO MEJORAR ESTO
    # EN PRINCIPIO AÑADIENDO OPCIONES DE FILTRO, COMO EN EL CASO
    # DE LOS ALUMNOS: PERO ENTONCES, PARA QUE TENEMOS UNA VARIABLE
    # DE CURSO ACADEMICO EN EL EVALUADOR?

    # curso_academico = alumno.grupo.curso_academico

    if tipo == Globales.IPAL:
        if curso == Globales.TERCERO:
            print('>>> Error: no hay IPAL TERCERO')


    try:

        if tipo == Globales.IPAL:
            if curso == Globales.INFANTIL:
                evaluaciones = Evaluacion_IPAL_INFANTIL.objects.filter \
                    (alumno=alumno).order_by('curso_academico', 'mes')#.reverse()
            if curso == Globales.PRIMERO:
                evaluaciones = Evaluacion_IPAL_PRIMERO.objects.filter \
                    (alumno=alumno).order_by('curso_academico', 'mes')#.reverse()
            if curso == Globales.SEGUNDO:
                evaluaciones = Evaluacion_IPAL_SEGUNDO.objects.filter \
                    (alumno=alumno).order_by('curso_academico', 'mes')#.reverse()

        if tipo == Globales.IPAM:
            if curso == Globales.INFANTIL:
                evaluaciones = Evaluacion_IPAM_INFANTIL.objects.filter \
                    (alumno=alumno).order_by('curso_academico', 'mes')#.reverse()
            if curso == Globales.PRIMERO:
                evaluaciones = Evaluacion_IPAM_PRIMERO.objects.filter \
                    (alumno=alumno).order_by('curso_academico', 'mes')#.reverse()
            if curso == Globales.SEGUNDO:
                evaluaciones = Evaluacion_IPAM_SEGUNDO.objects.filter \
                    (alumno=alumno).order_by('curso_academico', 'mes')#.reverse()
            if curso == Globales.TERCERO:
                evaluaciones = Evaluacion_IPAM_TERCERO.objects.filter \
                    (alumno=alumno).order_by('curso_academico', 'mes')#.reverse()

        if tipo == Globales.IPAE:
            if curso == Globales.PRIMERO:
                evaluaciones = Evaluacion_IPAE_PRIMERO.objects.filter \
                    (alumno=alumno).order_by('curso_academico', 'mes')#.reverse()
            if curso == Globales.SEGUNDO:
                evaluaciones = Evaluacion_IPAE_SEGUNDO.objects.filter \
                    (alumno=alumno).order_by('curso_academico', 'mes')#.reverse()
            if curso == Globales.TERCERO:
                evaluaciones = Evaluacion_IPAE_TERCERO.objects.filter \
                    (alumno=alumno).order_by('curso_academico', 'mes')#.reverse()

        plantilla = 'lista_evaluaciones.html'

        return render(request, plantilla,
                      {'evaluaciones': evaluaciones,
                       'alumno': alumno,
                       'tipo': tipo,
                       'curso': curso,
                       'index': server_url,
                       'server_url': server_url})

    except ObjectDoesNotExist:
        return render(request, 'error.html', {'error': "No tiene evaluaciones"})










# actualiza todos los cursos academicos de los
# alumnos en eun determinado grupo
def actualizar_curso_academico_grupo(request):
    print('>>> Actualizar los alumnos al nuevo curso academico del grupo')
    # grupo a actualizar
    id_grupo = request.GET['idGrupo']
    grupo = Grupo.objects.get(pk=id_grupo)
    print('>>> Actualizando curso academico del grupo ' + grupo.nombre)
    # comprobar los permisos en este grupo
    if not es_propietario_grupo(request, grupo):
        return render(request, 'error.html', {'error': ERROR_PROPIETARIO_GRUPO})
    # obtener todos los alumnos del grupo
    alumnos = Alumno.objects.filter(grupo=grupo)
    # actualizar
    for alumno in alumnos:
        alumno.curso_academico = grupo.curso_academico
        alumno.save()
        print('>>> Actualizado curso de ' + alumno.codigo)
    # volvemos al aula
    url_retorno = server_url + lista_alumnos_grupo_url + '/?idGrupo=' + id_grupo
    return redirect(url_retorno)


# listar alumnos de un grupo
def listar_alumnos_evaluador_en_grupo(request):
    # grupo al que se agregara el alumno
    id_grupo = request.GET['idGrupo']
    grupo = Grupo.objects.get(pk=id_grupo)
    # comprobar los permisos en este grupo
    if not es_propietario_grupo(request, grupo):
        return render(request,'error.html', {'error': ERROR_PROPIETARIO_GRUPO})
    mostrar_todos = True

    # comprobar si se ha filtrado por año academico
    if request.GET.get('cursoAcademico', ''):

        curso_academico = request.GET['cursoAcademico']

        if curso_academico == 'todos':
            mostrar_todos = True
            print('>>> Mostrando todos los alumnos sin filtro')

        else:
            print('>>> Filtrando por ' + str(curso_academico))

    else:
        # no se ha filtrado, recuperamos el curso por defecto
        curso_academico = grupo.curso_academico
        print('>>> Filtro por defecto ' + str(curso_academico))


    print('>>> Listando alumnos del grupo ' + grupo.nombre )

    try:

        # obtener alumnos solo de ese grupo
        # alumnos = Alumno.objects.filter(evaluador=request.user,grupo=grupo)

        # TODO COMRPOBAR QUE ERES EL PROPIETARIO DEL GRUPO
        # AHORA ESTA EL PROBLEMA DE QUE EL EVALUADOR DEBE APARECER
        # EN LA LISTA 'EVALUADORES' DEL GRUPO !!!!



        # filtros
        if mostrar_todos:
            alumnos = Alumno.objects.filter(grupo=grupo)

        else:
            alumnos = Alumno.objects.filter(grupo=grupo, curso_academico=curso_academico)


        # recuperar todas las evaluaciones asociadas
        # de cada alumno con IPAL, IPAM, IPAE de los momentos
        # INICIO, MEDIO, FIN

        print('>>> Recuperando evaluaciones')
        todas_evaluaciones = []  # lista de evaluaciones
        evas = {}


        for alumno in alumnos:

            print('- recuperado ' + alumno.codigo)

            # hacer las consultas
            modelo_IPAL = 'IPAL-' + alumno.curso
            modelo_IPAM = 'IPAM-' + alumno.curso
            modelo_IPAE = 'IPAE-' + alumno.curso


            if alumno.curso != Globales.TERCERO: # no hay tercero en IPAL
                IPAL = clases[modelo_IPAL]
                consulta_evaluaciones_IPAL = IPAL.objects.filter(alumno=alumno).filter(
                    Q(mes=Globales.NOVIEMBRE) |
                    Q(mes=Globales.FEBRERO) |
                    Q(mes=Globales.MAYO)
                )
                for registro_evaluacion in consulta_evaluaciones_IPAL:
                    print(registro_evaluacion.alumno.codigo + ' ' +
                          registro_evaluacion.mes_leible + ' ' +
                          registro_evaluacion.riesgo + ' ' +
                          registro_evaluacion.get_tipo_display())
                    todas_evaluaciones.append(registro_evaluacion)
                    key = str(alumno.pk) + registro_evaluacion.prueba + registro_evaluacion.momento
                    evas[key] = registro_evaluacion.riesgo



            if alumno.curso != Globales.INFANTIL: # no hay infantil en IPAE
                IPAE = clases[modelo_IPAE]
                consulta_evaluaciones_IPAE = IPAE.objects.filter(alumno=alumno).filter(
                    Q(mes=Globales.NOVIEMBRE) |
                    Q(mes=Globales.FEBRERO) |
                    Q(mes=Globales.MAYO)
                )
                for registro_evaluacion in consulta_evaluaciones_IPAE:
                    print(registro_evaluacion.alumno.codigo + ' ' +
                          registro_evaluacion.mes_leible + ' ' +
                          registro_evaluacion.riesgo + ' ' +
                          registro_evaluacion.get_tipo_display())
                    todas_evaluaciones.append(registro_evaluacion)
                    key = str(alumno.pk) + registro_evaluacion.prueba + registro_evaluacion.momento
                    evas[key] = registro_evaluacion.riesgo


            IPAM = clases[modelo_IPAM]
            consulta_evaluaciones_IPAM = IPAM.objects.filter(alumno=alumno).filter(
                Q(mes=Globales.NOVIEMBRE) |
                Q(mes=Globales.FEBRERO) |
                Q(mes=Globales.MAYO)
            )



            for registro_evaluacion in consulta_evaluaciones_IPAM:
                print(registro_evaluacion.alumno.codigo + ' ' +
                      registro_evaluacion.mes_leible + ' ' +
                      registro_evaluacion.riesgo + ' ' +
                      registro_evaluacion.get_tipo_display())
                todas_evaluaciones.append(registro_evaluacion)
                key = str(alumno.pk) + registro_evaluacion.prueba + registro_evaluacion.momento
                evas[key] = registro_evaluacion.riesgo


        return render(request, 'lista_alumnos_grupo.html',
                      { 'grupo': grupo,
                        'alumnos': alumnos,
                        'evaluaciones': todas_evaluaciones,
                        'evas':evas,
                        'curso_filtrado':curso_academico,
                        'index': server_url,
                        'server_url': server_url})

    except ObjectDoesNotExist:
        return render(request, 'error.html', {'error': "No tiene alumnos"})






@login_required
def compartir_grupo_centro(request):
    print('>>> Compartiendo el aula del centro')
    # obtennemos el grupo y el evaluador
    id_grupo = request.GET['idGrupo']
    grupo = Grupo.objects.get(pk=id_grupo)
    evaluador = Evaluador.objects.get(usuario=request.user)
    # agregar al grupo del centro el evaluador
    grupo.evaluadores.add(evaluador.usuario)
    grupo.save()
    print('>>> Grupo ' + grupo.nombre + ' en el centro ' + grupo.centro_pilotaje + ' compartido con ' + evaluador.nombre)
    return redirect(server_url + lista_grupos_url)



# listar grupos del evaluador (consejeria)
def lista_grupos_evaluador_consejeria(request):
    print('>>> Obteniendo listado de grupos del centro del evaluador')
    try:
        # obtenemos los grupos que pertenecen al centro del
        # evaluador
        evaluador = Evaluador.objects.get(usuario=request.user)
        print('>>> Centro del evaluador ' + evaluador.nombre + ' es ' + evaluador.centro_pilotaje)
        gruposCentro = Grupo.objects.filter(centro_pilotaje=evaluador.centro_pilotaje)
        url_retorno = server_url + lista_grupos_url
        return render(request, 'lista_grupos_consejeria.html',
                      {'grupos': gruposCentro,
                       'index': server_url,
                       'url_retorno': url_retorno,
                       'server_url': server_url})


    except ObjectDoesNotExist:
        return render(request,
                      'error.html', {'error': ERROR_LISTADO_GRUPOS})



# listar grupos del evaluador
@login_required
def lista_grupos_evaluador(request):
    print('>>> Obteniendo lista de grupos del evaluador')
    try:
        # obtenemos los grupos del usuario
        grupos = Grupo.objects.filter(evaluadores__pk=request.user.pk).order_by('curso_academico').reverse()
        return render(request, 'lista_grupos.html',
                      {'grupos': grupos,
                       'index': server_url,
                       'server_url': server_url})

    except ObjectDoesNotExist:
        return render(request,
                      'error.html', {'error': ERROR_LISTADO_GRUPOS})





# nuevo grupo
def nuevo_grupo(request):
    print('>>> Creando nuevo grupo')
    url_retorno = server_url + lista_grupos_url
    if request.method == "POST":
        form = FormGrupo(request.POST)
        if form.is_valid():
            grupo = form.save(commit=False)
            # establecer al creador del grupo
            # y agregarlo a la lista de evaluadores
            grupo.evaluador = request.user
            # agregar al grupo un nuevo evaluador
            grupo.save()
            grupo.evaluadores.add(request.user)

            return redirect(url_retorno)
    else:
        form = FormGrupo()
    return render(request, 'nuevo_grupo.html', {'form': form, 'index':server_url,'server_url': url_retorno})


# editar el perfil del evaluador
def editar_evaluador(request):
    print('>>> Editando perfil del evaluador')
    url_retorno = server_url
    evaluador = get_object_or_404(Evaluador, usuario=request.user)

    if request.method == "POST":
        form = FormEvaluador(request.POST, instance=evaluador)
        if form.is_valid():
            evaluador = form.save(commit=False)
            evaluador.usuario = request.user
            evaluador.save()
            return redirect(url_retorno)
    else:
        form = FormEvaluador(instance=evaluador)
    return render(request, 'form_editar_evaluador.html',
                  {'form': form, 'id_evaluador':evaluador.pk,'index':server_url,'server_url': url_retorno})


# editar un grupo
def editar_grupo(request):
    print('>>> Editando grupo')
    url_retorno = server_url + lista_grupos_url
    id = request.GET['id']
    grupo = get_object_or_404(Grupo, pk=id)

    # comprobar los permisos en este grupo
    if not es_creador_grupo(request, grupo):
    #if not es_propietario_alumno(request, grupo):
        return render(request,'error.html', {'error': ERROR_PROPIETARIO_GRUPO})

    if request.method == "POST":
        form = FormGrupo(request.POST, instance=grupo)
        if form.is_valid():
            grupo = form.save(commit=False)
            # El evaluador que cree el grupo estara siempre
            # en su campo evaluador. Este campo no se actualiza
            # nunca mas
            grupo.save()
            return redirect(url_retorno)
    else:
        form = FormGrupo(instance=grupo)
    return render(request, 'form_editar_grupo.html', {'form': form, 'index':server_url,'server_url': url_retorno})









# nuevo alumno sin que el evaluador pueda
# seleccionar el grupo, se asigna automaticamente
def nuevo_alumno(request):
    print('>>> Nuevo alumno (asignado a grupo automaticamente)')
    id_grupo = request.GET['idGrupo']
    grupo = get_object_or_404(Grupo, pk=id_grupo)
    print('>>> Grupo al que pertenecera: ' + grupo.nombre + ' | ' + grupo.curso)
    url_retorno = server_url + lista_alumnos_grupo_url + '/?idGrupo=' + id_grupo
    if request.method == "POST":

        form = FormAlumnoGrupoForzado(request.POST)

        if form.is_valid():
            alumno = form.save(commit=False)
            # obtener evaluador
            alumno.evaluador = request.user
            evaluador = Evaluador.objects.get(usuario=request.user) # pk=alumno.evaluador.pk)

            alumno.grupo = grupo # asignamos el grupo actual
            alumno.curso = grupo.curso # asignamos el curso del grupo
            alumno.centro = grupo.centro # asignamos el centro del grupo

            alumno.centro_pilotaje = evaluador.centro_pilotaje # asignameos el centro pilotje
            alumno.pais = evaluador.pais  # fijar el pais del evaluador
            alumno.codigo_evaluador = evaluador.codigo   # fijar el codigo del evaluacodr

            alumno.save()
            return redirect(url_retorno)
    else:
        form = FormAlumnoGrupoForzado()
    return render(request, 'form_nuevo_alumno.html',
                  {'form': form, 'index':server_url,'server_url': url_retorno})




# crear un nuevo alumno permitiendo al evaluador
# seleccionar el grupo al que pertenecera el alumno
def nuevo_alumno_Grupo(request):
    print('>>> Nuevo alumno')
    id_grupo = request.GET['idGrupo']
    grupo = get_object_or_404(Grupo, pk=id_grupo)
    print('>>> Grupo al que pertenecera: ' + grupo.nombre + ' | ' + grupo.curso)
    url_retorno = server_url + lista_alumnos_grupo_url + '/?idGrupo=' + id_grupo
    if request.method == "POST":
        form = FormAlumno(request.user, request.POST)

        if form.is_valid():
            alumno = form.save(commit=False)
            alumno.evaluador = request.user
            alumno.grupo = grupo
            alumno.save()
            return redirect(server_url )
    else:
        form = FormAlumno(request.user)
    return render(request, 'form_nuevo_alumno.html',
                  {'form': form, 'index':server_url,'server_url': url_retorno})



# editar un alumno
def editar_alumno(request):

    id_alumno = request.GET['idAlumno']
    id_grupo = request.GET['idGrupo']
    alumno = get_object_or_404(Alumno, pk=id_alumno)


    # comprobar los permisos en este alumno
    if not es_propietario_alumno(request, alumno):
        return render(request,'error.html', {'error': ERROR_PROPIETARIO_ALUMNO})


    print('>>> Editando alumno ' + alumno.codigo)
    url_retorno = server_url + lista_alumnos_grupo_url + '/?idGrupo=' + id_grupo
    if request.method == "POST":
        print('salvando')
        if es_participante(request):
            form = FormAlumnoConsejeriaPOST(request.POST, instance=alumno)
        else :
            form = FormAlumnoPOST(request.POST, instance=alumno)
        if form.is_valid():
            alumno = form.save(commit=False)
            alumno.save()
            return redirect(url_retorno)
    else:
        print('editando')
        if es_participante(request):
            form = FormAlumnoConsejeria(request.user, instance=alumno)
        else:
            form = FormAlumno(request.user, instance=alumno)
    return render(request, 'form_editar_alumno.html',
                  {'form': form, 'index':server_url,
                   'server_url': url_retorno, 'alumno':alumno, 'grupo':id_grupo})











# listar alumnos del evaluador
def listar_alumnos_evaluador(request):
    try:
        # obtener alumnos
        alumnos = Alumno.objects.filter(evaluador=request.user).order_by('grupo')
        return render(request, 'lista_alumnos.html',
                      {'alumnos': alumnos,'index': server_url})
    except ObjectDoesNotExist:
        return render(request, 'error.html', {'error': "No tiene alumnos"})





# SUBIR CSV Y PROCESARLO, IMPORTANTE:
# EL FICHERO DEBE SER UTF8 SIN BOM, EN CASO
# CONTRARIO EL PRIMER CARACTER SERA UN CARACTER ESPECIAL (BOM)
def importar_csv(request):

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
                      fields[2] + ', ' + fields[3] + ', ' + fields[4] + ', ' + fields[5])

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

    return redirect(server_url)



def exportar_CSV(request):
    print('>>> Exportando CSV')
    tipo_datos = request.GET['tipo']

    # respuesta
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="datos.csv"'
    writer = csv.writer(response, delimiter=',')

    if tipo_datos == 'grupos':
        print('>>> Exportando grupos')
        grupos = Grupo.objects.all()
        writer.writerow(['nombre','centro_pilotaje','codigo,''curso','curso_academico'])
        for grupo in grupos:
            writer.writerow([grupo.nombre, grupo.centro_pilotaje, grupo.codigo,grupo.curso, grupo.curso_academico])

    if tipo_datos == 'alumnos':
        print('>>> Exportando alumnos')
        # obtenemos todos los alumnos
        alumnos = Alumno.objects.all()
        # cabecera y fichero
        writer.writerow(['codigo', 'genero', 'curso', 'fecha nacimiento',
                         'pais', 'centro', 'grupo', 'id grupo', 'evaluador', 'curso academico' ])
        for alumno in alumnos:
            writer.writerow([alumno.codigo, alumno.sexo, alumno.curso,
            alumno.fecha_nacimiento, alumno.pais, alumno.centro_pilotaje, alumno.grupo.nombre,
            alumno.grupo.pk, alumno.codigo_evaluador, alumno.curso_academico
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
                e.alumno,e.evaluador,e.alumno.centro,e.curso_academico,e.ultima_modificacion,e.prueba,e.mes, e.tipo,
                e.ADIVINANZAS,e.CSL,e.CNL,e.CLE_IMAGEN,e.CLE_TEXTO,e.CFA,e.evaluado
                ])

        if curso == 'PRIMERO':
            writer.writerow(Encabezados.encabezado_IPAL_PRIMERO)
            for e in evaluaciones:
                writer.writerow([
                    e.alumno,e.evaluador,e.alumno.centro,e.curso_academico,e.ultima_modificacion,e.prueba,e.mes,e.tipo,
                    e.TM,e.LP,e.CSL,e.CNL,e.FLO,e.CLE_TEXTO,e.CFS,e.evaluado
                ])             
            
        if curso == 'SEGUNDO':
            writer.writerow(Encabezados.encabezado_IPAL_SEGUNDO)
            for e in evaluaciones:
                writer.writerow([
                e.alumno, e.evaluador,e.alumno.centro,  e.curso_academico,e.ultima_modificacion, e.prueba,e.mes, e.tipo,
                e.TM,e.LP,e.CSL,e.CNL,e.FLO,e.CLE_TEXTO,e.CFS,e.PRO,e.VOC,e.evaluado
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
                e.alumno,e.evaluador,e.alumno.centro,e.curso_academico,e.ultima_modificacion,e.prueba,e.mes, e.tipo,
                e.CN,e.EC,e.SN,e.IN,e.CVA,e.CM,e.evaluado
                ])
        if curso == 'PRIMERO' or curso == 'SEGUNDO' or curso == 'TERCERO':
            writer.writerow(Encabezados.encabezado_IPAM_PRIMERO)
            for e in evaluaciones:
                writer.writerow([
                e.alumno,e.evaluador,e.alumno.centro,e.curso_academico,e.ultima_modificacion,e.prueba,e.mes, e.tipo,
                e.CN,e.ODD,e.SN,e.OUD,e.VP,e.evaluado
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
                e.alumno,e.evaluador,e.alumno.centro,e.curso_academico,e.ultima_modificacion,e.prueba,e.mes, e.tipo,
                e.TLC_1,e.DICTADO_ORTOGRAFIA_ARBITRARIA,e.DICTADO_ORTOGRAFIA_REGLADA,e.DICTADO_PSEUDOPALABRAS,
                e.DICTADO_FRASES,e.evaluado
                ])
        if curso == 'TERCERO':
            writer.writerow(Encabezados.encabezado_IPAE_TERCERO)
            for e in evaluaciones:
                writer.writerow([
                e.alumno,e.evaluador,e.alumno.centro,e.curso_academico,e.ultima_modificacion,e.prueba,e.mes, e.tipo,
                e.DICTADO_ORTOGRAFIA_ARBITRARIA,e.DICTADO_ORTOGRAFIA_REGLADA,e.DICTADO_FRASES,
                e.SEC_5, e.SEC_SEI_5,e.PDC_5,e.evaluado
                ])


    # devolver el fichero para descargar
    return response

