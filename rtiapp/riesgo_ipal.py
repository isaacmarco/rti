import rtiapp.constantes as Globales

#
# REVISADO POR MI DURANTE EL DESARROLLO
#

def riesgo_INFANTIL(omnibus, momento):

      if momento == Globales.INICIO:

        if (omnibus <= -0.180658475):
            return Globales.RIESGO
        if (omnibus > -0.180658474 and omnibus < -0.07171876):
            return Globales.BAJO
        if (omnibus > -0.07171875 and omnibus < 0.098911218):
            return Globales.NORMAL
        if (omnibus > 0.098911218):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL INFANTIL')
        return 404


      if momento == Globales.MEDIO:

        if (omnibus <= -0.384165007):
            return Globales.RIESGO
        if (omnibus > -0.384165006 and omnibus < -0.043928001):
            return Globales.BAJO
        if (omnibus > -0.043928000 and omnibus < 0.168002466):
            return Globales.NORMAL
        if (omnibus > 0.168002466):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL INFANTIL')
        return 404

      if momento == Globales.FIN:

        if (omnibus <= -0.329980387):
            return Globales.RIESGO
        if (omnibus > -0.329980387 and omnibus < -0.00458066):
            return Globales.BAJO
        if (omnibus > 0.00458065 and omnibus < 0.131335391):
            return Globales.NORMAL
        if (omnibus > 0.131335391):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL INFANTIL')
        return 404



def riesgo_PRIMERO(omnibus, momento):

    if momento == Globales.INICIO:

        if (omnibus <= -0.551320299):
            return Globales.RIESGO
        if (omnibus > -0.551320298 and omnibus < -0.029852734):
            return Globales.BAJO
        if (omnibus > -0.029852733 and omnibus < 0.303682631):
            return Globales.NORMAL
        if (omnibus > 0.303682631):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL PRIMERO')
        return 404

    if momento == Globales.MEDIO:

        if (omnibus <= -0.328134203):
            return Globales.RIESGO
        if (omnibus > -0.328134202 and omnibus < 0.017611857):
            return Globales.BAJO
        if (omnibus > 0.017611858 and omnibus < 0.183694698):
            return Globales.NORMAL
        if (omnibus > 0.183694698):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL PRIMERO')
        return 404

    if momento == Globales.FIN:

        if (omnibus <= 0.318496649):
            return Globales.RIESGO
        if (omnibus > 0.318496648 and omnibus < 0.040984993):
            return Globales.BAJO
        if (omnibus > 0.040984994 and omnibus < 0.207333494):
            return Globales.NORMAL
        if (omnibus > 0.207333494):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL PRIMERO')
        return 404




def riesgo_SEGUNDO(omnibus, momento):

    if momento == Globales.INICIO:

        if (omnibus <= -0.5108):
            return Globales.RIESGO
        if (omnibus > -0.5109 and omnibus < 0.0797):
            return Globales.BAJO
        if (omnibus > 0.0798 and omnibus <0.1095):
            return Globales.NORMAL
        if (omnibus >0.1095):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL SEGUNDO')
        return 404

    if momento == Globales.MEDIO:

        if (omnibus <=  -0.2862):
            return Globales.RIESGO
        if (omnibus > -0.2861 and omnibus < 0.1328):
            return Globales.BAJO
        if (omnibus > 0.1329 and omnibus < 0.2890):
            return Globales.NORMAL
        if (omnibus > 0.2890):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL SEGUNDO')
        return 404

    if momento == Globales.FIN:

        if (omnibus <= -0.5143):
            return Globales.RIESGO
        if (omnibus > -0.5142 and omnibus < 0.0360):
            return Globales.BAJO
        if (omnibus > 0.0360 and omnibus < 0.2180):
            return Globales.NORMAL
        if (omnibus > 0.2180):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL SEGUNDO')
        return 404




