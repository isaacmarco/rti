import rtiapp.constantes as Globales


#
# REVISADO CON JUANE (SEGUNDA REVISION)
#


def riesgo_PRIMERO(omnibus, momento):

    if momento == Globales.INICIO:

        if (omnibus <= -0.70730561160):
            return Globales.ALTO_RIESGO
        if (omnibus > -0.70730561160 and omnibus <= -0.37984452327):
            return Globales.RIESGO
        if (omnibus > -0.37984452327  and omnibus <= 0.06867414335):
            return Globales.BAJO
        if (omnibus > 0.06867414335  and omnibus <= 0.21691417064):
            return Globales.NORMAL
        if (omnibus > 0.21691417064):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAE PRIMERO')
        return 404

    if momento == Globales.MEDIO:

        if (omnibus <= -0.3818744902):
            return Globales.ALTO_RIESGO
        if (omnibus > -0.3818744902   and omnibus <= -0.15640893632):
            return Globales.RIESGO
        if (omnibus > -0.15640893632  and omnibus <= 0.1956489893):
            return Globales.BAJO
        if (omnibus > 0.1956489893 and omnibus <= 0.4063569056):
            return Globales.NORMAL
        if (omnibus > 0.4063569056):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAE PRIMERO')
        return 404

    if momento == Globales.FIN:

        if (omnibus <= -0.225898215):
            return Globales.ALTO_RIESGO
        if (omnibus > -0.225898215 and omnibus <= -0.053461496):
            return Globales.RIESGO
        if (omnibus > -0.053461496 and omnibus <= 0.207542352):
            return Globales.BAJO
        if (omnibus > 0.207542352 and omnibus <= 0.525522662):
            return Globales.NORMAL
        if (omnibus > 0.525522662):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAE PRIMERO')
        return 404



def riesgo_SEGUNDO(omnibus, momento):

    if momento == Globales.INICIO:

        if (omnibus <= -0.302854366):
            return Globales.RIESGO
        if (omnibus > -0.302854366  and omnibus <= -0.111144333):
            return Globales.BAJO
        if (omnibus > -0.111144333 and omnibus <= -0.007799196):
            return Globales.NORMAL
        if (omnibus > -0.007799196):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAE PRIMERO')
        return 404

    if momento == Globales.MEDIO:

        if (omnibus <= -0.329250256):
            return Globales.RIESGO
        if (omnibus > -0.329250256 and omnibus <= -0.122463016):
            return Globales.BAJO
        if (omnibus > -0.122463016  and omnibus <= 0.055621763):
            return Globales.NORMAL
        if (omnibus > 0.055621763):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL PRIMERO')
        return 404

    if momento == Globales.FIN:

        if (omnibus <= -0.266751501):
            return Globales.RIESGO
        if (omnibus > -0.266751501 and omnibus <= -0.023180658):
            return Globales.BAJO
        if (omnibus > -0.023180658  and omnibus <= 0.167508746):
            return Globales.NORMAL
        if (omnibus > 0.167508746):
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


