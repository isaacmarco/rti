import rtiapp.constantes as Globales


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
        if (omnibus > -0.00458066 and omnibus <= 0.1734771618):
            return Globales.NORMAL
        if (omnibus > 0.1734771618):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL INFANTIL')
        return 404



def riesgo_PRIMERO(omnibus, momento):


    if momento == Globales.INICIO:

        if (omnibus <= -0.6492997036):
            return Globales.RIESGO
        if (omnibus > -0.6492997036 and omnibus <= -0.0520332120):
            return Globales.BAJO
        if (omnibus > -0.0520332120 and omnibus <= 0.2001745985):
            return Globales.NORMAL
        if (omnibus > 0.2001745985):
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

        if (omnibus <= -0.3426856027):
            return Globales.RIESGO
        if (omnibus > -0.3426856027 and omnibus <= 0.0206013380):
            return Globales.BAJO
        if (omnibus > 0.0206013380 and omnibus <= 0.207333494):
            return Globales.NORMAL
        if (omnibus > 0.207333494):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL PRIMERO')
        return 404




def riesgo_SEGUNDO(omnibus, momento):


    if momento == Globales.INICIO:

        if (omnibus <= -0.510825):
            return Globales.RIESGO
        if (omnibus > -0.510825 and omnibus <= -0.0708245780):
            return Globales.BAJO
        if (omnibus > -0.0708245780 and omnibus <= 0.117268):
            return Globales.NORMAL
        if (omnibus > 0.117268):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL SEGUNDO')
        return 404

    if momento == Globales.MEDIO:

        if (omnibus <= -0.3272089075):
            return Globales.RIESGO
        if (omnibus > -0.3272089075 and omnibus <= 0.028678):
            return Globales.BAJO
        if (omnibus > 0.028678 and omnibus <= 0.2376630446):
            return Globales.NORMAL
        if (omnibus > 0.2376630446):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL SEGUNDO')
        return 404

    if momento == Globales.FIN:

        if (omnibus <= -0.4237496660):
            return Globales.RIESGO
        if (omnibus > -0.4237496660 and omnibus <= -0.0807718261):
            return Globales.BAJO
        if (omnibus > -0.0807718261 and omnibus <= 0.1232562):
            return Globales.NORMAL
        if (omnibus > 0.1232562):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL SEGUNDO')
        return 404
