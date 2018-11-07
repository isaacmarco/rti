import rtiapp.constantes as Globales


#
# REVISADO CON JUANE
#

def riesgo_INFANTIL(omnibus, momento):



    if momento == Globales.INICIO:

        if (omnibus <= -0.3351722):
            return Globales.RIESGO
        if (omnibus > -0.3351722  and omnibus <= -0.1328701):
            return Globales.BAJO
        if (omnibus > -0.1328701 and omnibus <= 0.4237160):
            return Globales.NORMAL
        if (omnibus > 0.4237160):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL INFANTIL')
        return 404

    if momento == Globales.MEDIO:

        if (omnibus <= -0.2996457):
            return Globales.RIESGO
        if (omnibus > -0.2996457 and omnibus <= -0.1311223):
            return Globales.BAJO
        if (omnibus > -0.1311223 and omnibus <= 0.3529345):
            return Globales.NORMAL
        if (omnibus > 0.3529345):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL INFANTIL')
        return 404

    if momento == Globales.FIN:

        if (omnibus <= -0.2292327):
            return Globales.RIESGO
        if (omnibus > -0.2292327 and omnibus <= -0.07182318):
            return Globales.BAJO
        if (omnibus > -0.07182318 and omnibus <= 0.2602976):
            return Globales.NORMAL
        if (omnibus > 0.2602976):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL INFANTIL')
        return 404



def riesgo_PRIMERO(omnibus, momento):


    if momento == Globales.INICIO:
        if (omnibus <= -0.347999306):
            return Globales.ALTO_RIESGO
        if (omnibus > -0.347999306  and omnibus <= -0.07087435):
            return Globales.RIESGO
        if (omnibus > -0.07087435  and omnibus <= -0.019275252):
            return Globales.BAJO
        if (omnibus > -0.019275252 and omnibus <= 0.013140487):
            return Globales.NORMAL
        if (omnibus > 0.013140487):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL PRIMERO')
        return 404

    if momento == Globales.MEDIO:
        if (omnibus <= -0.342912398):
            return Globales.ALTO_RIESGO
        if (omnibus > -0.342912398 and omnibus <= -0.112608529):
            return Globales.RIESGO
        if (omnibus > -0.112608529 and omnibus <= 0.100530127):
            return Globales.BAJO
        if (omnibus > 0.100530127 and omnibus <= 0.162980798):
            return Globales.NORMAL
        if (omnibus > 0.162980798):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL PRIMERO')
        return 404

    if momento == Globales.FIN:
        if (omnibus <= -0.198908681):
            return Globales.ALTO_RIESGO
        if (omnibus > -0.198908681 and omnibus <= 0.018302796):
            return Globales.RIESGO
        if (omnibus > 0.018302796 and omnibus <= 0.114669608):
            return Globales.BAJO
        if (omnibus > 0.114669608 and omnibus <= 0.137982938):
            return Globales.NORMAL
        if (omnibus > 0.137982938):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL PRIMERO')
        return 404


def riesgo_SEGUNDO(omnibus, momento):

    if momento == Globales.INICIO:
        if (omnibus <= -0.530380796):
            return Globales.RIESGO
        if (omnibus > -0.530380796 and omnibus <= -0.20261015):
            return Globales.BAJO
        if (omnibus > -0.20261015 and omnibus <= 0.044400053):
            return Globales.NORMAL
        if (omnibus > 0.044400053):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL SEGUNDO')
        return 404

    if momento == Globales.MEDIO:
        if (omnibus <= -0.426241615):
            return Globales.RIESGO
        if (omnibus > -0.426241615 and omnibus <= -0.268322849):
            return Globales.BAJO
        if (omnibus > -0.268322849 and omnibus <= 0.052567295):
            return Globales.NORMAL
        if (omnibus > 0.052567295):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL SEGUNDO')
        return 404

    if momento == Globales.FIN:
        if (omnibus <= -0.448651826):
            return Globales.RIESGO
        if (omnibus > -0.448651826 and omnibus <= -0.120972641):
            return Globales.BAJO
        if (omnibus > -0.120972641 and omnibus <= 0.140222415):
            return Globales.NORMAL
        if (omnibus > 0.140222415):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL SEGUNDO')
        return 404



def riesgo_TERCERO(omnibus, momento):

    if momento == Globales.INICIO:
        if (omnibus <= -0.651197192):
            return Globales.RIESGO
        if (omnibus > -0.651197192 and omnibus <= -0.302387656):
            return Globales.BAJO
        if (omnibus > -0.302387656 and omnibus <= -0.032568676):
            return Globales.NORMAL
        if (omnibus > -0.032568676):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL SEGUNDO')
        return 404

    if momento == Globales.MEDIO:
        if (omnibus <= -0.794233912):
            return Globales.RIESGO
        if (omnibus > -0.794233912 and omnibus <= -0.264449392):
            return Globales.BAJO
        if (omnibus > -0.264449392 and omnibus <= -0.061627301):
            return Globales.NORMAL
        if (omnibus > -0.061627301):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL SEGUNDO')
        return 404

    if momento == Globales.FIN:
        if (omnibus <= -0.682065767):
            return Globales.RIESGO
        if (omnibus > -0.682065767 and omnibus <= -0.243051133):
            return Globales.BAJO
        if (omnibus > -0.243051133 and omnibus <= 0.005023444):
            return Globales.NORMAL
        if (omnibus > 0.005023444):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL SEGUNDO')
        return 404