import rtiapp.constantes as Globales



#
# REVISADO POR MI DURANTE EL DESARROLLO
#

def subprueba_complementaria_CSL(evaluacion):
    if evaluacion.CSL_TIEMPO == 0: return 0
    return evaluacion.CSL_ACIERTOS * 60 / evaluacion.CSL_TIEMPO

def subprueba_complementaria_CLE_TEXTOS(evaluacion):
    if evaluacion.CLE_TEXTO_TIEMPO == 0: return 0
    return evaluacion.CLE_TEXTO_ACIERTOS * 60 / evaluacion.CLE_TEXTO_TIEMPO

def subprueba_complementaria_CFS(evaluacion):
    if evaluacion.CFS_TIEMPO == 0: return 0
    return evaluacion.CFS_ACIERTOS * 60 / evaluacion.CFS_TIEMPO

def subprueba_complementaria_VOC(evaluacion):
    if evaluacion.VOC_ACIERTOS == 0: return 0
    return evaluacion.VOC_ACIERTOS * 60 / evaluacion.VOC_ACIERTOS



def omnibus_INFANTIL(evaluacion, momento):

    e = evaluacion

    if momento == Globales.INICIO:
        return (
            (e.CSL - 14.194) / 12.6769 +
            (e.CNL - 9.780) / 11.7215 +
            (e.CFA - 37.7487) / 30.23278 +
            (e.ADIVINANZAS - 7.8639) / 2.80269 +
            (e.CLE_TEXTO - 3.4503) / 1.22534 +
            (e.CLE_IMAGEN - 25.7068) / 7.39544
            ) / 6

    if momento == Globales.MEDIO:
        return (
            (e.CSL - 23.51) / 17.142 +
            (e.CNL - 15.41) / 13.386 +
            (e.CFA - 47.6548) / 32.75189 +
            (e.ADIVINANZAS - 9.4873) / 2.95823 +
            (e.CLE_TEXTO - 3.4162) / 1.22447 +
            (e.CLE_IMAGEN - 29.5736) / 4.66980
            ) / 6

    if momento == Globales.FIN:
        return (
            (e.CSL - 31.673) / 21.8882 +
            (e.CNL - 19.857) / 16.0994 +
            (e.CFA - 52.4388) / 34.10348 +
            (e.ADIVINANZAS - 9.8359) / 2.85270 +
            (e.CLE_TEXTO - 3.8316) / 1.06083 +
            (e.CLE_IMAGEN - 30.8418) / 2.83214
            ) / 6

    print('>>> Error calculando OMNIBUS IPAL INFANTIL')
    return 404




def omnibus_PRIMERO(evaluacion, momento):

    e = evaluacion

    if momento == Globales.INICIO:
        return (
            (e.CSL - 28.303) / 18.7054 +
            (e.CNL - 27.451) / 15.0171 +
            (e.CFS - 20.526) / 15.5126 +
            (e.FLO - 37.783) / 21.7755 +
            (e.CLE_TEXTO - 5.2914) / 1.02312 +
            (e.LP - 15.8971) / 9.90650 +
            (e.TM - 10.7314) / 6.07916
            ) / 7

    if momento == Globales.MEDIO:
        return (
            (e.CSL - 32.32) / 17.468 +
            (e.CNL - 39.41) / 15.679 +
            (e.CFS - 24.71) / 16.682 +
            (e.FLO - 49.48) / 21.874 +
            (e.CLE_TEXTO - 4.8249) / 1.20974 +
            (e.LP - 22.8305) / 9.60851 +
            (e.TM - 11.0847) / 4.68419
            ) / 7

    if momento == Globales.FIN:
        return (
            (e.CSL - 37.523) / 18.4722 +
            (e.CNL - 43.410) / 16.8340 +
            (e.CFS - 34.240) / 18.6285 +
            (e.FLO - 58.621) / 23.0878 +
            (e.CLE_TEXTO - 4.8652) / 1.13188 +
            (e.LP - 25.1517) / 9.47101 +
            (e.TM - 15.5730) / 4.97312
            ) / 7

    print ('>>> Error calculando OMNIBUS IPAL PRIMERO')
    return 404





def omnibus_SEGUNDO(evaluacion, momento):

    e = evaluacion

    if momento == Globales.INICIO:
        return (
            (e.CNL - 49.45) / 16.25 +
            (e.LP - 26.27) / 8.67  +
            (e.TM - 5.42) / 2.62 +
            (e.FLO - 64.39) / 26.58 +
            (e.PRO - 68.32) /26.95
            )  / 5

    if momento == Globales.MEDIO:
        return (
            (e.CNL - 56.14) / 15.28 +
            (e.LP - 30.08) / 8.13  +
            (e.TM - 4.37) / 2.35 +
            (e.FLO - 71.42) / 26.02 +
            (e.PRO - 73.38) / 23.93
             ) / 5

    if momento == Globales.FIN:
        return (
            (e.CNL - 59.03) / 16.96 +
            (e.LP - 29.83) / 8.46 +
            (e.TM - 7.11) / 3.22 +
            (e.FLO - 78.02) / 28.21 +
            (e.PRO - 72.74) / 26.30
            ) / 5


    print('>>> Error calculando OMNIBUS IPAL SEGUNDO')
    return 404


def complementarias_vocabulario(evaluacion):
    e = evaluacion
    return 404

def complementarias_CLE_texto(evaluacion):
    e = evaluacion
    return 404
