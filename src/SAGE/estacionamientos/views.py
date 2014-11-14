# -*- coding: utf-8 -*-

from django.shortcuts import render
from estacionamientos.forms import EstacionamientoForm
from estacionamientos.forms import EstacionamientoExtendedForm
from estacionamientos.forms import EstacionamientoReserva
from estacionamientos.controller import buscar, reservar, HorarioEstacionamiento

estacionamientos = []

def estacionamientos_all(request):
    if request.method == 'POST':
            form = EstacionamientoForm(request.POST)
            if form.is_valid():
                if len(estacionamientos) >= 5:
                    return render(request, 'estacionamientoLlen.html')
                estacionamiento = {
                        'propietario': form.cleaned_data['propietario'],
                        'nombre': form.cleaned_data['nombre'],
                        'direccion': form.cleaned_data['direccion'],
                        'telefono_1': form.cleaned_data['telefono_1'],
                        'telefono_2': form.cleaned_data['telefono_2'],
                        'telefono_3': form.cleaned_data['telefono_3'],
                        'email_1': form.cleaned_data['email_1'],
                        'email_2': form.cleaned_data['email_2'],
                        'rif': form.cleaned_data['rif'],
                }
                estacionamientos.append(estacionamiento)
    else:
        form = EstacionamientoForm()
    return render(request, 'base.html', {'form': form, 'estacionamientos': estacionamientos})

def estacionamiento_detail(request, _id):
    _id = int(_id)
    if request.method == 'GET':
        # Mayor al numero que hay
        if len(estacionamientos) < _id + 1:
            return render(request, '404.html')
        else:
            form = EstacionamientoExtendedForm()
            return render(request, 'estacionamiento.html', {'form': form, 'estacionamiento': estacionamientos[_id]})

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
                

                estacionamientos[_id]['tarifa'] = form.cleaned_data['tarifa']
                estacionamientos[_id]['horarioin'] = hora_in
                estacionamientos[_id]['horarioout'] = hora_out
                estacionamientos[_id]['horario_reserin'] = reserva_in
                estacionamientos[_id]['horario_reserout'] = reserva_out
                estacionamientos[_id]['puestos'] = form.cleaned_data['puestos']

                elem1 = (estacionamientos[_id]['horarioin'],estacionamientos[_id]['horarioin'])
                elem2 = (estacionamientos[_id]['horarioout'],estacionamientos[_id]['horarioout'])
                estacionamientos[_id]['puestoReservas'] = [[elem1, elem2] for _ in range(estacionamientos[_id]['puestos'])]


    else:
        form = EstacionamientoExtendedForm()

    return render(request, 'estacionamiento.html', {'form': form, 'estacionamiento': estacionamientos[_id]})



def estacionamiento_reserva(request, _id):
    _id = int(_id)
    listaReserva = estacionamientos[_id]['puestoReservas']
    print(listaReserva)

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

                if inicio_reserva >= estacionamientos[_id]['horarioout'] or final_reserva > estacionamientos[_id]['horarioout']:
                    return render(request, 'horarioReservaInvalido.html')
                if inicio_reserva >= final_reserva:
                    return render(request, 'horarioReservaMayor.html')


                if inicio_reserva < estacionamientos[_id]['horarioin'] or final_reserva <= estacionamientos[_id]['horarioin']:
                    return render(request, 'horarioReservaInvalido.html')

                #alguien
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

