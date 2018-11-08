from django.contrib import admin

from .models import Evaluador, Grupo, Alumno,  \
    Evaluacion_IPAL_INFANTIL, Evaluacion_IPAL_PRIMERO, Evaluacion_IPAL_SEGUNDO, \
    Evaluacion_IPAM_INFANTIL, Evaluacion_IPAM_PRIMERO, Evaluacion_IPAM_SEGUNDO, Evaluacion_IPAM_TERCERO, \
    Evaluacion_IPAE_PRIMERO, Evaluacion_IPAE_SEGUNDO, Evaluacion_IPAE_TERCERO


class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('codigo','sexo','centro_pilotaje','grupo','evaluador')
    search_fields = ('codigo', 'centro_pilotaje', 'grupo','evaluador')
    list_filter = ('centro_pilotaje','grupo')

class EvaluadorAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'centro_pilotaje', 'email')
    search_fields = ('codigo', 'nombre', 'centro_pilotaje', 'email')
    list_filter = ('centro_pilotaje',)


class GrupoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'curso', 'evaluador', 'centro_pilotaje')
    search_fields = ('codigo', 'nombre', 'curso', 'evaluador', 'centro_pilotaje')
    list_filter = ('centro_pilotaje',)


class IPAE_PRIMERO_Admin(admin.ModelAdmin):
    list_display = ('alumno', 'evaluador', 'mes', 'tipo')
    search_fields = ('alumno', 'evaluador', 'mes', 'tipo')

class IPAE_SEGUNDO_Admin(admin.ModelAdmin):
    list_display = ('alumno', 'evaluador', 'mes', 'tipo')
    search_fields = ('alumno', 'evaluador', 'mes', 'tipo')

class IPAE_TERCERO_Admin(admin.ModelAdmin):
    list_display = ('alumno', 'evaluador', 'mes', 'tipo')
    search_fields = ('alumno', 'evaluador', 'mes', 'tipo')



class IPAL_PRIMERO_Admin(admin.ModelAdmin):
    list_display = ('alumno', 'evaluador', 'mes', 'tipo')
    search_fields = ('alumno', 'evaluador', 'mes', 'tipo')

class IPAL_SEGUNDO_Admin(admin.ModelAdmin):
    list_display = ('alumno', 'evaluador', 'mes', 'tipo')
    search_fields = ('alumno', 'evaluador', 'mes', 'tipo')

class IPAL_INFANTIL_Admin(admin.ModelAdmin):
    list_display = ('alumno', 'evaluador', 'mes', 'tipo')
    search_fields = ('alumno', 'evaluador', 'mes', 'tipo')



class IPAM_PRIMERO_Admin(admin.ModelAdmin):
    list_display = ('alumno', 'evaluador', 'mes', 'tipo')
    search_fields = ('alumno', 'evaluador', 'mes', 'tipo')

class IPAM_SEGUNDO_Admin(admin.ModelAdmin):
    list_display = ('alumno', 'evaluador', 'mes', 'tipo')
    search_fields = ('alumno', 'evaluador', 'mes', 'tipo')

class IPAM_TERCERO_Admin(admin.ModelAdmin):
    list_display = ('alumno', 'evaluador', 'mes', 'tipo')
    search_fields = ('alumno', 'evaluador', 'mes', 'tipo')

class IPAM_INFANTIL_Admin(admin.ModelAdmin):
    list_display = ('alumno', 'evaluador', 'mes', 'tipo')
    search_fields = ('alumno', 'evaluador', 'mes', 'tipo')
    

admin.site.register(Evaluador, EvaluadorAdmin)
admin.site.register(Grupo, GrupoAdmin)
admin.site.register(Alumno,AlumnoAdmin)


admin.site.register(Evaluacion_IPAL_INFANTIL, IPAL_INFANTIL_Admin)
admin.site.register(Evaluacion_IPAL_PRIMERO, IPAL_PRIMERO_Admin)
admin.site.register(Evaluacion_IPAL_SEGUNDO, IPAL_SEGUNDO_Admin)

admin.site.register(Evaluacion_IPAM_INFANTIL, IPAM_INFANTIL_Admin)
admin.site.register(Evaluacion_IPAM_PRIMERO, IPAM_PRIMERO_Admin)
admin.site.register(Evaluacion_IPAM_SEGUNDO, IPAM_SEGUNDO_Admin)
admin.site.register(Evaluacion_IPAM_TERCERO, IPAM_TERCERO_Admin)

admin.site.register(Evaluacion_IPAE_PRIMERO, IPAE_PRIMERO_Admin)
admin.site.register(Evaluacion_IPAE_SEGUNDO, IPAE_SEGUNDO_Admin)
admin.site.register(Evaluacion_IPAE_TERCERO, IPAE_TERCERO_Admin)