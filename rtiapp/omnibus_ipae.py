import rtiapp.constantes as Globales


#
# REVISADO POR MI DURANTE EL DESARROLLO
#



def omnibus_PRIMERO(evaluacion, momento):

    e = evaluacion

    if momento == Globales.INICIO:
        return (
            (e.TLC_1 - 0.815) / 1.1135 +
            (e.DICTADO_ORTOGRAFIA_ARBITRARIA - 4.641) / 3.7134  +
            (e.DICTADO_ORTOGRAFIA_REGLADA - 5.015) / 5.2683 +
            (e.DICTADO_PSEUDOPALABRAS - 4.852) / 5.4534  +
            (e.DICTADO_FRASES - 4.874) / 5.4741
        ) / 5

    if momento == Globales.MEDIO:
        return (
            (e.TLC_1 - 2.268) / 2.4248 +
            (e.DICTADO_ORTOGRAFIA_ARBITRARIA - 9.308) / 4.1340 +
            (e.DICTADO_ORTOGRAFIA_REGLADA - 9.718) / 6.4661 +
            (e.DICTADO_PSEUDOPALABRAS - 11.150) / 6.1784 +
            (e.DICTADO_FRASES - 11.291) / 5.8328
             ) / 5

    if momento == Globales.FIN:
        return (
            (e.TLC_1 - 4.408) / 3.5700 +
            (e.DICTADO_ORTOGRAFIA_ARBITRARIA - 10.808) / 3.9568 +
            (e.DICTADO_ORTOGRAFIA_REGLADA - 12.899) / 6.3080 +
            (e.DICTADO_PSEUDOPALABRAS - 12.153) / 5.6186 +
            (e.DICTADO_FRASES - 12.690) / 5.9283
            ) / 5


    print ('>>> Error calculando OMNIBUS IPAM PRIMERO')
    return 404





def omnibus_SEGUNDO(evaluacion, momento):

    e = evaluacion

    if momento == Globales.INICIO:
        return (
            (e.TLC_1 - 1.451) / 1.8309 +
            (e.DICTADO_ORTOGRAFIA_ARBITRARIA - 10.694) / 3.3552  +
            (e.DICTADO_ORTOGRAFIA_REGLADA - 13.279) / 5.3998 +
            (e.DICTADO_PSEUDOPALABRAS - 13.789) / 4.2499  +
            (e.DICTADO_FRASES - 13.389) / 5.0228
        ) / 5

    if momento == Globales.MEDIO:
        return (
            (e.TLC_1 - 2.995) / 2.9214 +
            (e.DICTADO_ORTOGRAFIA_ARBITRARIA - 13.296) / 3.0081 +
            (e.DICTADO_ORTOGRAFIA_REGLADA - 16.128) / 4.2638  +
            (e.DICTADO_PSEUDOPALABRAS - 16.648) / 2.9593 +
            (e.DICTADO_FRASES - 16.507) / 2.8375
             ) / 5

    if momento == Globales.FIN:
        return (
            (e.TLC_1 - 4.861) / 3.8717 +
            (e.DICTADO_ORTOGRAFIA_ARBITRARIA - 13.986) / 3.0447  +
            (e.DICTADO_ORTOGRAFIA_REGLADA - 17.163) / 3.6159  +
            (e.DICTADO_PSEUDOPALABRAS - 15.757) / 3.1296 +
            (e.DICTADO_FRASES - 16.938) / 3.0914
            ) / 5

    print('>>> Error calculando OMNIBUS IPAM SEGUNDO')
    return 404




def omnibus_TERCERO(evaluacion, momento):

    e = evaluacion

    if momento == Globales.INICIO:
        return (
            (e.DICTADO_ORTOGRAFIA_ARBITRARIA - 1.451) / 1.8309 +
            (e.DICTADO_ORTOGRAFIA_REGLADA - 10.694) / 3.3552  +
            (e.DICTADO_FRASES - 13.279) / 5.3998 +
            (e.SEC_5 - 13.789) / 4.2499  +
            (e.SEC_SEI_5 - 13.789) / 4.2499 +
            (e.PDC_5 - 13.389) / 5.0228
        ) / 6

    if momento == Globales.MEDIO:
        return (
            (e.DICTADO_ORTOGRAFIA_ARBITRARIA - 2.995) / 2.9214 +
            (e.DICTADO_ORTOGRAFIA_REGLADA - 13.296) / 3.0081 +
            (e.DICTADO_FRASES - 16.128) / 4.2638  +
            (e.SEC_5 - 16.648) / 2.9593 +
            (e.SEC_SEI_5 - 13.789) / 4.2499 +
            (e.PDC_5 - 16.507) / 2.8375
             ) / 6

    if momento == Globales.FIN:
        return (
            (e.DICTADO_ORTOGRAFIA_ARBITRARIA - 4.861) / 3.8717 +
            (e.DICTADO_ORTOGRAFIA_REGLADA - 13.986) / 3.0447  +
            (e.DICTADO_FRASES - 17.163) / 3.6159  +
            (e.SEC_5 - 15.757) / 3.1296 +
            (e.SEC_SEI_5 - 13.789) / 4.2499 +
            (e.PDC_5 - 16.938) / 3.0914
            ) / 6

    print('>>> Error calculando OMNIBUS IPAE TERCERO')
    return 404