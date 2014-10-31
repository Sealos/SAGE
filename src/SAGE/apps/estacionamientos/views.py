from django.shortcuts import render_to_response, render
from django.http import HttpResponse
from apps.estacionamientos.forms import EstacionamientoForm

estacionamientos = []

def estacionamientos_all(request):
    if request.method == 'POST':
            form = EstacionamientoForm(request.POST)
            if form.is_valid():
                estacionamiento = {
                        'patrono': form.cleaned_data.get('patrono', ''),
                        'nombre': form.cleaned_data.get('nombre', ''),
                        'direccion': form.cleaned_data.get('direccion', ''),
                        'telefono_1': form.cleaned_data.get('telefono_1', ''),
                        'telefono_2': form.cleaned_data.get('telefono_2', ''),
                        'telefono_3': form.cleaned_data.get('telefono_3', ''),
                        'email_1': form.cleaned_data.get('email_1', ''),
                        'email_2': form.cleaned_data.get('email_2', ''),
                        'rif': form.cleaned_data.get('rif', ''),
                }
                estacionamientos.append(estacionamiento)
                return HttpResponse(estacionamiento)
            else:
                return HttpResponse('No')
    else:
        form = EstacionamientoForm()
    return render(request, 'base.html', {'form': form, 'estacionamientos': estacionamientos})

def estacionamiento_detail(request, _id):
    _id = int(_id)
    if len(estacionamientos) < _id + 1:
        return render(request, 'base.html')
    else:
        return render(request, 'estacionamiento.html', {'estacionamiento': estacionamientos[_id]})
