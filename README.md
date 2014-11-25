SAGE
====

	Para correr el Proyecto usando el terminal de comandos y un Sistema Operativo basado en 
	 Unix,debe serguir las siguientes instrucciones:
		1) Debe tener instalado python3 en su maquina, al igual que pip y easy_install-3.4.
			de igual manera habler instalado django con easy_install-3.4
		2) Debe situarse en la carpeta SAGE dentro de la carpeta src que se encuentra dentro 
			de la caperta SAGE 		/SAGE/src/SAGE/
		3) Debe migrar los modelos de la base de datos escribiendo en la terminal de comandos
			python3 manage.py syncdb
		4) Debe correr el servidor escribiendo en el terminal de comandos
			python3 manage.py runserver
		5) Proceda a abrir en su buscador web de prefencia la siguiente direccion:
			localhost:8000/estacionamientos/
			
	Para borrar la base de datos, debe eliminar en su repositorio local el archivo llamado
		'sage_development' situado en /SAGE/src/SAGE, y luego situado en esta misma direccion
		en su terminal de comandos ingresar python3 manage.py migrate

