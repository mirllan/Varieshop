from django import forms

#clases
#creacion de formularios
class RegistrarUsuarios(forms.Form):
    
    #la palabra filed es usada ara poder poner el tipo de dato
    #lo que se guarda dentro de los parentecis es para dar los parametros del campo
    nombres = forms.CharField(max_length=30,required=True,label='Nombres del usuario', help_text='Ingrese los nombres del usuarios')
    apellidos = forms.CharField(max_length=30,required=True,label='Apellidos del usuario', help_text='Ingrese sus Apellidos')
    fecha_nacimiento = forms.DateField(label='fecha de nacimiento',required=True,help_text='ingrese su fecha de nacimiento')
    telefono = forms.IntegerField(max_length=30,label='telefono del usuario',required=True, help_text='ingrese su numero de celular')
    contrasenia = forms.PasswordInput(max_length=30,required=True,label='Contraseña del usuario', help_text='Ingrese su contraseña')
    