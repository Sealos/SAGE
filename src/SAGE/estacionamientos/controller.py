# Archivo con funciones de control para SAGE


# Las Tuplas de cada puesto deben tener los horarios de inicio y de cierre para que
# pueda funcionar [(7:00,7:00), (19:00,19:00)]


# Suponiendo que cada estacionamiento tiene una estructura "matricial" lista de listas
# donde si m es una matriz, m[i,j] las i corresponden a los puestos y las j corresponden a tuplas
# con el horario inicio y fin de las reservas
# [[(horaIn,horaOut),(horaIn,horaOut)],[],....]

# chequeo de horarios de extended
def HorarioEstacionamiento(HoraInicio, HoraFin, ReservaInicio, ReservaFin):

	if HoraInicio >= HoraFin:
		return (False, 'El horario de apertura debe ser menor al horario de cierre')
	if ReservaInicio >= ReservaFin:
		return (False, 'El horario de inicio de reserva debe ser menor al horario de cierre')
	if ReservaInicio < HoraInicio:
		return (False, 'El horario de inicio de reserva debe mayor o igual al horario de apertuda del estacionamiento')
	if ReservaInicio > HoraFin:
		return (False, 'El horario de comienzo de reserva debe ser menor al horario de cierre del estacionamiento')
	if ReservaFin < HoraInicio:
		return (False, 'El horario de apertura de estacionamiento debe ser menor al horario de finalización de reservas')
	if ReservaFin > HoraFin:
		return (False, 'El horario de cierre de estacionamiento debe ser mayor o igual al horario de finalización de reservas')
	return (True, '')


# busca un puesta en el estacionamiento
def buscar(hin, hout, estacionamiento):
	for i in range(len(estacionamiento)):
		posicion = busquedaBin(hin, hout, estacionamiento[i])
		if posicion[1] == True:
			return (i, posicion[0], posicion[1])
	return (-1, -1, False)

def binaria(valor, inicio, fin, lista):
	if inicio == fin:
		return inicio
	centro = (inicio + fin) // 2
	if lista[centro][0] > valor:
		return binaria(valor, inicio, centro, lista)
	if lista[centro][0] < valor:
		return binaria(valor, centro + 1, fin, lista)
	return centro

def busquedaBin(hin, hout, listaTuplas):
	# ln = len(listaTuplas)
	index = binaria(hin, 0, len(listaTuplas), listaTuplas)
	if index == 0:
		index = index + 1
	if listaTuplas[index][0] >= hout and listaTuplas[index - 1][1] <= hin:
		return (index, True)
	else:
		return (index, False)

# inserta ordenadamente por hora de inicio
def insertarReserva(hin, hout, puesto, listaReserva):
	# no verifica precondicion, se supone que se hace buscar antes para ver si se puede agregar
	tupla = (hin, hout)
	listaReserva.insert(puesto, tupla)
	# estacionamiento[puesto].sort()
	return listaReserva

def reservar(hin, hout, estacionamiento):
	puesto = buscar(hin, hout, estacionamiento)
	if puesto[2] != False:
		estacionamiento[puesto[0]] = insertarReserva(hin, hout, puesto[1], estacionamiento[puesto[0]])
		return estacionamiento
	else:
		return 1


def validarHorarioReserva(ReservaInicio, ReservaFin, HorarioApertura, HorarioCierre):

	if ReservaInicio >= ReservaFin:
		return (False, 'El horario de apertura debe ser menor al horario de cierre')
	if ReservaFin.hour - ReservaInicio.hour < 1:
		return (False, 'El tiempo de reserva debe ser al menos de 1 hora')
	if ReservaFin > HorarioCierre:
		return (False, 'El horario de inicio de reserva debe estar en un horario válido')
	if ReservaInicio < HorarioApertura:
		return (False, 'El horario de cierre de reserva debe estar en un horario válido')
	return (True, '')

