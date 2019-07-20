from django import template
from django.conf import settings

register = template.Library()

# devuelve si una evaluacion esta completa
@register.assignment_tag
def evaluacion_completa(evaluacion):
    return evaluacion.evaluacion_completa()

@register.assignment_tag
def es_evaluacion_completa(lista_tareas):
    # recorremos la lista, es completa si todas
    # las tareas son diferentes a -1
    for tarea in lista_tareas:
        if tarea == -1:
            return False
    return True


@register.assignment_tag
def es_evaluacion_incompleta(lista_tareas):

    # si 1: si es completa

    if (es_evaluacion_completa(lista_tareas)):
        return False

    # 2: por lo menos unas de las tareas esta completa
    for tarea in lista_tareas:
        if tarea != -1:
            return True

    # en este caso esta toda a -1
    return False



# redondea el omnibus
@register.simple_tag
def omnibus_redondeado(omnibus):
    return round(omnibus, 6)


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
    #return 'http://webrti.ull.es/'

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