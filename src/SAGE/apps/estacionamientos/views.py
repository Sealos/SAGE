from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from apps.estacionamientos.forms import EstacionamientoForm

estacionamientos = []

def estacionamientos_all(request):
    if request.method == 'POST':
            form = EstacionamientoForm(request.POST)
            if form.is_valid():
                if len(estacionamientos) >= 5:
                    return HttpResponse('No se pueden agregar mas estacionamientos')
                estacionamiento = {
                        'patrono': form.cleaned_data['patrono'],
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
    if len(estacionamientos) < _id + 1:
        return render(request, 'base.html')
    else:
        return render(request, 'estacionamiento.html', {'estacionamiento': estacionamientos[_id]})
