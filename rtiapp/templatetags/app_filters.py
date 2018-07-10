from django import template


register = template.Library()

# devuelve el formato de año academico
@register.simple_tag
def get_curso(curso):
    siguiente = curso + 1
    return str(curso) + '-' + str(siguiente)

# devuelve si estamos en la pagina de login
#@register.simple_tag
#def get_loggin(url):
 #   return url == '/log/'

# devuelve el color segun la constante de riesgo
@register.simple_tag
def color(key):
    colores_riesgo = {
        "NOEV": "#808080",
        "ALTR": "#850202",
        "RIES": "#f00",
        "BAJO": "#ffa500",
        "NORM": "#1ae36e",
        "OPTI": "#009fff"
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