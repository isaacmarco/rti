from django import template
from django.conf import settings

register = template.Library()

# devuelve el formato de año academico
@register.simple_tag
def get_curso(curso):
    siguiente = curso + 1
    return str(curso) + '-' + str(siguiente)

@register.simple_tag
def get_server_url():
    return settings.DIRECCION
    #return 'http://127.0.0.1:8000/'
    #return 'http://193.145.96.31/'

# devuelve el riesgo IPAL de cada
# tarea segun su puntuacion directa
#@register.simple_tag
#def tarea(tarea, puntuacion_directa):



# devuelve true si el usuario puede eliminar alumnos
@register.filter
def puede_eliminar_alumno(usuario):
    # solo investigadores o usuarios normales de la plataforma pueden
    # eliminar. No esta permitido para el profesorado participante
    return True if es_investigador(usuario) or not es_participante(usuario) else False

# devuelve true si el usuario tiene el rol de participante en el experimento
@register.filter
def es_participante(usuario):
    return True if usuario.groups.filter(name='participantes').exists() else False

# devuelve true si el usuario tiene el rol de investigador
@register.filter
def es_investigador(usuario):
    return True if usuario.groups.filter(name='investigadores').exists() else False

# devuelve el color segun la constante de riesgo
@register.simple_tag
def color(key):
    colores_riesgo = {
        "NOEV": "#808080",
        "ALTR": "#850202",
        "RIES": "#f00",
        "BAJO": "#fff200",
        "NORM": "#009fff",
        "OPTI": "#1ae36e"
    }
    try:
        color = colores_riesgo[key]
    except:
        return colores_riesgo['NOEV']
    return color


# devuelve un elemento de un diccionario
# parametro por su key parametro
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)