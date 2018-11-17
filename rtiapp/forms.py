from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import rtiapp.constantes as Globales

from .models import Evaluador, Grupo, Alumno, \
    Evaluacion_IPAL_INFANTIL, Evaluacion_IPAL_PRIMERO, Evaluacion_IPAL_SEGUNDO, \
    Evaluacion_IPAM_INFANTIL, Evaluacion_IPAM_PRIMERO, Evaluacion_IPAM_SEGUNDO, Evaluacion_IPAM_TERCERO, \
    Evaluacion_IPAE_PRIMERO, Evaluacion_IPAE_SEGUNDO, Evaluacion_IPAE_TERCERO


class SignUpForm(UserCreationForm):
    # campos complementarios
    nombre = forms.CharField(max_length=50, required=True, help_text='Su nombre completo')
    email = forms.EmailField(max_length=254, required=True, help_text='Direccion de correo')
    centro = forms.CharField(max_length=50, required=True, help_text='Su centro')
    pais = forms.ChoiceField(choices=Globales.PAIS_OPCIONES, required=True)
    sexo = forms.ChoiceField( choices=Globales.SEXO_OPCIONES, required=True)
    nivel_academico = forms.ChoiceField(choices=Globales.NIVEL_ACADEMICO_OPCIONES, required=True)
    profesion = forms.ChoiceField(choices=Globales.PROFESION_OPCIONES, required=True)
    zona = forms.ChoiceField(choices=Globales.ZONA_OPCIONES, required=True)
    class Meta:
        model = User
        fields = ('username', 'nombre', 'email', 'password1', 'password2',
                  'nivel_academico', 'profesion', 'zona','centro', 'pais', 'sexo' )



# forms IPAE

class Form_Evaluacion_IPAE_PRIMERO(forms.ModelForm):
    tarea1 = 'Pasar de mayúscula a minúscula'
    tarea2 = 'Dictado de palabras con ortografía arbitraria'
    tarea3 = 'Dictado de palabras con ortografía reglada'
    tarea4 = 'Dictado de pseudopalabras'
    tarea5 = 'Dictado de frases'
    TLC_1 = forms.IntegerField(required=False,min_value=0, max_value=108, label=tarea1)
    DICTADO_ORTOGRAFIA_ARBITRARIA = forms.IntegerField(required=False,min_value=0, max_value=20, label=tarea2)
    DICTADO_ORTOGRAFIA_REGLADA = forms.IntegerField(required=False,min_value=0, max_value=20, label=tarea3)
    DICTADO_PSEUDOPALABRAS = forms.IntegerField(required=False,min_value=0, max_value=20, label=tarea4)
    DICTADO_FRASES = forms.IntegerField(required=False,min_value=0, max_value=21, label=tarea5)
    class Meta:
        model = Evaluacion_IPAE_PRIMERO
        fields = '__all__'
        exclude = ('curso_academico','mes','prueba','alumno', 'tipo', 'momento', 'riesgo', 'omnibus', 'evaluador', 'mes_leible')

class Form_Evaluacion_IPAE_SEGUNDO(forms.ModelForm):
    tarea1 = 'Pasar de mayúscula a minúscula'
    tarea2 = 'Dictado de palabras con ortografía arbitraria'
    tarea3 = 'Dictado de palabras con ortografía reglada'
    tarea4 = 'Dictado de pseudopalabras'
    tarea5 = 'Dictado de frases'
    TLC_1 = forms.IntegerField(required=False, min_value=0, max_value=108, label=tarea1)
    DICTADO_ORTOGRAFIA_ARBITRARIA = forms.IntegerField(required=False, min_value=0, max_value=20, label=tarea2)
    DICTADO_ORTOGRAFIA_REGLADA = forms.IntegerField(required=False, min_value=0, max_value=20, label=tarea3)
    DICTADO_PSEUDOPALABRAS = forms.IntegerField(required=False, min_value=0, max_value=20, label=tarea4)
    DICTADO_FRASES = forms.IntegerField(required=False, min_value=0, max_value=21, label=tarea5)
    class Meta:
        model = Evaluacion_IPAE_SEGUNDO
        fields = '__all__'
        exclude = ('curso_academico','mes','prueba','alumno', 'tipo', 'momento', 'riesgo', 'omnibus', 'evaluador', 'mes_leible')



class Form_Evaluacion_IPAE_TERCERO(forms.ModelForm):
    tarea1 = 'Dictado de palabras con ortografía arbitraria'
    tarea2 = 'Dictado de palabras con ortografía reglada'
    tarea3 = 'Dictado de frases'
    tarea4 = 'Escritura de una historia (SPC-5)'
    tarea5 = 'Escritura de una historia (SPC-SPI-5)'
    tarea6 = 'Escritura de una historia (PDC-5)'
    DICTADO_ORTOGRAFIA_ARBITRARIA = forms.IntegerField(required=False, min_value=0, max_value=20, label=tarea1)
    DICTADO_ORTOGRAFIA_REGLADA = forms.IntegerField(required=False, min_value=0, max_value=20, label=tarea2)
    DICTADO_FRASES = forms.IntegerField(required=False, min_value=0, max_value=21, label=tarea3)
    SEC_5 = forms.IntegerField(required=False, min_value=0, max_value=80, label=tarea4)
    SEC_SEI_5 = forms.IntegerField(required=False, min_value=0, max_value=80, label=tarea5)
    PDC_5 = forms.IntegerField(required=False, min_value=0, max_value=80, label=tarea6)
    class Meta:
        model = Evaluacion_IPAE_TERCERO
        fields = '__all__'
        exclude = ('curso_academico','mes','prueba','alumno', 'tipo', 'momento', 'riesgo', 'omnibus', 'evaluador', 'mes_leible')



# forms IPAM


class Form_Evaluacion_IPAM_TERCERO(forms.ModelForm):
    tarea1 = 'Comparación Numérica (CN)'
    tarea2 = 'Operaciones de dos dígitos (ODD)'
    tarea3 = 'Secuencias Numéricas (SN)'
    tarea4 = 'Operaciones de un dígito (OUD)'
    tarea5 = 'Valor de Posición (VP)'
    CN = forms.IntegerField(required=False,min_value=0, max_value=64, label=tarea1)
    ODD = forms.IntegerField(required=False,min_value=0, max_value=45, label=tarea2)
    SN = forms.IntegerField(required=False,min_value=0, max_value=45, label=tarea3)
    OUD = forms.IntegerField(required=False,min_value=0, max_value=45, label=tarea4)
    VP = forms.IntegerField(required=False,min_value=0, max_value=45, label=tarea5)
    class Meta:
        model = Evaluacion_IPAM_TERCERO
        fields = '__all__'
        exclude = ('curso_academico','mes','prueba','alumno', 'tipo', 'momento', 'riesgo', 'omnibus', 'evaluador','mes_leible')



class Form_Evaluacion_IPAM_SEGUNDO(forms.ModelForm):
    tarea1 = 'Comparación Numérica (CN)'
    tarea2 = 'Operaciones de dos dígitos (ODD)'
    tarea3 = 'Secuencias Numéricas (SN)'
    tarea4 = 'Operaciones de un dígito (OUD)'
    tarea5 = 'Valor de Posición (VP)'
    CN = forms.IntegerField(required=False,min_value=0, max_value=64, label=tarea1)
    ODD = forms.IntegerField(required=False,min_value=0, max_value=45, label=tarea2)
    SN = forms.IntegerField(required=False,min_value=0, max_value=45, label=tarea3)
    OUD = forms.IntegerField(required=False,min_value=0, max_value=45, label=tarea4)
    VP = forms.IntegerField(required=False,min_value=0, max_value=45, label=tarea5)
    class Meta:
        model = Evaluacion_IPAM_SEGUNDO
        fields = '__all__'
        exclude = ('prueba','curso_academico','mes','alumno', 'tipo', 'momento', 'riesgo', 'omnibus', 'evaluador', 'mes_leible')



class Form_Evaluacion_IPAM_PRIMERO(forms.ModelForm):
    tarea1 = 'Comparación Numérica (CN)'
    tarea2 = 'Operaciones de dos dígitos (ODD)'
    tarea3 = 'Secuencias Numéricas (SN)'
    tarea4 = 'Operaciones de un dígito (OUD)'
    tarea5 = 'Valor de Posición (VP)'
    CN = forms.IntegerField(required=False,min_value=0, max_value=64, label=tarea1)
    ODD = forms.IntegerField(required=False,min_value=0, max_value=45, label=tarea2)
    SN = forms.IntegerField(required=False,min_value=0, max_value=45, label=tarea3)
    OUD = forms.IntegerField(required=False,min_value=0, max_value=45, label=tarea4)
    VP = forms.IntegerField(required=False,min_value=0, max_value=45, label=tarea5)
    class Meta:
        model = Evaluacion_IPAM_PRIMERO
        fields = '__all__'
        exclude = ('curso_academico','mes','prueba','alumno', 'tipo', 'momento', 'riesgo', 'omnibus', 'evaluador', 'mes_leible')


class Form_Evaluacion_IPAM_INFANTIL(forms.ModelForm):
    tarea1 = 'Comparación Numérica (CN)'
    tarea2 = 'Estimación Cantidad (EC)'
    tarea3 = 'Secuencias Numéricas (SN)'
    tarea4 = 'Identificación Numérica (IN)'
    tarea5 = 'Conteo Voz Alta (CVA)'
    tarea6 = 'Comparación Magnitud (CM) '
    CN = forms.IntegerField(required=False,min_value=0, max_value=64, label=tarea1)
    EC = forms.IntegerField(required=False,min_value=0, max_value=36, label=tarea2)
    SN = forms.IntegerField(required=False,min_value=0, max_value=36, label=tarea3)
    IN = forms.IntegerField(required=False,min_value=0, max_value=63, label=tarea4)
    CVA = forms.IntegerField(required=False,min_value=0, max_value=100, label=tarea5)
    CM = forms.IntegerField(required=False,min_value=0, max_value=40, label=tarea6)
    class Meta:
        model = Evaluacion_IPAM_INFANTIL
        fields = '__all__'
        exclude = ('curso_academico','mes','prueba','alumno', 'tipo', 'momento', 'riesgo', 'omnibus', 'evaluador', 'mes_leible')



# forms IPAL

class Form_Evaluacion_IPAL_INFANTIL(forms.ModelForm):
    tarea1 = 'Adivinanzas (ADI)'
    tarea2 = 'Conocimiento Sonido Letra (CSL)'
    tarea3 = 'Conocimiento Nombre Letra (CNL)'
    tarea4 = 'CLE-imagen'
    tarea5 = 'CLE-texto'
    tarea6 = 'Conciencia Fonológica Aislar (CFA)'
    ADIVINANZAS = forms.IntegerField(required=False,min_value=0, max_value=20, label=tarea1)
    CSL = forms.IntegerField(required=False,min_value=0, max_value=100, label=tarea2)
    CNL = forms.IntegerField(required=False,min_value=0, max_value=100, label=tarea3)
    CLE_IMAGEN = forms.IntegerField(required=False,min_value=0, max_value=35, label=tarea4)
    CLE_TEXTO = forms.IntegerField(required=False,min_value=0, max_value=6, label=tarea5)
    CFA = forms.IntegerField(required=False,min_value=0, max_value=80, label=tarea6)
    class Meta:
        model = Evaluacion_IPAL_INFANTIL
        fields = '__all__'
        progreso = False
        exclude = ('curso_academico', 'mes', 'prueba', 'alumno', 'tipo', 'momento', 'riesgo', 'omnibus', 'evaluador', 'mes_leible')


class Form_Evaluacion_IPAL_PRIMERO(forms.ModelForm):
    tarea1 = 'Textos Mutilados (TM)'
    tarea2 = 'Lectura de Pseudopalabras (LP)'
    tarea3 = 'Conocimiento Sonido Letra (CSL)'
    tarea4 = 'Conocimiento Nombre Letra (CNL)'
    tarea5 = 'Fluidez Lectura Oral (FLO)'
    tarea6 = 'CLE-texto'
    tarea7 = 'Conciencia Fonológica Segmentar (CFS)'
    TM = forms.IntegerField(required=False,min_value=0, max_value=20, label=tarea1)
    LP = forms.IntegerField(required=False,min_value=0, max_value=40, label=tarea2)
    CSL = forms.IntegerField(required=False,min_value=0, max_value=100, label=tarea3)
    CNL = forms.IntegerField(required=False,min_value=0, max_value=100, label=tarea4)
    FLO = forms.IntegerField(required=False,min_value=0, max_value=133, label=tarea5)
    CLE_TEXTO = forms.IntegerField(required=False,min_value=0, max_value=6, label=tarea6)
    CFS = forms.IntegerField(required=False,min_value=0, max_value=85, label=tarea7)
    class Meta:
        model = Evaluacion_IPAL_PRIMERO
        fields = '__all__'
        exclude = ('curso_academico','prueba','mes','alumno', 'tipo', 'momento', 'riesgo', 'omnibus', 'evaluador', 'mes_leible')



class Form_Evaluacion_IPAL_SEGUNDO(forms.ModelForm):
    tarea1 = 'Conocimiento Nombre Letra (CNL)'
    tarea2 = 'Lectura de Pseudopalabras (LP)'
    tarea3 = 'Textos Mutilados (TM)'
    tarea4 = 'Prosodia (PRO)'
    tarea5 = 'Fluidez Lectura Oral (FLO)'
    tarea6 = 'Conocimiento Sonido Letra (CSL)'
    tarea7 = 'CLEtexto'
    tarea8 = 'Conciencia Fonológica Segmentar (CFS)'
    tarea9 = 'Vocabulario (VOC)'
    CNL = forms.IntegerField(required=False,min_value=0, max_value=100, label=tarea1)
    LP = forms.IntegerField(required=False,min_value=0, max_value=40, label=tarea2)
    TM = forms.IntegerField(required=False,min_value=0, max_value=20, label=tarea3)
    PRO = forms.IntegerField(required=False,min_value=0, max_value=133, label=tarea4)
    FLO = forms.IntegerField(required=False,min_value=0, max_value=133, label=tarea5)
    # tareas complementarias 'CSL', 'CLE_TEXTO', 'CFS', 'VOC',
    CSL = forms.IntegerField(required=False,min_value=0, max_value=100, label=tarea6)
    CLE_TEXTO = forms.IntegerField(required=False,min_value=0, max_value=20, label=tarea7)
    CFS = forms.IntegerField(required=False,min_value=0, max_value=85, label=tarea8)
    VOC = forms.IntegerField(required=False,min_value=0, max_value=30, label=tarea9)
    class Meta:
        model = Evaluacion_IPAL_SEGUNDO
        fields = '__all__'
        exclude = ('curso_academico','mes','prueba','alumno', 'tipo', 'momento', 'riesgo', 'omnibus',
                   'evaluador', 'observaciones', 'mes_leible')


# formulario para grupos
class FormGrupo(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = ('nombre', 'curso', 'curso_academico', 'centro')


# formulario para enviar la edicion del nuevo alumno
class FormAlumnoPOST(forms.ModelForm):
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'),
                                       input_formats=('%d/%m/%Y',))
    class Meta:
        model = Alumno
        fields = ('codigo', 'sexo', 'fecha_nacimiento', 'curso_academico','pais', 'curso', 'centro', 'grupo')

class FormAlumnoConsejeriaPOST(forms.ModelForm):
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'),
                                       input_formats=('%d/%m/%Y',))
    class Meta:
        model = Alumno
        fields = ('codigo', 'sexo', 'fecha_nacimiento', 'curso_academico','pais', 'curso', 'centro')



# formulario para editar y crear nuevo alumno,
# en el que el grupo esta forzado
class FormAlumnoGrupoForzado(forms.ModelForm):
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'),
                                       input_formats=('%d/%m/%Y',))
    class Meta:
        model = Alumno
        fields = ('codigo', 'sexo', 'fecha_nacimiento')



# formulario para editar y crear nuevo alumno,
# en el que se puede seleccionar el grupo
class FormAlumno(forms.ModelForm):
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'),
                                       input_formats=('%d/%m/%Y',))
    class Meta:
        model = Alumno
        fields = ('codigo', 'sexo', 'fecha_nacimiento', 'pais', 'curso', 'curso_academico', 'centro', 'grupo')


    def __init__(self, user_evaluador, *args, **kwargs):
        super(FormAlumno, self).__init__(*args, **kwargs)
        self.fields['grupo'].queryset = Grupo.objects.filter(evaluador=user_evaluador)


# formulario en el que no se puede cmbiar el grupo
# del alumno (profesores consejeria)
class FormAlumnoConsejeria(forms.ModelForm):
    fecha_nacimiento = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'),
                                       input_formats=('%d/%m/%Y',))

    class Meta:
        model = Alumno
        fields = ('codigo', 'sexo', 'fecha_nacimiento', 'pais', 'curso', 'curso_academico', 'centro')


    def __init__(self, user_evaluador, *args, **kwargs):
        super(FormAlumnoConsejeria, self).__init__(*args, **kwargs)
        self.fields['codigo'].widget.attrs['readonly'] = True
        self.fields['curso'].widget.attrs['readonly'] = True
        self.fields['pais'].widget.attrs['readonly'] = True
        self.fields['centro'].widget.attrs['readonly'] = True

        # self.fields['grupo'].queryset = Grupo.objects.filter(evaluador=user_evaluador)




# formulario para evaluadores
class FormEvaluador(forms.ModelForm):
    class Meta:
        model = Evaluador
        fields = '__all__'
        exclude = ('clave','usuario', 'informacion_adicional_completa', 'centro_pilotaje', 'codigo')
