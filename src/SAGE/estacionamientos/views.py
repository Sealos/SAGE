# -*- coding: utf-8 -*-

from django.shortcuts import render
from estacionamientos.forms import EstacionamientoForm
from estacionamientos.forms import EstacionamientoExtendedForm
from estacionamientos.forms import EstacionamientoReserva
from estacionamientos.models import *
from estacionamientos.controller import buscar, reservar, HorarioEstacionamiento, HorarioReserva

def estacionamientos_all(request):
    if request.method == 'POST':
            form = EstacionamientoForm(request.POST)
            if form.is_valid():
                if len(Estacionamiento.objects.all()) >= 5:
                    return render(request, 'estacionamientoLlen.html')
                
                obj = Estacionamiento(
                        Propietario = form.cleaned_data['propietario'], 
                        Nombre = form.cleaned_data['nombre'],
                        Direccion = form.cleaned_data['direccion'], 
                        Rif = form.cleaned_data['rif'], 
                        Telefono_1 = form.cleaned_data['telefono_1'],
                        Telefono_2 = form.cleaned_data['telefono_2'], 
                        Telefono_3 = form.cleaned_data['telefono_3'], 
                        Email_1 = form.cleaned_data['email_1'], 
                        Email_2 = form.cleaned_data['email_2']
                )
                obj.save()
                print obj.id
    else:
        form = EstacionamientoForm()
    return render(request, 'base.html', {'form': form, 'estacionamientos': Estacionamiento.objects.all()})

def estacionamiento_detail(request, _id):
    _id = int(_id)
    estacion = Estacionamiento.objects.get(id=_id)
    if request.method == 'GET':
        # Mayor al numero que hay
        if len(Estacionamiento.objects.filter(id = _id)) < 1 :
            return render(request, '404.html')
        else:
            form = EstacionamientoExtendedForm()
            if len(ExtendedModel.objects.filter(Estacionamiento = estacion))>0 :
                return render(request, 'estacionamiento.html', {'form': form, 'estacionamiento': estacion, 
                    'estacionamiento2': ExtendedModel.objects.get(Estacionamiento = estacion)})
            else:
                return render(request, 'estacionamiento.html', {'form': form, 'estacionamiento': estacion, 
                    'estacionamiento2': None})

    elif request.method == 'POST':
            form = EstacionamientoExtendedForm(request.POST)
            if form.is_valid():
                hora_in = form.cleaned_data['horarioin']
                hora_out = form.cleaned_data['horarioout']
                reserva_in = form.cleaned_data['horario_reserin']
                reserva_out = form.cleaned_data['horario_reserout']


                x = HorarioEstacionamiento(hora_in,hora_out,reserva_in,reserva_out)
                if not x[0]:
                    return render(request, x[1])
                if len(ExtendedModel.objects.filter(Estacionamiento = estacion))>0 :

                    obj = ExtendedModel.objects.get(Estacionamiento = estacion)
                    obj.Estacionamiento = estacion 
                    obj.Tarifa = form.cleaned_data['tarifa']
                    obj.Apertura = form.cleaned_data['horarioin'] 
                    obj.Cierre = form.cleaned_data['horarioout'] 
                    obj.Reservas_Inicio = form.cleaned_data['horario_reserin']
                    obj.Reservas_Cierre = form.cleaned_data['horario_reserout'] 
                    obj.NroPuesto = form.cleaned_data['puestos']
                    
                else:
                    obj = ExtendedModel(
                            Estacionamiento = estacion, 
                            Tarifa = form.cleaned_data['tarifa'],
                            Apertura = form.cleaned_data['horarioin'], 
                            Cierre = form.cleaned_data['horarioout'], 
                            Reservas_Inicio = form.cleaned_data['horario_reserin'],
                            Reservas_Cierre = form.cleaned_data['horario_reserout'], 
                            NroPuesto = form.cleaned_data['puestos']
                    )
                obj.save()
                if len(PuestosModel.objects.filter(estacionamiento = obj))>0 :
                    PuestosModel.objects.filter(estacionamiento = obj).delete()
                
                i = 0
                while i < obj.NroPuesto :
                    puesto = PuestosModel(estacionamiento = obj)
                    puesto.save()
                    i = i+1 

                elem1 = (obj.Apertura,obj.Apertura)
                elem2 = (obj.Cierre,obj.Cierre)
                #estacionamientos[_id]['puestoReservas'] = [[elem1, elem2] for _ in range(estacionamientos[_id]['puestos'])]


    else:
        form = EstacionamientoExtendedForm()

    return render(request, 'estacionamiento.html', {'form': form, 'estacionamiento': estacion, 
        'estacionamiento2': ExtendedModel.objects.get(Estacionamiento = estacion)})



def estacionamiento_reserva(request, _id):
    _id = int(_id)
    listaReserva = estacionamientos[_id]['puestoReservas']

    if request.method == 'GET':
        # Mayor al numero que hay
        if len(estacionamientos) < _id + 1:
            return render(request, '404.html')
        else:
            form = EstacionamientoReserva()
            return render(request, 'estacionamientoReserva.html', {'form': form, 'estacionamiento': estacionamientos[_id]})

    elif request.method == 'POST':
            form = EstacionamientoReserva(request.POST)
            if form.is_valid():
                inicio_reserva = form.cleaned_data['inicio']
                final_reserva = form.cleaned_data['final']

                Validado = HorarioReserva(inicio_reserva,final_reserva,estacionamientos[_id]['horarioin'],estacionamientos[_id]['horarioout'])

                if not Validado[0]:
                    return render(request, Validado[1])
                
                x = buscar(inicio_reserva,final_reserva,listaReserva)
                if x[2] == True :
                    reservar(inicio_reserva,final_reserva,listaReserva)
                    return render(request, 'reservaDisponible.html')
                else:
                    #TEFYYY
                    return render(request, 'reservaNoDisponible.html')
    else:
        form = EstacionamientoReserva()

    return render(request, 'estacionamientoReserva.html', {'form': form, 'estacionamiento': estacionamientos[_id]})

