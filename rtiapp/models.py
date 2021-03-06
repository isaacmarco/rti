from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
import rtiapp.constantes as Globales

# tipo de prueba
IPAL = 'IPAL'
IPAM = 'IPAM'
IPAE = 'IPAE'
# islas
NINGUNA = 'NINGUNA'
TENERIFE = 'TENERIFE'
PALMA = 'PALMA'
GOMERA = 'GOMERA'
HIERRO = 'HIERRO'
GRANCANARIA = 'GRANCANARIA'
FUERTEVENTURA = 'FUERTEVENTURA'
LANZAROTE = 'LANZAROTE'
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
MOMENTO_DEFECTO = 'PROGRESO'
INICIO = 'INICIO'
MEDIO = 'MEDIO'
FIN = 'FIN'
# paises
ESP = 'ESP'
ECU = 'ECU'
GTM = 'GTM'
CAN = 'CAN'
PAN = 'PAN'
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
LOGOPEDA = 'LP'
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
    (ALTO_RIESGO, 'Alto riesgo'),
    (RIESGO, 'Riesgo'),
    (BAJO, 'Rendimiento bajo'),
    (NORMAL, 'Rendimiento normal'),
    (OPTIMO, 'Rendimiento optimo')
)
# opciones de evaluaciones
MOMENTOS_OPCIONES = (
    (MOMENTO_DEFECTO, 'Progreso'),
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
# opciones de isla
ISLA_OPCIONES = (
    (NINGUNA, 'Ninguna'),
    (TENERIFE, 'Tenerife'),
    (GOMERA, 'Gomera'),
    (PALMA, 'Palma'),
    (HIERRO, 'Hierro'),
    (GRANCANARIA, 'GranCanaria'),
    (FUERTEVENTURA, 'Fuerteventura'),
    (LANZAROTE, 'Lanzarote')
)
# opciones de pais
PAIS_OPCIONES = (
    (ESP, 'España'),
    (GTM, 'Guatemala'),
    (ECU, 'Ecuador'),
    (CAN, 'Canarias'),
    (PAN, 'Panama')
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
    (MAESTRO, 'Maestro'),
    (LOGOPEDA, 'Logopeda')
)
# opciones de tipo de prueba
PRUEBA_OPCIONES = (
    (IPAL, 'IPAL'),
    (IPAM, 'IPAM'),
    (IPAE, 'IPAE')
)


class Evaluador(models.Model):

    # identificador del usuario y datos personales
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    clave = models.CharField(max_length=20, default="Clave del evaluador")
    nombre = models.CharField(max_length=50, default="Nombre del evaluador")
    centro = models.CharField(max_length=50, default="Centro del evaluador")
    # centro forzado para el grupo ULL (el usuario no puede cambiarlo)
    centro_pilotaje = models.CharField(max_length=50, default="Centro pilotaje")
    # codigo forzado para el grupo ULL (el usuario no puede cambiarlo)
    codigo = models.CharField(max_length=20, default="Codigo")
    email = models.EmailField(default='email@email.com')

    # fecha en la que se registro el evaluador
    fecha_alta = models.DateTimeField(auto_now_add=True)
    ultima_modificacion = models.DateTimeField(auto_now=True)

    # indica que el evaluador ha completado toda su
    # informacion necesaria para usar la plataforma
    informacion_adicional_completa = models.BooleanField(default=False)

    # curso academico en el que esta trabajoro
    # actualmente en la plataforma
    curso_academico = models.IntegerField(default=2018)

    # sexo
    pais = models.CharField(
        max_length=3,
        choices=PAIS_OPCIONES,
        default=ESP
    )

    # sexo
    sexo = models.CharField(
        max_length=2,
        choices=SEXO_OPCIONES,
        default=HOMBRE
    )

    # nivel academico
    nivel_academico = models.CharField(
        max_length=2,
        choices=NIVEL_ACADEMICO_OPCIONES,
        default=GRADO
    )

    # profesion
    profesion = models.CharField(
        max_length=2,
        choices=PROFESION_OPCIONES,
        default=MAESTRO
    )

    # zona
    zona = models.CharField(
        max_length=2,
        choices=ZONA_OPCIONES,
        default=URBANA
    )

    def __str__(self):
        return self.nombre

    class Meta(object):
        verbose_name = 'Evaluador'
        verbose_name_plural = 'Evaluadores'




class Grupo(models.Model):

    nombre = models.CharField(max_length=100, default="Nombre del grupo")#, help_text='Nombre del grupo')
    # el campo evaluador identifica al creador original del grupo, ya que
    # ahora varios evaluadores pueden compartir grupo mediante la relacion grupo-evaluador
    evaluador = models.ForeignKey(User,  default=0) # borrar un evaluador no elimina sus grupos (on_delete=models.CASCADE,)
    curso_academico = models.IntegerField(default=2018)#, help_text='Curso academico')
    centro = models.CharField(max_length=100, default="Centro")
    centro_pilotaje = models.CharField(max_length=50, default="Centro pilotaje") # centro de la consejeria
    codigo = models.CharField(max_length=50, default="Codigo del grupo")  # centro de la consejeria
    fecha_alta = models.DateTimeField(auto_now_add=True)
    ultima_modificacion = models.DateTimeField(auto_now=True)
    isla = models.CharField(max_length=15, choices=ISLA_OPCIONES, default=NINGUNA)

    # todos los evaluadores que tienen acceso al grupo
    evaluadores = models.ManyToManyField(
        User, related_name='Evaluadores'
    )
    curso = models.CharField(
        max_length=20,
        choices=CURSO_OPCIONES,
        default=INFANTIL
    )

    def __str__(self):
        return self.nombre


import datetime
class Alumno(models.Model):

    codigo = models.CharField(max_length=100, default="código del alumno")
    fecha_nacimiento = models.DateField(default=datetime.date.today)
    centro = models.CharField(max_length=100, default="Centro")
    evaluador = models.ForeignKey(User,  default=0) # eliminar un evaluador no elimina sus alumnos (on_delete=models.CASCADE,
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, default=0)
    curso_academico = models.IntegerField(default=2018)
    isla = models.CharField(max_length=15, choices=ISLA_OPCIONES, default=NINGUNA)
    # fechas de alta del alumno y actualizacion de su ficha
    fecha_alta = models.DateTimeField(auto_now_add=True)
    ultima_modificacion = models.DateTimeField(auto_now=True)

    centro_pilotaje = models.CharField(max_length=50, default="Centro pilotaje")
    codigo_evaluador = models.CharField(max_length=20, default="Codigo")

    curso = models.CharField(
        max_length=20,
        choices=CURSO_OPCIONES,
        default=INFANTIL
    )

    sexo = models.CharField(
        max_length=2,
        choices=SEXO_OPCIONES,
        default=HOMBRE
    )

    pais = models.CharField(
        max_length=3,
        choices=PAIS_OPCIONES,
        default=ESP
    )

    # recordar cuoro es la ultima evaluacion
    ultima_evaluacion_curso = models.IntegerField(default=0)
    ultima_evaluacion_mes = models.IntegerField(choices=FECHA_OPCIONES,default=NOVIEMBRE)


    # niveles de riesgo en cada prueba y curso
    riesgo_IPAL = models.CharField(max_length=4,choices=RIESGO_OPCIONES,default=SIN_EVALUAR)
    riesgo_IPAL_INICIO = models.CharField(max_length=4, choices=RIESGO_OPCIONES, default=SIN_EVALUAR)
    riesgo_IPAL_MEDIO = models.CharField(max_length=4, choices=RIESGO_OPCIONES, default=SIN_EVALUAR)
    riesgo_IPAL_FIN = models.CharField(max_length=4, choices=RIESGO_OPCIONES, default=SIN_EVALUAR)

    riesgo_IPAM = models.CharField(max_length=4, choices=RIESGO_OPCIONES, default=SIN_EVALUAR)
    riesgo_IPAM_INICIO = models.CharField(max_length=4, choices=RIESGO_OPCIONES, default=SIN_EVALUAR)
    riesgo_IPAM_MEDIO = models.CharField(max_length=4, choices=RIESGO_OPCIONES, default=SIN_EVALUAR)
    riesgo_IPAM_FIN = models.CharField(max_length=4, choices=RIESGO_OPCIONES, default=SIN_EVALUAR)

    riesgo_IPAE = models.CharField(max_length=4, choices=RIESGO_OPCIONES, default=SIN_EVALUAR)
    riesgo_IPAE_INICIO = models.CharField(max_length=4, choices=RIESGO_OPCIONES, default=SIN_EVALUAR)
    riesgo_IPAE_MEDIO = models.CharField(max_length=4, choices=RIESGO_OPCIONES, default=SIN_EVALUAR)
    riesgo_IPAE_FIN = models.CharField(max_length=4, choices=RIESGO_OPCIONES, default=SIN_EVALUAR)



    def __str__(self):
        return self.codigo



    def key_IPAL_INICIO(self):
        return str(self.pk) + 'IPALINICIO'
    def key_IPAL_MEDIO(self):
        return str(self.pk) + 'IPALMEDIO'
    def key_IPAL_FIN(self):
        return str(self.pk) + 'IPALFIN'

    def key_IPAM_INICIO(self):
        return str(self.pk) + 'IPAMINICIO'
    def key_IPAM_MEDIO(self):
        return str(self.pk) + 'IPAMMEDIO'
    def key_IPAM_FIN(self):
        return str(self.pk) + 'IPAMFIN'

    def key_IPAE_INICIO(self):
        return str(self.pk) + 'IPAEINICIO'
    def key_IPAE_MEDIO(self):
        return str(self.pk) + 'IPAEMEDIO'
    def key_IPAE_FIN(self):
        return str(self.pk) + 'IPAEFIN'

    class Meta(object):
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'



colores_riesgo = {
  "NOEV": "#ffffff",
  "ALTR": "#850202",
  "RIES": "#f00",
  "BAJO": "#fff200",
  "NORM": "#009fff",
  "OPTI": "#1ae36e"
}

class Evaluacion(models.Model):

    evaluador = models.ForeignKey(User, default=0) # eliminar el evaluador no elimina las evaluaciones
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, default=0)  # eliminar el alumno SI elimina las evaluaciones
    omnibus = models.DecimalField(default=0, max_digits=12, decimal_places=10)
    curso_academico = models.IntegerField(default=2018)
    mes_leible = models.CharField(max_length=10, default='noviembre')
    fecha_alta = models.DateTimeField(auto_now_add=True)
    ultima_modificacion = models.DateTimeField(auto_now=True)

    # indica que la evaluacion es valida
    evaluado = models.BooleanField(default=False)

    prueba = models.CharField(
        max_length=4,
        choices=PRUEBA_OPCIONES,
        default=IPAL
    )

    riesgo = models.CharField(
        max_length=4,
        choices=RIESGO_OPCIONES,
        default=SIN_EVALUAR
    )

    momento = models.CharField(
        max_length=10,
        choices=MOMENTOS_OPCIONES,
        default=MOMENTO_DEFECTO
    )

    mes = models.IntegerField(
        choices=FECHA_OPCIONES,
        default=NOVIEMBRE
    )

    tipo = models.CharField(
        max_length=3,
        choices=EVALUACION_OPCIONES,
        default=CRIBADO
    )

    def key(self):
        return str(self.alumno.pk) + self.prueba + self.momento

    def color_riesgo(self):
        return colores_riesgo[self.riesgo]

    def get_evaluador(self):
        return Evaluador.objects.filter(evaluador=self.evaluador).name

    class Meta:
        abstract = True



# IPAL

class Evaluacion_IPAL_INFANTIL(Evaluacion):

    ADIVINANZAS = models.IntegerField(default=-1,  validators=[MaxValueValidator(20), MinValueValidator(-1)])
    CSL = models.IntegerField(default=-1,  validators=[MaxValueValidator(100), MinValueValidator(-1)])
    CNL = models.IntegerField(default=-1,  validators=[MaxValueValidator(100), MinValueValidator(-1)])
    CLE_IMAGEN = models.IntegerField(default=-1,  validators=[MaxValueValidator(35), MinValueValidator(-1)])
    CLE_TEXTO = models.IntegerField(default=-1,  validators=[MaxValueValidator(6), MinValueValidator(-1)])
    CFA = models.IntegerField(default=-1,  validators=[MaxValueValidator(80), MinValueValidator(-1)])

    def tareas(self):
        return [self.CFA, self.CSL]

    def tareas_progreso(self):
        return [self.ADIVINANZAS, self.CSL, self.CNL, self.CLE_IMAGEN, self.CLE_TEXTO, self.CFA]




'''
 Adivinanzas (ADI)  
 Conocimiento Sonido Letra (CSL)  
 Conocimiento Nombre Letra (CNL)  
 Cleimagen 
 CLEtexto 
 Conciencia Fonológica Aislar (CFA)  
'''


class Evaluacion_IPAL_PRIMERO(Evaluacion):

    TM = models.IntegerField(default=-1,  validators=[MaxValueValidator(20), MinValueValidator(-1)])
    LP = models.IntegerField(default=-1,  validators=[MaxValueValidator(40), MinValueValidator(-1)])
    CSL = models.IntegerField(default=-1,  validators=[MaxValueValidator(100), MinValueValidator(-1)])
    CNL = models.IntegerField(default=-1,  validators=[MaxValueValidator(100), MinValueValidator(-1)])
    FLO = models.IntegerField(default=-1,  validators=[MaxValueValidator(133), MinValueValidator(-1)])
    CLE_TEXTO = models.IntegerField(default=-1,  validators=[MaxValueValidator(6), MinValueValidator(-1)])
    CFS = models.IntegerField(default=-1,  validators=[MaxValueValidator(85), MinValueValidator(-1)])

    def tareas(self):
        return [self.TM, self.LP, self.CSL, self.CNL, self.FLO, self.CLE_TEXTO, self.CFS]

    def tareas_progreso(self):
        return [self.LP, self.CNL, self.FLO, self.CSL]

    def reiniciar(self):
        self.TM = -1
        self.LP = -1
        self.CSL = -1
        self.CNL = -1
        self.FLO = -1
        self.CLE_TEXTO = -1
        self.CFS = -1

'''
•	Textos Mutilados (TM) 
•	Lectura de Pseudopalabras (LP) 
•	Conocimiento Sonido Letra (CSL)  
•	Conocimiento Nombre Letra (CNL)  
•	Fluidez Lectura Oral (FLO) 
•	CLEtexto 
•	Conciencia Fonológica Segmentar (CFS)  
'''



class Evaluacion_IPAL_SEGUNDO(Evaluacion):

    # subpruebas de evaluacion
    CNL = models.IntegerField(default=-1, validators=[MaxValueValidator(100), MinValueValidator(-1)])
    LP = models.IntegerField(default=-1, validators=[MaxValueValidator(40), MinValueValidator(-1)])
    TM = models.IntegerField(default=-1, validators=[MaxValueValidator(20), MinValueValidator(-1)])
    FLO = models.IntegerField(default=-1, validators=[MaxValueValidator(133), MinValueValidator(-1)])
    PRO = models.IntegerField(default=-1, validators=[MinValueValidator(-1)])

    '''
    •	Conocimiento Nombre Letra (CNL) 
    •	Lectura de Pseudopalabras (LP) 
    •	Textos Mutilados (TM)  
    •	Fluidez Lectura Oral (FLO)  
    •	Prosodia (PRO)
    ------------------------    
    
    •	Conocimiento Sonido Letra (CSL) 0-100
    •	CLEtexto 0-20
    •	Conciencia Fonológica Segmentar (CFS) 0-85
    •	Vocabulario (VOC) 0-30
    '''

    # subpruebas complementarias, no se usan para el calculo
    # de omnibus ni riesgo, pero si se usaran para
    # ciertos informes de progreso del alumno

    CSL = models.IntegerField(default=-1, validators=[MaxValueValidator(100), MinValueValidator(-1)])
    CLE_TEXTO = models.IntegerField(default=-1, validators=[MaxValueValidator(20), MinValueValidator(-1)])
    CFS = models.IntegerField(default=-1, validators=[MaxValueValidator(85), MinValueValidator(-1)])
    VOC = models.IntegerField(default=-1, validators=[MaxValueValidator(30), MinValueValidator(-1)])


    def tareas(self):
        return [self.CNL, self.LP, self.TM, self.FLO, self.PRO, self.CSL, self.CLE_TEXTO, self.CFS, self.VOC]

    def tareas_progreso(self):
        return [self.LP, self.CNL, self.FLO, self.CSL]


# IPAM

class Evaluacion_IPAM_INFANTIL(Evaluacion):

    CN = models.IntegerField(default=-1, validators=[MaxValueValidator(64), MinValueValidator(-1)])
    EC = models.IntegerField(default=-1, validators=[MaxValueValidator(36), MinValueValidator(-1)])
    SN = models.IntegerField(default=-1, validators=[MaxValueValidator(36), MinValueValidator(-1)])
    IN = models.IntegerField(default=-1, validators=[MaxValueValidator(63), MinValueValidator(-1)])
    CVA = models.IntegerField(default=-1, validators=[MaxValueValidator(100), MinValueValidator(-1)])
    CM = models.IntegerField(default=-1, validators=[MaxValueValidator(40), MinValueValidator(-1)])

    def tareas(self):
        return [self.CN, self.EC, self.SN, self.IN, self.CVA, self.CM]

    def tareas_progreso(self):
        return [self.CN, self.EC, self.SN, self.IN, self.CVA, self.CM]

'''
•	Comparación Numérica (CN) 
•	Estimación Cantidad (EC)  
•	Secuencias Numéricas (SN)  
•	Identificación Numérica (IN)  
•	Conteo Voz Alta (CVA)  
•	Comparación Magnitud (CM) 
'''


class Evaluacion_IPAM_PRIMERO(Evaluacion):

    CN = models.IntegerField(default=-1, validators=[MaxValueValidator(64), MinValueValidator(-1)])
    ODD = models.IntegerField(default=-1, validators=[MaxValueValidator(45), MinValueValidator(-1)])
    SN = models.IntegerField(default=-1, validators=[MaxValueValidator(45), MinValueValidator(-1)])
    OUD = models.IntegerField(default=-1, validators=[MaxValueValidator(45), MinValueValidator(-1)])
    VP = models.IntegerField(default=-1, validators=[MaxValueValidator(45), MinValueValidator(-1)])

    def tareas(self):
        return [self.CN, self.ODD, self.SN, self.OUD, self.VP]

    def tareas_progreso(self):
        return [self.CN, self.SN, self.OUD]

    def reiniciar(self):
        self.CN = -1
        self.ODD = -1
        self.SN = -1
        self.OUD = -1
        self.VP = -1

'''
•	Comparación Numérica (CN)  
•	Operaciones de dos dígitos (ODD)  
•	Secuencias Numéricas (SN) 
•	Operaciones de un dígito (OUD)  
•	Valor de Posición (VP)  
'''


class Evaluacion_IPAM_SEGUNDO(Evaluacion):

    CN = models.IntegerField(default=-1, validators=[MaxValueValidator(64), MinValueValidator(-1)])
    ODD = models.IntegerField(default=-1, validators=[MaxValueValidator(45), MinValueValidator(-1)])
    SN = models.IntegerField(default=-1, validators=[MaxValueValidator(45), MinValueValidator(-1)])
    OUD = models.IntegerField(default=-1, validators=[MaxValueValidator(45), MinValueValidator(-1)])
    VP = models.IntegerField(default=-1, validators=[MaxValueValidator(45), MinValueValidator(-1)])

    def tareas(self):
        return [self.CN, self.ODD, self.SN, self.OUD, self.VP]

    def tareas_progreso(self):
        return [self.CN, self.ODD, self.SN, self.OUD, self.VP]
'''
•	Comparación Numérica (CN) 
•	Operaciones de dos dígitos (ODD)  
•	Secuencias Numéricas (SN)  
•	Operaciones de un dígito (OUD)  
•	Valor de Posición (VP) 

'''

class Evaluacion_IPAM_TERCERO(Evaluacion):

    CN = models.IntegerField(default=-1, validators=[MaxValueValidator(64), MinValueValidator(-1)])
    ODD = models.IntegerField(default=-1, validators=[MaxValueValidator(45), MinValueValidator(-1)])
    SN = models.IntegerField(default=-1, validators=[MaxValueValidator(45), MinValueValidator(-1)])
    OUD = models.IntegerField(default=-1, validators=[MaxValueValidator(45), MinValueValidator(-1)])
    VP = models.IntegerField(default=-1, validators=[MaxValueValidator(45), MinValueValidator(-1)])

    def tareas(self):
        return [self.CN, self.ODD, self.SN, self.OUD, self.VP]

    def tareas_progreso(self):
        return [self.CN, self.ODD, self.SN, self.OUD, self.VP]


'''
•	Comparación Numérica (CN)  
•	Operaciones de dos dígitos (ODD)  
•	Secuencias Numéricas (SN)  
•	Operaciones de un dígito (OUD)  
•	Valor de Posición (VP)  
'''



# IPAE

class Evaluacion_IPAE_PRIMERO(Evaluacion):

    TLC_1 = models.IntegerField(default=-1, validators=[MaxValueValidator(108), MinValueValidator(-1)])
    DICTADO_ORTOGRAFIA_ARBITRARIA = models.IntegerField(default=-1, validators=[MaxValueValidator(20), MinValueValidator(-1)])
    DICTADO_ORTOGRAFIA_REGLADA = models.IntegerField(default=-1, validators=[MaxValueValidator(20), MinValueValidator(-1)])
    DICTADO_PSEUDOPALABRAS = models.IntegerField(default=-1, validators=[MaxValueValidator(20), MinValueValidator(-1)])
    DICTADO_FRASES = models.IntegerField(default=-1, validators=[MaxValueValidator(21), MinValueValidator(-1)])

    def tareas_progreso(self):
        return [self.TLC_1, self.DICTADO_ORTOGRAFIA_ARBITRARIA, self.DICTADO_ORTOGRAFIA_REGLADA, \
                self.DICTADO_PSEUDOPALABRAS, self.DICTADO_FRASES]


    def tareas(self):
        return [self.TLC_1, self.DICTADO_ORTOGRAFIA_ARBITRARIA, self.DICTADO_ORTOGRAFIA_REGLADA, \
                self.DICTADO_PSEUDOPALABRAS, self.DICTADO_FRASES]

    def reiniciar(self):
        self.TLC_1 = -1
        self.DICTADO_ORTOGRAFIA_ARBITRARIA = -1
        self.DICTADO_ORTOGRAFIA_REGLADA = -1
        self.DICTADO_PSEUDOPALABRAS = -1
        self.DICTADO_FRASES = -1

'''
Pasar de mayúscula a minúscula (TLC-1)	 
Dictado de palabras con ortografía arbitraria  
Dictado de palabras con ortografía reglada  
Dictado de pseudopalabras	 
Dictado de frases	 
'''

class Evaluacion_IPAE_SEGUNDO(Evaluacion):

    TLC_1 = models.IntegerField(default=-1, validators=[MaxValueValidator(108), MinValueValidator(-1)])
    DICTADO_ORTOGRAFIA_ARBITRARIA = models.IntegerField(default=-1, validators=[MaxValueValidator(20), MinValueValidator(-1)])
    DICTADO_ORTOGRAFIA_REGLADA = models.IntegerField(default=-1, validators=[MaxValueValidator(20), MinValueValidator(-1)])
    DICTADO_PSEUDOPALABRAS = models.IntegerField(default=-1, validators=[MaxValueValidator(20), MinValueValidator(-1)])
    DICTADO_FRASES = models.IntegerField(default=-1, validators=[MaxValueValidator(21), MinValueValidator(-1)])


    def tareas(self):
        return [self.TLC_1, self.DICTADO_ORTOGRAFIA_ARBITRARIA, self.DICTADO_ORTOGRAFIA_REGLADA, \
                self.DICTADO_PSEUDOPALABRAS, self.DICTADO_FRASES]

    def tareas_progreso(self):
        return [self.TLC_1, self.DICTADO_ORTOGRAFIA_ARBITRARIA, self.DICTADO_ORTOGRAFIA_REGLADA, \
                self.DICTADO_PSEUDOPALABRAS, self.DICTADO_FRASES]


'''
Pasar de mayúscula a minúscula (TLC-1)
Dictado de palabras con ortografía arbitraria 
Dictado de palabras con ortografía reglada 
Dictado de pseudopalabras
Dictado de frases
'''


class Evaluacion_IPAE_TERCERO(Evaluacion):

    DICTADO_ORTOGRAFIA_ARBITRARIA = models.IntegerField(default=-1, validators=[MaxValueValidator(20), MinValueValidator(-1)])
    DICTADO_ORTOGRAFIA_REGLADA = models.IntegerField(default=-1, validators=[MaxValueValidator(20), MinValueValidator(-1)])
    DICTADO_FRASES = models.IntegerField(default=-1, validators=[MaxValueValidator(21), MinValueValidator(-1)])
    SEC_5 = models.IntegerField(default=-1, validators=[MaxValueValidator(80), MinValueValidator(-1)])
    SEC_SEI_5 = models.IntegerField(default=-1, validators=[MaxValueValidator(80), MinValueValidator(-1)])
    PDC_5 = models.IntegerField(default=-1, validators=[MaxValueValidator(80), MinValueValidator(-1)])


    def tareas(self):
        return [self.DICTADO_ORTOGRAFIA_ARBITRARIA, self.DICTADO_ORTOGRAFIA_REGLADA, self.DICTADO_FRASES, \
                self.SEC_5, self.SEC_SEI_5, self.PDC_5]

    def tareas_progreso(self):
        return [self.DICTADO_ORTOGRAFIA_ARBITRARIA, self.DICTADO_ORTOGRAFIA_REGLADA, self.DICTADO_FRASES, \
                self.SEC_5, self.SEC_SEI_5, self.PDC_5]


'''
Dictado de palabras con ortografía arbitraria 
Dictado de palabras con ortografía reglada 
Dictado de frases	 
Escritura de una historia (SEC-5) 
Escritura de una historia (SEC-SEI-5) 
Escritura de una historia (PDC-5) 
'''






