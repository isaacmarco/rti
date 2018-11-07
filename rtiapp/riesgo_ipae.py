import rtiapp.constantes as Globales


#
# REVISADO CON JUANE
#


def riesgo_PRIMERO(omnibus, momento):

    if momento == Globales.INICIO:

        if (omnibus <= -0.740080287):
            return Globales.ALTO_RIESGO
        # no hay nivel riesgo
        if (omnibus > -0.740080287  and omnibus <= 0.862731281):
            return Globales.BAJO
        if (omnibus > 0.862731281  and omnibus <= 1.74861109):
            return Globales.NORMAL
        if (omnibus > 1.74861109):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAE PRIMERO')
        return 404

    if momento == Globales.MEDIO:

        if (omnibus <= -0.228144238):
            return Globales.ALTO_RIESGO
        if (omnibus > -0.228144238   and omnibus <= -0.22656331):
            return Globales.RIESGO
        if (omnibus > -0.22656331  and omnibus <= 1.262659227):
            return Globales.BAJO
        if (omnibus > 1.262659227 and omnibus <= 1.770315515):
            return Globales.NORMAL
        if (omnibus > 1.770315515):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAE PRIMERO')
        return 404

    if momento == Globales.FIN:

        if (omnibus <= -0.314248128):
            return Globales.ALTO_RIESGO
        if (omnibus > -0.314248128 and omnibus <= 0.210416406):
            return Globales.RIESGO
        if (omnibus > 0.210416406 and omnibus <= 2.120545545):
            return Globales.BAJO
        # NO HAY RENDIMIENTO 'NORMAL'
        if (omnibus > 2.120545545):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAE PRIMERO')
        return 404




def riesgo_SEGUNDO(omnibus, momento):

    if momento == Globales.INICIO:

        if (omnibus <= -1.532965198):
            return Globales.RIESGO
        if (omnibus > -1.532965198  and omnibus <= -0.6034989):
            return Globales.BAJO
        if (omnibus > -0.6034989 and omnibus <= 0.978968326):
            return Globales.NORMAL
        if (omnibus > 0.978968326):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAE PRIMERO')
        return 404

    if momento == Globales.MEDIO:

        if (omnibus <= -1.899277272):
            return Globales.RIESGO
        if (omnibus > -1.899277272 and omnibus <= -1.059334541):
            return Globales.BAJO
        if (omnibus > -1.059334541  and omnibus <= 0.294693554):
            return Globales.NORMAL
        if (omnibus > 0.294693554):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL PRIMERO')
        return 404

    if momento == Globales.FIN:

        if (omnibus <= -1.974925464):
            return Globales.RIESGO
        if (omnibus > -1.974925464 and omnibus <= -0.150502921):
            return Globales.BAJO
        if (omnibus > -0.150502921  and omnibus <= 1.114174218):
            return Globales.NORMAL
        if (omnibus > 1.114174218):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAE SEGUNDO')
        return 404



def riesgo_TERCERO(omnibus, momento):

    if momento == Globales.INICIO:

        if (omnibus <= -5.22799):
            return Globales.RIESGO
        if (omnibus > -5.22799  and omnibus <= -2.941368084):
            return Globales.BAJO
        if (omnibus > -2.941368084 and omnibus <= -2.5089):
            return Globales.NORMAL
        if (omnibus > -2.5089):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAE TERCERO')
        return 404

    if momento == Globales.MEDIO:

        if (omnibus <= -2.1619):
            return Globales.RIESGO
        if (omnibus > -2.1619 and omnibus <= -2.0894):
            return Globales.BAJO
        if (omnibus > -2.0894  and omnibus <= -1.4279):
            return Globales.NORMAL
        if (omnibus > -1.4279):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAE TERCERO')
        return 404

    if momento == Globales.FIN:

        if (omnibus <= -4.2210):
            return Globales.RIESGO
        if (omnibus > -4.2210 and omnibus <= -3.2738):
            return Globales.BAJO
        if (omnibus > -3.2738 and omnibus <= -1.3799):
            return Globales.NORMAL
        if (omnibus > -1.3799):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAE TERCERO')
        return 404


