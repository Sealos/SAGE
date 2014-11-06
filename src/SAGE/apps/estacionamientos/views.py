from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from apps.estacionamientos.forms import EstacionamientoForm
from apps.estacionamientos.forms import EstacionamientoExtendedForm

estacionamientos = []

def estacionamientos_all(request):
    if request.method == 'POST':
            form = EstacionamientoForm(request.POST)
            if form.is_valid():
                if len(estacionamientos) >= 5:
                    return HttpResponse('No se pueden agregar mas estacionamientos')
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
                estacionamientos[_id]['tarifa'] = form.cleaned_data['tarifa']
                estacionamientos[_id]['horarioin'] = form.cleaned_data['horarioin']
                estacionamientos[_id]['horarioout'] = form.cleaned_data['horarioout']
                estacionamientos[_id]['horario_reserin'] = form.cleaned_data['horario_reserin']
                estacionamientos[_id]['horario_reserout'] = form.cleaned_data['horario_reserout']
                estacionamientos[_id]['puestos'] = form.cleaned_data['puestos']
                return render(request, 'estacionamiento_extend.html', {'estacionamiento': estacionamientos[_id]})

            else:
                return HttpResponse('No')
    else:
        form = EstacionamientoExtendedForm()

    return render(request, 'estacionamiento.html', {'form': form, 'estacionamiento': estacionamientos[_id]})

