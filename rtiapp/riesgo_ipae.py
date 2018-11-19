import rtiapp.constantes as Globales


#
# REVISADO CON JUANE
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
        if (omnibus > -0.225898215 and omnibus <= -0.007182770):
            return Globales.RIESGO
        if (omnibus > -0.007182770 and omnibus <= 0.207542352):
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
        if (omnibus > -0.302854366  and omnibus <= -0.080415909):
            return Globales.BAJO
        if (omnibus > -0.080415909 and omnibus <= 0.131535102):
            return Globales.NORMAL
        if (omnibus > 0.131535102):
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
        if (omnibus > -0.266751501 and omnibus <= 0.036251262):
            return Globales.BAJO
        if (omnibus > 0.036251262  and omnibus <= 0.258451001):
            return Globales.NORMAL
        if (omnibus > 0.258451001):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAE SEGUNDO')
        return 404



def riesgo_TERCERO(omnibus, momento):

    if momento == Globales.INICIO:

        if (omnibus <= -0.38633645):
            return Globales.RIESGO
        if (omnibus > -0.38633645  and omnibus <= -0.22613658):
            return Globales.BAJO
        if (omnibus > -0.22613658 and omnibus <= -0.10753715):
            return Globales.NORMAL
        if (omnibus > -0.10753715):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAE TERCERO')
        return 404

    if momento == Globales.MEDIO:

        if (omnibus <= -0.362857743):
            return Globales.RIESGO
        if (omnibus > -0.362857743 and omnibus <= -0.160645297):
            return Globales.BAJO
        if (omnibus > -0.160645297  and omnibus <= -0.065985047):
            return Globales.NORMAL
        if (omnibus > -0.065985047):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAE TERCERO')
        return 404

    if momento == Globales.FIN:

        if (omnibus <= -0.164233297):
            return Globales.RIESGO
        if (omnibus > -0.164233297 and omnibus <= 0.028560792):
            return Globales.BAJO
        if (omnibus > 0.028560792 and omnibus <= 0.128285922):
            return Globales.NORMAL
        if (omnibus > 0.128285922):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAE TERCERO')
        return 404


