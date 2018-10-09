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
# todo faltan los valores maximos y minimos
class Form_Evaluacion_IPAE_PRIMERO(forms.ModelForm):
    class Meta:
        model = Evaluacion_IPAE_PRIMERO
        fields = '__all__'
        exclude = ('curso_academico','mes','prueba','alumno', 'tipo', 'momento', 'riesgo', 'omnibus', 'evaluador', 'mes_leible')

class Form_Evaluacion_IPAE_SEGUNDO(forms.ModelForm):
    class Meta:
        model = Evaluacion_IPAE_SEGUNDO
        fields = '__all__'
        exclude = ('curso_academico','mes','prueba','alumno', 'tipo', 'momento', 'riesgo', 'omnibus', 'evaluador', 'mes_leible')

class Form_Evaluacion_IPAE_TERCERO(forms.ModelForm):
    class Meta:
        model = Evaluacion_IPAE_TERCERO
        fields = '__all__'
        exclude = ('curso_academico','mes','prueba','alumno', 'tipo', 'momento', 'riesgo', 'omnibus', 'evaluador', 'mes_leible')


# forms IPAM


class Form_Evaluacion_IPAM_TERCERO(forms.ModelForm):
    CN = forms.IntegerField(min_value=0, max_value=64, label='CN')
    ODD = forms.IntegerField(min_value=0, max_value=45, label='ODD')
    SN = forms.IntegerField(min_value=0, max_value=45, label='SN')
    OUD = forms.IntegerField(min_value=0, max_value=45, label='OUD')
    VP = forms.IntegerField(min_value=0, max_value=45, label='VP')
    class Meta:
        model = Evaluacion_IPAM_TERCERO
        fields = '__all__'
        exclude = ('curso_academico','mes','prueba','alumno', 'tipo', 'momento', 'riesgo', 'omnibus', 'evaluador','mes_leible')


class Form_Evaluacion_IPAM_SEGUNDO(forms.ModelForm):
    CN = forms.IntegerField(min_value=0, max_value=64, label='CN')
    ODD = forms.IntegerField(min_value=0, max_value=45, label='ODD')
    SN = forms.IntegerField(min_value=0, max_value=45, label='SN')
    OUD = forms.IntegerField(min_value=0, max_value=45, label='OUD')
    VP = forms.IntegerField(min_value=0, max_value=45, label='VP')
    class Meta:
        model = Evaluacion_IPAM_SEGUNDO
        fields = '__all__'
        exclude = ('prueba','curso_academico','mes','alumno', 'tipo', 'momento', 'riesgo', 'omnibus', 'evaluador', 'mes_leible')


class Form_Evaluacion_IPAM_PRIMERO(forms.ModelForm):
    CN = forms.IntegerField(min_value=0, max_value=64, label='CN')
    ODD = forms.IntegerField(min_value=0, max_value=45, label='ODD')
    SN = forms.IntegerField(min_value=0, max_value=45, label='SN')
    OUD = forms.IntegerField(min_value=0, max_value=45, label='OUD')
    VP = forms.IntegerField(min_value=0, max_value=45, label='VP')
    class Meta:
        model = Evaluacion_IPAM_PRIMERO
        fields = '__all__'
        exclude = ('curso_academico','mes','prueba','alumno', 'tipo', 'momento', 'riesgo', 'omnibus', 'evaluador', 'mes_leible')


class Form_Evaluacion_IPAM_INFANTIL(forms.ModelForm):
    CN = forms.IntegerField(min_value=0, max_value=64, label='CN')
    EC = forms.IntegerField(min_value=0, max_value=36, label='EC')
    SN = forms.IntegerField(min_value=0, max_value=36, label='SN')
    IN = forms.IntegerField(min_value=0, max_value=63, label='IN')
    CVA = forms.IntegerField(min_value=0, max_value=100, label='CVA')
    CM = forms.IntegerField(min_value=0, max_value=40, label='CM')
    class Meta:
        model = Evaluacion_IPAM_INFANTIL
        fields = '__all__'
        exclude = ('curso_academico','mes','prueba','alumno', 'tipo', 'momento', 'riesgo', 'omnibus', 'evaluador', 'mes_leible')


# forms IPAL

class Form_Evaluacion_IPAL_INFANTIL(forms.ModelForm):
    ADIVINANZAS = forms.IntegerField(min_value=0, max_value=20, label='ADIVINANZAS')
    CSL = forms.IntegerField(min_value=0, max_value=100, label='CSL')
    CNL = forms.IntegerField(min_value=0, max_value=100, label='CNL')
    CLE_IMAGEN = forms.IntegerField(min_value=0, max_value=35, label='CLE_IMAGEN')
    CLE_TEXTO = forms.IntegerField(min_value=0, max_value=6, label='CLE_TEXTO')
    CFA = forms.IntegerField(min_value=0, max_value=80, label='CFA')

    class Meta:
        model = Evaluacion_IPAL_INFANTIL
        fields = '__all__'
        progreso = False
        exclude = ('curso_academico', 'mes', 'prueba', 'alumno', 'tipo', 'momento', 'riesgo', 'omnibus', 'evaluador', 'mes_leible')


class Form_Evaluacion_IPAL_PRIMERO(forms.ModelForm):
    TM = forms.IntegerField(min_value=0, max_value=20, label='TM')
    LP = forms.IntegerField(min_value=0, max_value=40, label='LP')
    CSL = forms.IntegerField(min_value=0, max_value=100, label='CSL')
    CNL = forms.IntegerField(min_value=0, max_value=100, label='CNL')
    FLO = forms.IntegerField(min_value=0, max_value=133, label='FLO')
    CLE_TEXTO = forms.IntegerField(min_value=0, max_value=6, label='CLE_TEXTO')
    CFS = forms.IntegerField(min_value=0, max_value=85, label='CFS')

    class Meta:
        model = Evaluacion_IPAL_PRIMERO
        fields = '__all__'
        exclude = ('curso_academico','prueba','mes','alumno', 'tipo', 'momento', 'riesgo', 'omnibus', 'evaluador', 'mes_leible')


class Form_Evaluacion_IPAL_SEGUNDO(forms.ModelForm):
    CNL = forms.IntegerField(min_value=0, max_value=100, label='CNL')
    LP = forms.IntegerField(min_value=0, max_value=40, label='LP')
    TM = forms.IntegerField(min_value=0, max_value=20, label='TM')
    PRO = forms.IntegerField(min_value=0, max_value=133, label='PRO')
    # tareas complementarias
    CSL_ACIERTOS =  forms.IntegerField(min_value=0, max_value=100, label='CSL ACIERTOS')
    CSL_TIEMPO =  forms.IntegerField(min_value=0, max_value=100, label='CSL TIEMPO')
    CLE_TEXTO_ACIERTOS =  forms.IntegerField(min_value=0, max_value=100, label='CLE TEXTO ACIERTOS')
    CLE_TEXTO_TIEMPO =  forms.IntegerField(min_value=0, max_value=100, label='CLE TEXTO TIEMPO')
    CFS_ACIERTOS =  forms.IntegerField(min_value=0, max_value=100, label='CFS ACIERTOS')
    CFS_TIEMPO =  forms.IntegerField(min_value=0, max_value=100, label='CFS TIEMPO')
    VOC_ACIERTOS =  forms.IntegerField(min_value=0, max_value=100, label='VOC ACIERTOS')
    VOC_TIEMPO =  forms.IntegerField(min_value=0, max_value=100, label='VOC TIEMPO')

    class Meta:
        model = Evaluacion_IPAL_SEGUNDO
        fields = '__all__'
        # la prueba IPAL segundo tiene una serie de subpruebas complementarias
        # con puntuaciones directas que el programa debe calcular:
        # CSL, CLE_TEXTO, CFS, VOC
        exclude = ('curso_academico','mes','prueba','alumno', 'tipo', 'momento', 'riesgo', 'omnibus',
                   'evaluador', 'observaciones', 'mes_leible',
                   'CSL', 'CLE_TEXTO', 'CFS', 'VOC',)

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



# formulario para editar y crear nuevo alumno,
# en el que el grupo esta forzado
class FormAlumnoGrupoForzado(forms.ModelForm):

    fecha_nacimiento = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y'),
                                       input_formats=('%d/%m/%Y',))

    class Meta:
        model = Alumno
        fields = ('codigo', 'sexo', 'fecha_nacimiento', 'pais')



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



# formulario para evaluadores
class FormEvaluador(forms.ModelForm):
    class Meta:
        model = Evaluador
        fields = '__all__'
        exclude = ('usuario', 'informacion_adicional_completa', 'centro_pilotaje')
