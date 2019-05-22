from django.contrib import admin



from .models import Evaluador, Grupo, Alumno,  \
    Evaluacion_IPAL_INFANTIL, Evaluacion_IPAL_PRIMERO, Evaluacion_IPAL_SEGUNDO, \
    Evaluacion_IPAM_INFANTIL, Evaluacion_IPAM_PRIMERO, Evaluacion_IPAM_SEGUNDO, Evaluacion_IPAM_TERCERO, \
    Evaluacion_IPAE_PRIMERO, Evaluacion_IPAE_SEGUNDO, Evaluacion_IPAE_TERCERO


class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('codigo','sexo','centro_pilotaje','grupo','evaluador','fecha_alta')
    search_fields = ['codigo', 'centro_pilotaje', 'grupo','evaluador']
    list_filter = ('centro_pilotaje','grupo')


class EvaluadorAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'centro_pilotaje', 'email','usuario','fecha_alta')
    search_fields = ['codigo', 'nombre', 'centro_pilotaje', 'email', 'usuario']
    list_filter = ('centro_pilotaje',)
    list_per_page = 9999

class GrupoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'curso', 'evaluador', 'centro_pilotaje','fecha_alta')
    search_fields = ['codigo', 'nombre', 'curso', 'evaluador', 'centro_pilotaje']
    list_filter = ('centro_pilotaje','centro', 'evaluador')


class IPAE_PRIMERO_Admin(admin.ModelAdmin):
    list_display = ('alumno', 'evaluador', 'mes', 'tipo', 'evaluado', 'get_grupo')
    list_filter = ('evaluador', )
    search_fields = ['alumno', 'evaluador', 'mes', 'tipo']
    list_per_page = 9999
    def get_grupo(self, obj):
        return obj.alumno.grupo
    get_grupo.short_description = 'Grupo'

class IPAE_SEGUNDO_Admin(admin.ModelAdmin):
    list_display = ('alumno', 'evaluador', 'mes', 'tipo', 'evaluado', 'get_grupo')
    list_filter = ('evaluador',)
    search_fields = ['alumno', 'evaluador', 'mes', 'tipo']
    list_per_page = 9999
    def get_grupo(self, obj):
        return obj.alumno.grupo
    get_grupo.short_description = 'Grupo'

class IPAE_TERCERO_Admin(admin.ModelAdmin):
    list_display = ('alumno', 'evaluador', 'mes', 'tipo', 'evaluado', 'get_grupo')
    list_filter = ('evaluador',)
    search_fields = ['alumno', 'evaluador', 'mes', 'tipo']
    list_per_page = 9999
    def get_grupo(self, obj):
        return obj.alumno.grupo
    get_grupo.short_description = 'Grupo'


class IPAL_PRIMERO_Admin(admin.ModelAdmin):
    list_display = ('alumno', 'evaluador', 'mes', 'tipo', 'evaluado','get_grupo')
    list_filter = ('evaluador',)
    search_fields = ['alumno', 'evaluador', 'mes', 'tipo']
    list_per_page = 9999
    def get_grupo(self, obj):
        return obj.alumno.grupo
    get_grupo.short_description = 'Grupo'


class IPAL_SEGUNDO_Admin(admin.ModelAdmin):
    list_display = ('alumno', 'evaluador', 'mes', 'tipo', 'evaluado', 'get_grupo')
    list_filter = ('evaluador',)
    search_fields = ['alumno', 'evaluador', 'mes', 'tipo']
    list_per_page = 9999
    def get_grupo(self, obj):
        return obj.alumno.grupo
    get_grupo.short_description = 'Grupo'

class IPAL_INFANTIL_Admin(admin.ModelAdmin):
    list_display = ('alumno', 'evaluador', 'mes', 'tipo', 'evaluado', 'get_grupo')
    list_filter = ('evaluador',)
    search_fields = ['alumno', 'evaluador', 'mes', 'tipo']
    list_per_page = 9999
    def get_grupo(self, obj):
        return obj.alumno.grupo
    get_grupo.short_description = 'Grupo'

class IPAM_PRIMERO_Admin(admin.ModelAdmin):
    list_display = ('alumno', 'evaluador', 'mes', 'tipo', 'evaluado', 'get_grupo')
    list_filter = ('evaluador',)
    search_fields = ['alumno', 'evaluador', 'mes', 'tipo']
    list_per_page = 9999
    def get_grupo(self, obj):
        return obj.alumno.grupo
    get_grupo.short_description = 'Grupo'

class IPAM_SEGUNDO_Admin(admin.ModelAdmin):
    list_display = ('alumno', 'evaluador', 'mes', 'tipo', 'evaluado', 'get_grupo')
    list_filter = ('evaluador',)
    search_fields = ['alumno', 'evaluador', 'mes', 'tipo']
    list_per_page = 9999
    def get_grupo(self, obj):
        return obj.alumno.grupo
    get_grupo.short_description = 'Grupo'

class IPAM_TERCERO_Admin(admin.ModelAdmin):
    list_display = ('alumno', 'evaluador', 'mes', 'tipo', 'evaluado', 'get_grupo')
    list_filter = ('evaluador',)
    search_fields = ['alumno', 'evaluador', 'mes', 'tipo']
    list_per_page = 9999
    def get_grupo(self, obj):
        return obj.alumno.grupo
    get_grupo.short_description = 'Grupo'

class IPAM_INFANTIL_Admin(admin.ModelAdmin):
    list_display = ('alumno', 'evaluador', 'mes', 'tipo', 'evaluado', 'get_grupo')
    list_filter = ('evaluador',)
    search_fields = ['alumno', 'evaluador', 'mes', 'tipo']
    list_per_page = 9999
    def get_grupo(self, obj):
        return obj.alumno.grupo
    get_grupo.short_description = 'Grupo'

admin.site.register(Evaluador, EvaluadorAdmin)
admin.site.register(Grupo, GrupoAdmin)
admin.site.register(Alumno, AlumnoAdmin)


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