def omnibus():
    return -1


def calculo_omnibus(evaluacion):

    if momento_evaluacion is INICIO:
        print('inicio')
        return ((self.CSL - 14.194) / 12.6769 + (self.CNL - 9.780) / 11.7215 + (self.CFA - 37.7487) / 30.23278
                + (self.ADIVINANZAS - 7.8639) / 2.80269 + (self.CLE_TEXTO - 3.4503) / 1.22534
                + (self.CLE_IMAGEN - 25.7068) / 7.39544) / 6

    if momento_evaluacion is MEDIO:
        print('medio')
        return ((self.CSL - 23.51) / 17.142 + (self.CNL - 15.41) / 13.386 + (self.CFA - 47.6548) / 32.75189
                + (self.ADIVINANZAS - 9.4873) / 2.95823 + (self.CLE_TEXTO - 3.4162) / 1.22447
                + (self.CLE_IMAGEN - 29.5736) / 4.66980) / 6

    if momento_evaluacion is FIN:
        print('final')
        return ((self.CSL - 31.673) / 21.8882 + (self.CNL - 19.857) / 16.0994
                + (self.CFA - 52.4388) / 34.10348 + (self.ADIVINANZAS - 9.8359) / 2.85270
                + (self.CLE_TEXTO - 3.8316) / 1.06083 + (self.CLE_IMAGEN - 30.8418) / 2.83214) / 6