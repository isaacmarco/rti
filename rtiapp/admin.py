from django.contrib import admin

from .models import Evaluador, Grupo, Alumno,  \
    Evaluacion_IPAL_INFANTIL, Evaluacion_IPAL_PRIMERO, Evaluacion_IPAL_SEGUNDO, \
    Evaluacion_IPAM_INFANTIL, Evaluacion_IPAM_PRIMERO, Evaluacion_IPAM_SEGUNDO, Evaluacion_IPAM_TERCERO, \
    Evaluacion_IPAE_PRIMERO, Evaluacion_IPAE_SEGUNDO, Evaluacion_IPAE_TERCERO


# TODO BORRA ESTO !
from .models import Ubicacion, Emblema, Explorador

admin.site.register(Ubicacion)
admin.site.register(Emblema)
admin.site.register(Explorador)


admin.site.register(Evaluador)
admin.site.register(Grupo)
admin.site.register(Alumno)


admin.site.register(Evaluacion_IPAL_INFANTIL)
admin.site.register(Evaluacion_IPAL_PRIMERO)
admin.site.register(Evaluacion_IPAL_SEGUNDO)

admin.site.register(Evaluacion_IPAM_INFANTIL)
admin.site.register(Evaluacion_IPAM_PRIMERO)
admin.site.register(Evaluacion_IPAM_SEGUNDO)
admin.site.register(Evaluacion_IPAM_TERCERO)

admin.site.register(Evaluacion_IPAE_PRIMERO)
admin.site.register(Evaluacion_IPAE_SEGUNDO)
admin.site.register(Evaluacion_IPAE_TERCERO)