import rtiapp.constantes as Globales

#
# REVISADO CON JUANE
#

def riesgo_INFANTIL(omnibus, momento):

  

    if momento == Globales.INICIO:

        if (omnibus <= -0.317927540):
            return Globales.RIESGO

        if (omnibus > -0.317927540 and omnibus <= -0.1566956848830483): # -0.1566956849
            return Globales.BAJO

        if (omnibus > -0.1566956848830483 and omnibus <= 0.191346370):
            return Globales.NORMAL

        if (omnibus > 0.191346370):
            return Globales.OPTIMO

        print('>>> Error calculando RIESGO IPAL INFANTIL')
        return 404

    if momento == Globales.MEDIO:

        if (omnibus <= -0.2996457):
            return Globales.RIESGO
        if (omnibus > -0.2996457 and omnibus <= -0.1311223):
            return Globales.BAJO
        if (omnibus > -0.1311223 and omnibus <= 0.097948452):
            return Globales.NORMAL
        if (omnibus > 0.097948452):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL INFANTIL')
        return 404

    if momento == Globales.FIN:

        if (omnibus <= -0.2677698249):
            return Globales.RIESGO
        if (omnibus > -0.2677698249 and omnibus <= -0.07182318):
            return Globales.BAJO
        if (omnibus > -0.07182318 and omnibus <= 0.1023734856):
            return Globales.NORMAL
        if (omnibus > 0.1023734856):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL INFANTIL')
        return 404



def riesgo_PRIMERO(omnibus, momento):


    if momento == Globales.INICIO:
        if (omnibus <= -0.347999306):
            return Globales.ALTO_RIESGO
        if (omnibus > -0.347999306  and omnibus <= -0.07087435):
            return Globales.RIESGO
        if (omnibus > -0.07087435  and omnibus <= 0.097947505):
            return Globales.BAJO
        if (omnibus > 0.097947505 and omnibus <= 0.334823181):
            return Globales.NORMAL
        if (omnibus > 0.334823181):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL PRIMERO')
        return 404

    if momento == Globales.MEDIO:
        if (omnibus <= -0.333712733):
            return Globales.ALTO_RIESGO
        if (omnibus > -0.333712733 and omnibus <= -0.112608529):
            return Globales.RIESGO
        if (omnibus > -0.112608529 and omnibus <= 0.100530127):
            return Globales.BAJO
        if (omnibus > 0.100530127 and omnibus <= 0.3091813822):
            return Globales.NORMAL
        if (omnibus > 0.3091813822):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL PRIMERO')
        return 404

    if momento == Globales.FIN:
        if (omnibus <= -0.198908681):
            return Globales.ALTO_RIESGO
        if (omnibus > -0.198908681 and omnibus <= 0.018302796):
            return Globales.RIESGO
        if (omnibus > 0.018302796 and omnibus <= 0.2311316100):
            return Globales.BAJO
        if (omnibus > 0.2311316100 and omnibus <= 0.3431618169):
            return Globales.NORMAL
        if (omnibus > 0.3431618169):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL PRIMERO')
        return 404


def riesgo_SEGUNDO(omnibus, momento):


    if momento == Globales.INICIO:
        if (omnibus <= -0.530380796):
            return Globales.RIESGO
        if (omnibus > -0.530380796 and omnibus <= -0.20261015):
            return Globales.BAJO
        if (omnibus > -0.20261015 and omnibus <= 0.109327853):
            return Globales.NORMAL
        if (omnibus > 0.109327853):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL SEGUNDO')
        return 404

    if momento == Globales.MEDIO:
        if (omnibus <= -0.426241615):
            return Globales.RIESGO
        if (omnibus > -0.426241615 and omnibus <= -0.233464275):
            return Globales.BAJO
        if (omnibus > -0.233464275 and omnibus <= 0.177905594):
            return Globales.NORMAL
        if (omnibus > 0.177905594):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL SEGUNDO')
        return 404

    if momento == Globales.FIN:
        if (omnibus <= -0.448651826):
            return Globales.RIESGO
        if (omnibus > -0.448651826 and omnibus <= -0.0688233010):
            return Globales.BAJO
        if (omnibus > -0.0688233010 and omnibus <= 0.2359250521):
            return Globales.NORMAL
        if (omnibus > 0.2359250521):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL SEGUNDO')
        return 404



def riesgo_TERCERO(omnibus, momento):


    if momento == Globales.INICIO:
        if (omnibus <= -0.651197192):
            return Globales.RIESGO
        if (omnibus > -0.651197192 and omnibus <= -0.302387656):
            return Globales.BAJO
        if (omnibus > -0.302387656 and omnibus <= 0.056823835):
            return Globales.NORMAL
        if (omnibus > 0.056823835):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL SEGUNDO')
        return 404

    if momento == Globales.MEDIO:
        if (omnibus <= -0.794233912):
            return Globales.RIESGO
        if (omnibus > -0.794233912 and omnibus <= -0.264449392):
            return Globales.BAJO
        if (omnibus > -0.264449392 and omnibus <= 0.041385219):
            return Globales.NORMAL
        if (omnibus > 0.041385219):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL SEGUNDO')
        return 404

    if momento == Globales.FIN:
        if (omnibus <= -0.682065767):
            return Globales.RIESGO
        if (omnibus > -0.682065767 and omnibus <= -0.243051133):
            return Globales.BAJO
        if (omnibus > -0.243051133 and omnibus <= 0.115224294):
            return Globales.NORMAL
        if (omnibus > 0.115224294):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL SEGUNDO')
        return 404