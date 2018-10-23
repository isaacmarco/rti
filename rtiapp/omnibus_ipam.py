import rtiapp.constantes as Globales



#
# REVISADO POR MI DURANTE EL DESARROLLO
#



def omnibus_INFANTIL(evaluacion, momento):
    e = evaluacion

    if momento == Globales.INICIO:
        return (
            (e.CN - 18.257) / 8.1132 +
            (e.EC - 11.786) / 3.9993 +
            (e.SN - 5.775) / 3.4122 +
            (e.IN - 19.104) / 12.2411 +
            (e.CVA - 26.990) / 14.3512
        ) / 5

    if momento == Globales.MEDIO:
        return (
            (e.CN - 21.597) / 8.9222 +
            (e.EC - 12.446) / 3.6615 +
            (e.SN - 7.040) / 3.8771 +
            (e.IN - 24.921) / 14.0033 +
            (e.CVA - 33.310) / 16.8600
        ) / 5

    if momento == Globales.FIN:
        return (
            (e.CN - 25.749) / 8.8139 +
            (e.EC - 14.109) / 3.7819 +
            (e.SN - 8.845) / 3.8117 +
            (e.IN - 30.531) / 15.2430 +
            (e.CVA - 41.409) / 19.6327
         ) / 5

    print('>>> Error calculando OMNIBUS IPAM INFANTIL')

    return 404


def omnibus_PRIMERO(evaluacion, momento):

    e = evaluacion

    if momento == Globales.INICIO:
        return (
            (e.CN - 23.8869) / 9.75228 +
            (e.ODD - 2.4109) / 2.42259 +
            (e.SN - 8.3473) / 4.31155 +
            (e.OUD - 7.3273) / 3.65287 +
            (e.VP - 2.7515) / 2.74841
            ) / 5

    if momento == Globales.MEDIO:
        return (
            (e.CN - 31.0473) / 10.96195 +
            (e.ODD - 4.4099) / 3.07098 +
            (e.SN - 10.4417) / 4.79081 +
            (e.OUD - 9.8225) / 4.75261 +
            (e.VP - 3.6506) / 3.52801
            ) / 5

    if momento == Globales.FIN:
        return (
            (e.CN - 36.1221) / 9.41519 +
            (e.ODD - 7.4294) / 3.49442 +
            (e.SN - 12.8284) / 5.53238 +
            (e.OUD - 11.5848) / 5.16067 +
            (e.VP - 7.2035) / 4.87857
            ) / 5

    print ('>>> Error calculando OMNIBUS IPAM PRIMERO')
    return 404




def omnibus_SEGUNDO(evaluacion, momento):

    e = evaluacion

    if momento == Globales.INICIO:
        return (
            (e.CN - 33.9502) / 11.07952 +
            (e.ODD - 8.1587) / 3.39888 +
            (e.SN - 2.8208) / 3.50300 +
            (e.OUD - 7.3992) / 4.01741 +
            (e.VP - 3.8167) / 2.65281
            ) / 5

    if momento == Globales.MEDIO:
        return (
            (e.CN - 40.4008) / 11.66666 +
            (e.ODD - 8.4980) / 3.06704 +
            (e.SN - 6.0947) / 4.64830 +
            (e.OUD - 10.5458) / 4.71510 +
            (e.VP - 4.6270) / 2.70274
            ) / 5

    if momento == Globales.FIN:
        return (
            (e.CN - 42.6307) / 11.51668 +
            (e.ODD - 9.3602) / 3.22120 +
            (e.SN - 7.9342) / 5.03119 +
            (e.OUD - 13.4678) / 6.50531 +
            (e.VP - 10.1958) / 5.55829
            ) / 5

    print('>>> Error calculando OMNIBUS IPAM SEGUNDO')
    return 404




def omnibus_TERCERO(evaluacion, momento):

    e = evaluacion

    if momento == Globales.INICIO:
        return (
            (e.CN - 39.3524) / 9.98357 +
            (e.ODD - 5.5177) / 2.75716 +
            (e.SN - 8.5882) / 5.64862 +
            (e.OUD - 13.5221) / 6.16672 +
            (e.VP - 6.8899) / 3.36184
        ) / 5

    if momento == Globales.MEDIO:
        return (
            (e.CN - 47.2889) / 10.53061 +
            (e.ODD - 7.4133) / 3.22972 +
            (e.SN - 10.6205) / 5.93868 +
            (e.OUD - 15.7578) / 7.73809 +
            (e.VP - 7.2611) / 4.05166
            ) / 5

    if momento == Globales.FIN:
        return (
            (e.CN - 52.3084) / 9.55154 +
            (e.ODD - 7.2655) / 3.99559 +
            (e.SN - 12.1858) / 6.26319 +
            (e.OUD - 21.0529) / 8.57486 +
            (e.VP - 9.9736) / 6.13341
            ) / 5

    print('>>> Error calculando OMNIBUS IPAM TERCERO')
    return 404