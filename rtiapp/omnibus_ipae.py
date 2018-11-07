import rtiapp.constantes as Globales


#
#   REVISADO POR JUANE
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


    print ('>>> Error calculando OMNIBUS IPE PRIMERO')
    return 404





def omnibus_SEGUNDO(evaluacion, momento):

    e = evaluacion

    if momento == Globales.INICIO:
        return (
            (e.TLC_1 - 1.451) / 1.8309 +
            (e.DICTADO_ORTOGRAFIA_ARBITRARIA - 10.694) / 3.3552  +
            (e.DICTADO_ORTOGRAFIA_REGLADA - 13.279) / 5.3998 +
            (e.DICTADO_PSEUDOPALABRAS - 13.783) / 4.2499  +
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

    print('>>> Error calculando OMNIBUS IPE SEGUNDO')
    return 404




def omnibus_TERCERO(evaluacion, momento):

    e = evaluacion

    if momento == Globales.INICIO:
        return (
            (e.DICTADO_ORTOGRAFIA_ARBITRARIA - 14.316) / 2.8776 +
            (e.DICTADO_ORTOGRAFIA_REGLADA - 15.458) / 3.1245  +
            (e.DICTADO_FRASES - 15.524) / 3.8263 +
            (e.SEC_5 - 26.466) / 12.1264  +
            (e.SEC_SEI_5 - 25.817) / 11.7282 +
            (e.PDC_5 - 27.7784) / 12.07706
        ) / 6

    if momento == Globales.MEDIO:
        return (
            (e.DICTADO_ORTOGRAFIA_ARBITRARIA - 14.787) / 2.8690 +
            (e.DICTADO_ORTOGRAFIA_REGLADA - 15.314) / 2.5691 +
            (e.DICTADO_FRASES - 17.766) / 2.4069  +
            (e.SEC_5 - 35.036) / 12.4947 +
            (e.SEC_SEI_5 - 34.421) / 12.5947 +
            (e.PDC_5 - 36.3145) / 12.59790
             ) / 6

    if momento == Globales.FIN:
        return (
            (e.DICTADO_ORTOGRAFIA_ARBITRARIA - 14.374) / 3.2913 +
            (e.DICTADO_ORTOGRAFIA_REGLADA - 16.381) / 2.5971  +
            (e.DICTADO_FRASES - 17.376) / 2.5422  +
            (e.SEC_5 - 35.454) / 14.7490 +
            (e.SEC_SEI_5 - 34.840) / 14.5321 +
            (e.PDC_5 - 36.9828) / 14.73706
            ) / 6

    print('>>> Error calculando OMNIBUS IPE TERCERO')
    return 404