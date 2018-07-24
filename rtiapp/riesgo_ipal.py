import rtiapp.constantes as Globales

#
# REVISADO POR MI DURANTE EL DESARROLLO
#


# riesgos por puntuaciones directas de cada tarea
# los parametros son siglas de la tarea, momento: inicio
# medio, fin, y la puntuacion directa en la tarea pd
'''
def riesgo_todas_las_tareas_INFANTIL(evaluacion):
    # diccionario con los riesgos de cada tarea
    riesgos = {}

    riesgos['CFA-INICIO'] = riesgo_TAREA_INFANTIL('CFA', Globales.INICIO, evaluacion.CFA)
    riesgos['CFA-MEDIO'] = riesgo_TAREA_INFANTIL('CFA', Globales.INICIO, evaluacion.CFA)
    riesgos['CFA-FIN'] = riesgo_TAREA_INFANTIL('CFA', Globales.INICIO, evaluacion.CFA)

    return riesgos

def riesgo_TAREA_INFANTIL(tarea, momento, pd):

    if tarea == 'CFA':

        if momento == Globales.INICIO:
            if pd <= 17: return Globales.RIESGO
            if pd >= 18 and pd <= 38:  return Globales.BAJO
            if pd >= 39 and pd <= 46:  return Globales.NORMAL
            if pd > 46: return Globales.OPTIMO

        if momento == Globales.MEDIO:
           print('>>> No se pasa la tarea CFA')

        if momento == Globales.FIN:
            if pd <= 22:  return Globales.RIESGO
            if pd >= 23 and pd <= 70: return Globales.BAJO
            if pd >= 71 and pd <= 75: return Globales.NORMAL
            if pd > 75: return Globales.OPTIMO


    if tarea == 'ADIVINANZAS':

        if momento == Globales.INICIO:
            if pd <= 8: return Globales.RIESGO
            if pd == 9: return Globales.BAJO
            if pd > 9: return Globales.OPTIMO

        if momento == Globales.MEDIO:
            if pd <= 9: return Globales.RIESGO
            if pd == 10: return Globales.BAJO
            if pd == 11: return Globales.NORMAL
            if pd > 11: return Globales.OPTIMO

        if momento == Globales.FIN:
            if pd <= 9: return Globales.RIESGO
            if pd == 10: return Globales.BAJO
            if pd == 11: return Globales.NORMAL
            if pd > 11: return Globales.OPTIMO

    if tarea == 'CSL':

        if momento == Globales.INICIO:
            if pd <= 5: return Globales.RIESGO
            if pd >= 6 and pd <= 8: return Globales.BAJO
            if pd >= 9 and pd <= 14: return Globales.NORMAL
            if pd > 14: return Globales.OPTIMO

        if momento == Globales.MEDIO:
            if pd <= 10: return Globales.RIESGO
            if pd >= 11 and pd <= 16: return Globales.BAJO
            if pd >= 17 and pd <= 29: return Globales.NORMAL
            if pd > 29: return Globales.OPTIMO

        if momento == Globales.FIN:
            if pd <= 15: return Globales.RIESGO
            if pd >= 16 and pd <= 25: return Globales.BAJO
            if pd >= 26 and pd <= 37: return Globales.NORMAL
            if pd > 37: return Globales.OPTIMO

    if tarea == 'CNL':

        if momento == Globales.INICIO:
            if pd <= 6: return Globales.RIESGO
            if pd >= 7 and pd <= 8: return Globales.BAJO
            if pd > 8: return Globales.OPTIMO

        if momento == Globales.MEDIO:
            if pd <= 12: return Globales.RIESGO
            if pd >= 13 and pd <= 14: return Globales.BAJO
            if pd > 14: return Globales.OPTIMO

        if momento == Globales.FIN:
            if pd <= 18: return Globales.RIESGO
            if pd >= 19 and pd <= 21: return Globales.BAJO
            if pd == 22: return Globales.NORMAL
            if pd > 22: return Globales.OPTIMO

    if tarea == 'CLE_IMAGEN':

        if momento == Globales.INICIO:
            if pd <= 28: return Globales.RIESGO
            if pd >= 29 and pd <= 31: return Globales.BAJO
            if pd > 31: return Globales.OPTIMO

        if momento == Globales.MEDIO:
            if pd <= 29: return Globales.RIESGO
            if pd >= 30 and pd <= 31: return Globales.BAJO
            if pd > 31: return Globales.OPTIMO

        if momento == Globales.FIN:
            if pd <= 30: return Globales.RIESGO
            if pd == 31: return Globales.BAJO
            if pd > 31: return Globales.OPTIMO

    if tarea == 'CLE_TEXTO':

        if momento == Globales.INICIO:
            if pd <= 2: return Globales.RIESGO
            if pd == 3: return Globales.BAJO
            if pd > 3: return Globales.OPTIMO

        if momento == Globales.MEDIO:
            if pd <= 3: return Globales.RIESGO
            if pd == 4: return Globales.BAJO
            if pd > 4: return Globales.OPTIMO

        if momento == Globales.FIN:
            if pd <= 3: return Globales.RIESGO
            if pd == 4: return Globales.BAJO
            if pd > 4: return Globales.OPTIMO

'''

# riesgo por omnibus

def riesgo_INFANTIL(omnibus, momento):

      if momento == Globales.INICIO:

        if (omnibus <= -0.180658475):
            return Globales.RIESGO
        if (omnibus > -0.180658474 and omnibus < -0.07171876):
            return Globales.BAJO
        if (omnibus > -0.07171875 and omnibus < 0.098911218):
            return Globales.NORMAL
        if (omnibus > 0.098911218):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL INFANTIL')
        return 404


      if momento == Globales.MEDIO:

        if (omnibus <= -0.384165007):
            return Globales.RIESGO
        if (omnibus > -0.384165006 and omnibus < -0.043928001):
            return Globales.BAJO
        if (omnibus > -0.043928000 and omnibus < 0.168002466):
            return Globales.NORMAL
        if (omnibus > 0.168002466):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL INFANTIL')
        return 404

      if momento == Globales.FIN:

        if (omnibus <= -0.329980387):
            return Globales.RIESGO
        if (omnibus > -0.329980387 and omnibus < -0.00458066):
            return Globales.BAJO
        if (omnibus > 0.00458065 and omnibus < 0.131335391):
            return Globales.NORMAL
        if (omnibus > 0.131335391):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL INFANTIL')
        return 404



def riesgo_PRIMERO(omnibus, momento):

    if momento == Globales.INICIO:

        if (omnibus <= -0.551320299):
            return Globales.RIESGO
        if (omnibus > -0.551320298 and omnibus < -0.029852734):
            return Globales.BAJO
        if (omnibus > -0.029852733 and omnibus < 0.303682631):
            return Globales.NORMAL
        if (omnibus > 0.303682631):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL PRIMERO')
        return 404

    if momento == Globales.MEDIO:

        if (omnibus <= -0.328134203):
            return Globales.RIESGO
        if (omnibus > -0.328134202 and omnibus < 0.017611857):
            return Globales.BAJO
        if (omnibus > 0.017611858 and omnibus < 0.183694698):
            return Globales.NORMAL
        if (omnibus > 0.183694698):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL PRIMERO')
        return 404

    if momento == Globales.FIN:

        if (omnibus <= 0.318496649):
            return Globales.RIESGO
        if (omnibus > 0.318496648 and omnibus < 0.040984993):
            return Globales.BAJO
        if (omnibus > 0.040984994 and omnibus < 0.207333494):
            return Globales.NORMAL
        if (omnibus > 0.207333494):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL PRIMERO')
        return 404




def riesgo_SEGUNDO(omnibus, momento):

    if momento == Globales.INICIO:

        if (omnibus <= -0.5108):
            return Globales.RIESGO
        if (omnibus > -0.5109 and omnibus < 0.0797):
            return Globales.BAJO
        if (omnibus > 0.0798 and omnibus <0.1095):
            return Globales.NORMAL
        if (omnibus >0.1095):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL SEGUNDO')
        return 404

    if momento == Globales.MEDIO:

        if (omnibus <=  -0.2862):
            return Globales.RIESGO
        if (omnibus > -0.2861 and omnibus < 0.1328):
            return Globales.BAJO
        if (omnibus > 0.1329 and omnibus < 0.2890):
            return Globales.NORMAL
        if (omnibus > 0.2890):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL SEGUNDO')
        return 404

    if momento == Globales.FIN:

        if (omnibus <= -0.5143):
            return Globales.RIESGO
        if (omnibus > -0.5142 and omnibus < 0.0360):
            return Globales.BAJO
        if (omnibus > 0.0360 and omnibus < 0.2180):
            return Globales.NORMAL
        if (omnibus > 0.2180):
            return Globales.OPTIMO
        print('>>> Error calculando RIESGO IPAL SEGUNDO')
        return 404




