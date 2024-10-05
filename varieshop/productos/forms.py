from django import forms

#clases
#creacion de formularios
class RegistrarProducto(forms.Form):
    
    #la palabra filed es usada ara poder poner el tipo de dato
    #lo que se guarda dentro de los parentecis es para dar los parametros del campo
    nombre = forms.CharField(max_length=30,required=True,label='Nombre del producto', help_text='Ingrese el nombre del producto')
    descripcion = forms.CharField(max_length=200,label='Descrpicion del producto', help_text='Descripcion del producto')
    precio = forms.IntegerField(required=True)
    stock = forms.IntegerField(required=True)
    imagen = forms.FileField(required=True) 

