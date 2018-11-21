import rtiapp.constantes as Globales


#
# REVISADO CON JUANE
#


def r(a):
    return round(a, 6)

def riesgo_PRIMERO(omnibus, momento):

    omnibus = round(omnibus, 6)
    print('>>> Omnibus truncado ' + str(omnibus))

    if momento == Globales.INICIO:

        if (omnibus <= r(-0.70730561160)):
            return Globales.ALTO_RIESGO
        if (omnibus > r(-0.70730561160) and omnibus <= r(-0.37984452327)):
            return Globales.RIESGO
        if (omnibus > r(-0.37984452327 ) and omnibus <= r(0.06867414335)):
            return Globales.BAJO
        if (omnibus > r(0.06867414335 ) and omnibus <= r(0.21691417064)):
            return Globales.NORMAL
        if (omnibus > r(0.21691417064)):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAE PRIMERO')
        return 404

    if momento == Globales.MEDIO:

        if (omnibus <= r(-0.3818744902)):
            return Globales.ALTO_RIESGO
        if (omnibus > r(-0.3818744902)   and omnibus <= r(-0.15640893632)):
            return Globales.RIESGO
        if (omnibus > r(-0.15640893632)  and omnibus <= r(0.1956489893)):
            return Globales.BAJO
        if (omnibus > r(0.1956489893) and omnibus <= r(0.4063569056)):
            return Globales.NORMAL
        if (omnibus > r(0.4063569056)):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAE PRIMERO')
        return 404

    if momento == Globales.FIN:

        if (omnibus <= r(-0.225898215)):
            return Globales.ALTO_RIESGO
        if (omnibus > r(-0.225898215) and omnibus <= r(-0.007182770)):
            return Globales.RIESGO
        if (omnibus > r(-0.007182770) and omnibus <= r(0.207542352)):
            return Globales.BAJO
        if (omnibus > r(0.207542352) and omnibus <= r(0.525522662)):
            return Globales.NORMAL
        if (omnibus > r(0.525522662)):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAE PRIMERO')
        return 404



def riesgo_SEGUNDO(omnibus, momento):

    omnibus = round(omnibus, 6)
    print('>>> Omnibus truncado ' + str(omnibus))

    if momento == Globales.INICIO:

        if (omnibus <= r(-0.302854366)):
            return Globales.RIESGO
        if (omnibus > r(-0.302854366)  and omnibus <= r(-0.080415909)):
            return Globales.BAJO
        if (omnibus > r(-0.080415909) and omnibus <= r(0.131535102)):
            return Globales.NORMAL
        if (omnibus > r(0.131535102)):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAE PRIMERO')
        return 404

    if momento == Globales.MEDIO:

        if (omnibus <= r(-0.329250256)):
            return Globales.RIESGO
        if (omnibus > r(-0.329250256) and omnibus <= r(-0.122463016)):
            return Globales.BAJO
        if (omnibus > r(-0.122463016 ) and omnibus <= r(0.055621763)):
            return Globales.NORMAL
        if (omnibus > r(0.055621763)):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL PRIMERO')
        return 404

    if momento == Globales.FIN:

        if (omnibus <= r(-0.266751501)):
            return Globales.RIESGO
        if (omnibus > r(-0.266751501) and omnibus <= r(0.036251262)):
            return Globales.BAJO
        if (omnibus > r(0.036251262 ) and omnibus <= r(0.258451001)):
            return Globales.NORMAL
        if (omnibus > r(0.258451001)):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAE SEGUNDO')
        return 404



def riesgo_TERCERO(omnibus, momento):


    omnibus = round(omnibus, 6)
    print('>>> Omnibus truncado ' + str(omnibus))

    if momento == Globales.INICIO:

        if (omnibus <= r(-0.38633645)):
            return Globales.RIESGO
        if (omnibus > r(-0.38633645)  and omnibus <= r(-0.22613658)):
            return Globales.BAJO
        if (omnibus > r(-0.22613658) and omnibus <= r(-0.10753715)):
            return Globales.NORMAL
        if (omnibus > r(-0.10753715)):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAE TERCERO')
        return 404

    if momento == Globales.MEDIO:

        if (omnibus <= r(-0.362857743)):
            return Globales.RIESGO
        if (omnibus > r(-0.362857743 )and omnibus <= r(-0.160645297)):
            return Globales.BAJO
        if (omnibus > r(-0.160645297)  and omnibus <= r(-0.065985047)):
            return Globales.NORMAL
        if (omnibus > r(-0.065985047)):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAE TERCERO')
        return 404

    if momento == Globales.FIN:

        if (omnibus <= r(-0.164233297)):
            return Globales.RIESGO
        if (omnibus > r(-0.164233297) and omnibus <= r(0.028560792)):
            return Globales.BAJO
        if (omnibus > r(0.028560792) and omnibus <= r(0.128285922)):
            return Globales.NORMAL
        if (omnibus > r(0.128285922)):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAE TERCERO')
        return 404


