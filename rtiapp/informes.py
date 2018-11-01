'''
from rtiapp.views import server_url, colores_riesgo
from .models import Grupo, Alumno
import rtiapp.constantes as Globales
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

# generar datos y mostrar el informe general
# de grupo
def informe_grupo(request):

    print('>>> Informe de grupo')
    # obtener el grupo y recuperar los alumnos
    id_grupo = request.GET['idGrupo']
    grupo = Grupo.objects.get(pk=id_grupo)
    curso = grupo.curso
    prueba = request.GET['prueba']
    url_retorno = server_url + 'lista-alumnos-grupo' + '/?idGrupo=' + id_grupo
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

'''
