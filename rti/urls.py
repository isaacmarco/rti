from django.conf.urls import include, url
from django.contrib import admin
from rtiapp.views import index
from django.contrib.auth import views as auth_views

from rtiapp.views import \
    editar_evaluador,  \
    nuevo_grupo, editar_grupo,  lista_grupos_evaluador,\
    nuevo_alumno,editar_alumno,\
    listar_alumnos_evaluador_en_grupo,\
    listar_evaluaciones,nueva_evaluacion, editar_evaluacion, alta_evaluador,documentos,informe_grupo,\
    establecer_curso,actualizar_curso,compartir_grupo,actualizar_grupo_compartido,exportar,exportar_CSV, \
    cerrar_sesion,informe_individual


urlpatterns = [

    # plataforma
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
    url(r'^alta/', alta_evaluador),
    url(r'^documentos/', documentos),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^cerrar-sesion/', cerrar_sesion),

    # exportar datos
    url(r'^exportar/', exportar),
    url(r'^exportar-csv/', exportar_CSV),

    # informes
    url(r'^informe-grupo/', informe_grupo),
    url(r'^informe-individual/', informe_individual),

    # evaluador
    url(r'^editar-evaluador/', editar_evaluador),
    url(r'^establecer-curso/', establecer_curso),
    url(r'^actualizar-curso/', actualizar_curso),

    # grupos
    url(r'^nuevo-grupo/', nuevo_grupo),
    url(r'^editar-grupo/', editar_grupo),
    url(r'^lista-grupos/', lista_grupos_evaluador),
    url(r'^compartir-grupo/', compartir_grupo),
    url(r'^actualizar-grupo-compartido/', actualizar_grupo_compartido),

    # alumnos
    url(r'^nuevo-alumno/', nuevo_alumno),
    url(r'^editar-alumno/', editar_alumno),
    url(r'^lista-alumnos-grupo/', listar_alumnos_evaluador_en_grupo),

    # evaluaciones
    url(r'^lista-evaluaciones/', listar_evaluaciones),
    url(r'^nueva-evaluacion/', nueva_evaluacion),
    url(r'^editar-evaluacion/', editar_evaluacion),

]
