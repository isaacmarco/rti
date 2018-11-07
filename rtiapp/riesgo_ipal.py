import rtiapp.constantes as Globales

# riesgos por puntuaciones directas de cada tarea
# los parametros son siglas de la tarea, momento: inicio
# medio, fin, y la puntuacion directa en la tarea pd

# REVISADO CON JUANE

# riesgo por omnibus

def riesgo_INFANTIL(omnibus, momento):

      if momento == Globales.INICIO:

        if (omnibus <= -0.180658475):
            return Globales.RIESGO
        if (omnibus > -0.180658475 and omnibus <= -0.07171876):
            return Globales.BAJO
        if (omnibus > -0.07171876 and omnibus <= 0.098911218):
            return Globales.NORMAL
        if (omnibus > 0.098911218):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL INFANTIL')
        return 404


      if momento == Globales.MEDIO:

        if (omnibus <= -0.384165007):
            return Globales.RIESGO
        if (omnibus > -0.384165007 and omnibus <= -0.043928001):
            return Globales.BAJO
        if (omnibus > -0.043928001 and omnibus <= 0.168002466):
            return Globales.NORMAL
        if (omnibus > 0.168002466):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL INFANTIL')
        return 404

      if momento == Globales.FIN:

        if (omnibus <= -0.329980387):
            return Globales.RIESGO
        if (omnibus > -0.329980387 and omnibus <= -0.00458066):
            return Globales.BAJO
        if (omnibus > -0.00458066 and omnibus <= 0.131335391):
            return Globales.NORMAL
        if (omnibus > 0.131335391):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL INFANTIL')
        return 404



def riesgo_PRIMERO(omnibus, momento):

    if momento == Globales.INICIO:

        if (omnibus <= -0.551320299):
            return Globales.RIESGO
        if (omnibus > -0.551320299 and omnibus <= -0.029852734):
            return Globales.BAJO
        if (omnibus > -0.029852734 and omnibus <= 0.303682631):
            return Globales.NORMAL
        if (omnibus > 0.303682631):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL PRIMERO')
        return 404

    if momento == Globales.MEDIO:

        if (omnibus <= -0.328134203):
            return Globales.RIESGO
        if (omnibus > -0.328134203 and omnibus <= 0.017611857):
            return Globales.BAJO
        if (omnibus > 0.017611857 and omnibus <= 0.183694698):
            return Globales.NORMAL
        if (omnibus > 0.183694698):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL PRIMERO')
        return 404

    if momento == Globales.FIN:

        if (omnibus <= -0.318496649):
            return Globales.RIESGO
        if (omnibus > -0.318496649 and omnibus <= 0.040984993):
            return Globales.BAJO
        if (omnibus > 0.040984993 and omnibus <= 0.207333494):
            return Globales.NORMAL
        if (omnibus > 0.207333494):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL PRIMERO')
        return 404




def riesgo_SEGUNDO(omnibus, momento):

    if momento == Globales.INICIO:

        if (omnibus <= -0.5108):
            return Globales.RIESGO
        if (omnibus > -0.5108 and omnibus <= 0.0946):
            return Globales.BAJO
        if (omnibus > 0.0946 and omnibus <= 0.1172):
            return Globales.NORMAL
        if (omnibus >0.1172):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL SEGUNDO')
        return 404

    if momento == Globales.MEDIO:

        if (omnibus <=  -0.2862):
            return Globales.RIESGO
        if (omnibus > -0.2862 and omnibus <= 0.0287):
            return Globales.BAJO
        if (omnibus > 0.0287 and omnibus <= 0.1795):
            return Globales.NORMAL
        if (omnibus > 0.1795):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL SEGUNDO')
        return 404

    if momento == Globales.FIN:

        if (omnibus <= -0.5143):
            return Globales.RIESGO
        if (omnibus > -0.5143 and omnibus <= 0.0360):
            return Globales.BAJO
        if (omnibus > 0.0360 and omnibus <= 0.1232):
            return Globales.NORMAL
        if (omnibus > 0.1232):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL SEGUNDO')
        return 404




