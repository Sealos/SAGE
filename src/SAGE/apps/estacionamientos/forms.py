from django import forms
from django.core.validators import RegexValidator


class EstacionamientoForm(forms.Form):

    phone_validator = RegexValidator(
                            regex='^[0-9]+$',
                            message='Solo debe contener digitos'
                        )

    # nombre del dueño (no se permiten dígitos)
    patrono = forms.CharField(
                    required=True,
                    validators = [
                          RegexValidator(
                                regex='^[a-zA-z]+$',
                                message='Solo debe contener letras'
                        )
                    ]
                )

    nombre = forms.CharField(required=True)

    direccion = forms.CharField(required=True)

    telefono_1 = forms.CharField(required=False, validators = [phone_validator])
    telefono_2 = forms.CharField(required=False, validators = [phone_validator])
    telefono_3 = forms.CharField(required=False, validators = [phone_validator])

    email_1 = forms.EmailField(required=False)
    email_2 = forms.EmailField(required=False)

    rif = forms.CharField(required=True)
