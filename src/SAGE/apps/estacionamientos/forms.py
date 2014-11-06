from django import forms
from django.core.validators import RegexValidator


class EstacionamientoForm(forms.Form):

    phone_validator = RegexValidator(
                            regex='^(\d)+',
                            message='Solo debe contener digitos'
                        )

    # nombre del dueno (no se permiten digitos)
    propietario = forms.CharField(
                    required=True,
                    label="Propietario",
                    validators = [
                          RegexValidator(
                                regex='^[a-zA-z]+( [a-zA-z]+)?$',
                                message='Solo debe contener letras'
                        )
                    ]
                )

    nombre = forms.CharField(required=True, label="Nombre")

    direccion = forms.CharField(required=True)

    telefono_1 = forms.CharField(required=False, validators = [phone_validator])
    telefono_2 = forms.CharField(required=False, validators = [phone_validator])
    telefono_3 = forms.CharField(required=False, validators = [phone_validator])

    email_1 = forms.EmailField(required=False)
    email_2 = forms.EmailField(required=False)

    rif = forms.CharField(
                    required=True,
                    label="RIF",
                    validators = [
                          RegexValidator(
                                regex='^[JV]-?\d{8}-?\d$',
                                message='Introduzca un rif con un formato válido'
                        )
                    ]
                )


class EstacionamientoExtendedForm(forms.Form):


    puestos = forms.IntegerField(min_value=0, label='Número de puestos')

    tarifa_validator = RegexValidator(
                            regex='^[0-9]+$',
                            message='Solo debe contener digitos'
                        )

    horarioin = forms.TimeField(required = True)
    horarioout = forms.TimeField(required = True)

    horario_reserin = forms.TimeField(required = True)
    horario_reserout = forms.TimeField(required = True)

    tarifa =  forms.CharField(required = True, validators = [tarifa_validator])
