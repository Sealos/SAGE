# -*- coding: utf-8 -*-

from django.shortcuts import render
from estacionamientos.forms import EstacionamientoForm
from estacionamientos.forms import EstacionamientoExtendedForm
from estacionamientos.forms import EstacionamientoReserva
from estacionamientos.models import *
from estacionamientos.controller import *

listaReserva = []

def estacionamientos_all(request):
    global listaReserva
    listaReserva = []
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
    else:
        form = EstacionamientoForm()
    return render(request, 'base.html', {'form': form, 'estacionamientos': Estacionamiento.objects.all()})

def estacionamiento_detail(request, _id):
    _id = int(_id)
    estacion = Estacionamiento.objects.get(id=_id)
    global listaReserva
    listaReserva = []
    if request.method == 'GET':
        # Mayor al numero que hay
        if len(Estacionamiento.objects.filter(id = _id)) < 1 :
            return render(request, '404.html')
        else:
            form = EstacionamientoExtendedForm()
            return render(request, 'estacionamiento.html', {'form': form, 'estacionamiento': estacion})

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

                estacion.Tarifa = form.cleaned_data['tarifa']
                estacion.Apertura = hora_in
                estacion.Cierre = hora_out 
                estacion.Reservas_Inicio = reserva_in
                estacion.Reservas_Cierre = reserva_out
                estacion.NroPuesto = form.cleaned_data['puestos']

                estacion.save()

                
#                i = 0
#                while i < obj.NroPuesto :
#                    puesto = PuestosModel(estacionamiento = obj)
#                    puesto.save()
#                    i = i+1 
    else:
        form = EstacionamientoExtendedForm()

    return render(request, 'estacionamiento.html', {'form': form, 'estacionamiento': estacion})



def estacionamiento_reserva(request, _id):
    _id = int(_id)
    global listaReserva

    estacion = Estacionamiento.objects.get(id=_id)

    if len(listaReserva) < 1:

        Puestos = ReservasModel.objects.filter(Estacionamiento = estacion).values_list('Puesto','InicioReserva','FinalReserva')
        elem1 = (estacion.Apertura,estacion.Apertura)
        elem2 = (estacion.Cierre,estacion.Cierre)
        listaReserva = [[elem1, elem2] for _ in range(estacion.NroPuesto)]
        print listaReserva

        for obj in Puestos:
            puesto = busquedaBin(obj[1],obj[2],listaReserva[obj[0]])
            listaReserva[obj[0]] = insertarReserva(obj[1],obj[2],puesto[0],listaReserva[obj[0]])
        print listaReserva


    if request.method == 'GET':
        # Mayor al numero que hay
        if len(Estacionamiento.objects.filter(id = _id)) < 1:
            return render(request, '404.html')
        else:
            form = EstacionamientoReserva()
            return render(request, 'estacionamientoReserva.html', {'form': form, 'estacionamiento': estacion} )

    elif request.method == 'POST':
            form = EstacionamientoReserva(request.POST)
            if form.is_valid():
                inicio_reserva = form.cleaned_data['inicio']
                final_reserva = form.cleaned_data['final']

                Validado = HorarioReserva(inicio_reserva,final_reserva,estacion.Apertura,estacion.Cierre)

                if not Validado[0]:
                    return render(request, Validado[1])
                
                x = buscar(inicio_reserva,final_reserva,listaReserva)
                if x[2] == True :
                    reservar(inicio_reserva,final_reserva,listaReserva)
                    reservaFinal = ReservasModel(
                                        Estacionamiento = estacion,
                                        Puesto = x[0],
                                        InicioReserva = inicio_reserva,
                                        FinalReserva = final_reserva
                                    )
                    reservaFinal.save()
                    return render(request, 'reservaDisponible.html')
                else:
                    #TEFYYY
                    return render(request, 'reservaNoDisponible.html')
    else:
        form = EstacionamientoReserva()

    return render(request, 'estacionamientoReserva.html', {'form': form, 'estacionamiento': estacion})

