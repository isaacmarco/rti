import rtiapp.constantes as Globales


#
# REVISADO POR MI DURANTE EL DESARROLLO
#


def riesgo_PRIMERO(omnibus, momento):

    if momento == Globales.INICIO:

        if (omnibus <= -2.073502827):
            return Globales.ALTO_RIESGO

        # NO HAY NIVEL 'RIESGO' EN IPAE PRIMERO
        #if (omnibus > -0.551320298 and omnibus < -0.029852734):
        #    return Globales.RIESGO

        if (omnibus > -2.073502826  and omnibus < 0.862731281):
            return Globales.BAJO
        if (omnibus > 0.862731282  and omnibus < 1.74861109):
            return Globales.NORMAL
        if (omnibus > 1.74861109):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAE PRIMERO')
        return 404

    if momento == Globales.MEDIO:

        if (omnibus <= -0.228144238):
            return Globales.ALTO_RIESGO
        if (omnibus > -0.22814422   and omnibus < -0.22656331):
            return Globales.RIESGO
        if (omnibus > -0.22656330  and omnibus < 1.262659227):
            return Globales.BAJO
        if (omnibus > 1.262659228 and omnibus < 1.770315515):
            return Globales.NORMAL
        if (omnibus > 1.770315515):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAE PRIMERO')
        return 404

    if momento == Globales.FIN:

        if (omnibus <= -0.314248128):
            return Globales.ALTO_RIESGO
        if (omnibus > -0.314248127 and omnibus < 0.210416406):
            return Globales.RIESGO
        if (omnibus > 0.210416407 and omnibus < 2.120545545):
            return Globales.BAJO

        # NO HAY RENDIMIENTO 'NORMAL'
        #if (omnibus > 0.040984994 and omnibus < 0.207333494):
        #    return Globales.NORMAL

        if (omnibus > 2.120545545):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAE PRIMERO')
        return 404




def riesgo_SEGUNDO(omnibus, momento):

    print('>>> #########################DATOS DE PRUEBA')

    if momento == Globales.INICIO:

        if (omnibus <= -1.532965198):
            return Globales.RIESGO
        if (omnibus > -1.532965197  and omnibus < -0.6034989):
            return Globales.BAJO
        if (omnibus > -0.6034987 and omnibus < 0.978968326):
            return Globales.NORMAL
        if (omnibus > 0.978968326):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAE PRIMERO')
        return 404

    if momento == Globales.MEDIO:

        if (omnibus <= -1.899277272):
            return Globales.RIESGO
        if (omnibus > -1.899277271 and omnibus < -1.059334541):
            return Globales.BAJO
        if (omnibus > -1.059334540  and omnibus < 0.294693554):
            return Globales.NORMAL
        if (omnibus > 0.294693554):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL PRIMERO')
        return 404

    if momento == Globales.FIN:

        if (omnibus <= -1.974925464):
            return Globales.RIESGO
        if (omnibus > -1.974925463 and omnibus < 0.150502921):
            return Globales.BAJO
        if (omnibus > -0.150502920  and omnibus < 1.114174218):
            return Globales.NORMAL
        if (omnibus > 1.114174218):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAE SEGUNDO')
        return 404



def riesgo_TERCERO(omnibus, momento):

    if momento == Globales.INICIO:

        if (omnibus <= 3.203130137):
            return Globales.RIESGO
        if (omnibus > -3.203130136  and omnibus < -2.243914368):
            return Globales.BAJO
        if (omnibus > -2.243914367 and omnibus < -2.5089):
            return Globales.NORMAL
        if (omnibus > -2.5089):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAE TERCERO')
        return 404

    if momento == Globales.MEDIO:

        if (omnibus <= -2.1619):
            return Globales.RIESGO
        if (omnibus > -2.1618 and omnibus < -2.0894):
            return Globales.BAJO
        if (omnibus > -2.0893  and omnibus < -1.4279):
            return Globales.NORMAL
        if (omnibus > -1.4279):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAE TERCERO')
        return 404

    if momento == Globales.FIN:

        if (omnibus <= 0.12080137):
            return Globales.RIESGO
        if (omnibus > 0.12080136 and omnibus < 0.798707253):
            return Globales.BAJO

        # NO HAY RENDIMIENTO 'NORMAL'
        #if (omnibus > 0.040984994 and omnibus < 0.207333494):
        #    return Globales.NORMAL

        if (omnibus > 0.798707253):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAE TERCERO')
        return 404


