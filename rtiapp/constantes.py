
# tipo de prueba
IPAL = 'IPAL'
IPAM = 'IPAM'
IPAE = 'IPAE'

# niveles de riesgo
ALTO_RIESGO = 'ALTR'
RIESGO = 'RIES'
BAJO = 'BAJO'
NORMAL = 'NORM'
OPTIMO = 'OPTI'
SIN_EVALUAR = 'NOEV'
# fechas
NOVIEMBRE = 1
DICIEMBRE = 2
ENERO = 3
FEBRERO = 4
MARZO = 5
ABRIL = 6
MAYO = 7
# evaluaciones
CRIBADO = 'CR'
PROGRESO = 'PR'
# momento de evaluacion
INICIO = 'INICIO'
MEDIO = 'MEDIO'
FIN = 'FIN'
# paises
ESP = 'ESP'
ECU = 'ECU'
GTM = 'GTM'
CAN = 'CAN'
# constantes personales
HOMBRE = 'HM'
MUJER = 'MJ'
# nivel de estudios
DIPLOMATURA = 'DP'
LICENCIATURA = 'LC'
GRADO = 'GR'
MASTER = 'MT'
DOCTORADO = 'DC'
# profesiones
ORIENTADOR = 'OR'
PSICOLOGO = 'PS'
PEDAGOGO = 'PG'
PSICOPEDAGOGO = 'SG'
MAESTRO = 'MS'
# zona de trabajo
PERIFERIA = 'PR'
URBANA = 'UB'
RURAL = 'RU'
# cursos
INFANTIL = 'INFANTIL'
PRIMERO = 'PRIMERO'
SEGUNDO = 'SEGUNDO'
TERCERO = 'TERCERO'
# opciones de riesgo
RIESGO_OPCIONES = (
    (SIN_EVALUAR, 'Sin evaluar'),
    (RIESGO, 'Riesgo'),
    (BAJO, 'Rendimiento bajo'),
    (NORMAL, 'Rendimiento normal'),
    (OPTIMO, 'Rendimiento optimo')
)
# opciones de evaluaciones
MOMENTOS_OPCIONES = (
    (INICIO, 'Inicio'),
    (MEDIO, 'Medio'),
    (FIN, 'FIn')
)
# opciones de fecha
FECHA_OPCIONES = (
    (NOVIEMBRE, 'Noviembre'),
    (DICIEMBRE, 'Diciembre'),
    (ENERO, 'Enero'),
    (FEBRERO, 'Febrero'),
    (MARZO, 'Marzo'),
    (ABRIL, 'Abril'),
    (MAYO, 'Mayo')
)
# opciones de curso
CURSO_OPCIONES = (
    (INFANTIL, 'Infantil'),
    (PRIMERO, 'Primero'),
    (SEGUNDO, 'Segundo'),
    (TERCERO, 'Tercero')
)
# opciones de pais
PAIS_OPCIONES = (
    (ESP, 'España'),
    (GTM, 'Guatemala'),
    (ECU, 'Ecuador'),
    (CAN, 'Canarias')
)
# opciones de evaluacion
EVALUACION_OPCIONES = (
    (CRIBADO, 'Cribado'),
    (PROGRESO, 'Progreso')
)
# opciones de sexo
SEXO_OPCIONES = (
    (HOMBRE, 'Hombre'),
    (MUJER, 'Mujer')
)
# opciones de zona
ZONA_OPCIONES = (
    (PERIFERIA, 'Periferia'),
    (URBANA, 'Urbana'),
    (RURAL, 'Rural')
)
# opciones de nivel academico
NIVEL_ACADEMICO_OPCIONES = (
    (DIPLOMATURA, 'Diplomatura'),
    (LICENCIATURA, 'Licenciatura'),
    (GRADO, 'Grado'),
    (MASTER, 'Master'),
    (DOCTORADO, 'Doctorado')
)
# opciones de profesion
PROFESION_OPCIONES = (
    (ORIENTADOR, 'Orientador'),
    (PSICOLOGO, 'Psicologo'),
    (PEDAGOGO, 'Pedagogo'),
    (PSICOPEDAGOGO, 'Psicopedagogo'),
    (MAESTRO, 'Maestro')
)
# opciones de tipo de prueba
PRUEBA_OPCIONES = (
    (IPAL, 'IPAL'),
    (IPAM, 'IPAM'),
    (IPAE, 'IPAE')
)
