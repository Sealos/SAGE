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
		return (False,'horarioAperturaMayor.html')
	if ReservaInicio >= ReservaFin:
		return (False,'horarioReservaMayor.html')
	if ReservaInicio > HoraFin:
		return (False, 'horarioReservaInvalido.html')
	if ReservaFin < HoraInicio or ReservaFin > HoraFin:
		return (False, 'horarioReservaInvalido2.html')
	return (True,'')


# busca un puesta en el estacionamiento
def buscar(hin,hout,estacionamiento):
	for i in range(len(estacionamiento)):
		posicion = busquedaBin(hin,hout,estacionamiento[i])
		if posicion[1] == True:
			return (i,posicion[0],posicion[1])
	return (-1,-1,False)
		
def binaria(valor,inicio,fin,lista):
	if inicio==fin:
		return inicio
	centro = (inicio + fin) // 2
	if lista[centro][0] > valor:
		return binaria(valor,inicio,centro,lista)
	if lista[centro][0] < valor:
		return binaria(valor,centro+1,fin,lista)
	return centro

def busquedaBin(hin,hout,listaTuplas):
	#ln = len(listaTuplas)
	index = binaria(hin,0,len(listaTuplas),listaTuplas)
	if listaTuplas[index][0] > hout and listaTuplas[index-1][1] < hin:
		return (index, True)
	else:
		return (index, False)
	
	
# inserta ordenadamente por hora de inicio
def insertarReserva(hin,hout,puesto,listaReserva):
	# no verifica precondicion, se supone que se hace buscar antes para ver si se puede agregar
	tupla = (hin,hout)
	listaReserva.insert(puesto,tupla)
	#estacionamiento[puesto].sort()
	return listaReserva
			
def reservar(hin,hout,estacionamiento):
	puesto = buscar(hin,hout,estacionamiento)
	if puesto[2] != False:
		estacionamiento[puesto[0]]=insertarReserva(hin,hout,puesto[1],estacionamiento[puesto[0]])
		return estacionamiento
	else:
		return 1


#print busquedaBin(3,4,[(0,1),(1,1),(3,4),(4,5)])	
#hin = '13:00'
#hout = '17:00'
#l = [[('16:00','18:00'),('19:00','20:00')]]

#reservar(hin,hout,l)
#l.sort()
