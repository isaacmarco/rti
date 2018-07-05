from django.conf.urls import include, url
from django.contrib import admin
from rtiapp.views import index
from rtiapp.views import \
    editar_evaluador,  \
    nuevo_grupo, editar_grupo,  lista_grupos_evaluador,\
    nuevo_alumno,editar_alumno,\
    listar_alumnos_evaluador_en_grupo,\
    listar_evaluaciones,nueva_evaluacion, editar_evaluacion, alta_evaluador,documentos,informe_grupo,\
    establecer_curso,actualizar_curso,compartir_grupo,actualizar_grupo_compartido,exportar

# DELETE
from rtiapp.views import comprobar_ubicacion

urlpatterns = [

    # TODO EXPLORADORES
    url(r'^comprobar-ubicacion/', comprobar_ubicacion),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
    url(r'^alta/', alta_evaluador),
    url(r'^documentos/', documentos),
    url(r'^establecer-curso/', establecer_curso),
    url(r'^actualizar-curso/', actualizar_curso),
    url(r'^compartir-grupo/', compartir_grupo),
    url(r'^actualizar-grupo-compartido/', actualizar_grupo_compartido),
    url(r'^exportar/', exportar),

    # informes
    url(r'^informe-grupo/', informe_grupo),


    # evaluador
    url(r'^editar-evaluador/', editar_evaluador),


    # grupos
    url(r'^nuevo-grupo/', nuevo_grupo),
    url(r'^editar-grupo/', editar_grupo),
    # url(r'^vista-grupo/', vista_grupo),
    url(r'^lista-grupos/', lista_grupos_evaluador),

    # alumnos
    url(r'^nuevo-alumno/', nuevo_alumno),
    url(r'^editar-alumno/', editar_alumno),
    url(r'^lista-alumnos-grupo/', listar_alumnos_evaluador_en_grupo),

    # listar evaluaciones
    url(r'^lista-evaluaciones/', listar_evaluaciones),

    # nuevas evaluaciones
    url(r'^nueva-evaluacion/', nueva_evaluacion),


    # editar evaluaciones
    url(r'^editar-evaluacion/', editar_evaluacion),

]
