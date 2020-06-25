import subprocess

while True:
	try:
		memoria_input = int(input("Ingrese el limite de memoria <en KB>: "))
	except ValueError:
		print("No engresaste un numero.")
	else:
		p = subprocess.run('tasklist',  capture_output = True, encoding = 'cp850' )
		resultados = p.stdout.strip()
		resultados = resultados.split('\n')
		resultados = resultados[2:]
		
		d = []
		for resultado in resultados:
			lista_resultados = []
			lista_temp = []
			resultado = resultado.split('  ')
			lista_resultados.append(resultado[0] + " , " + resultado[-1][:-2])
			lista_resultados = lista_resultados[0].split(' , ')
			lista_resultados[1] = lista_resultados[1].replace(',', '')
			lista_resultados[1] = lista_resultados[1].strip()
			if lista_resultados[1] != 'N':
				lista_temp.append(lista_resultados[0])
				lista_temp.append(int(lista_resultados[1]))
			if len(lista_temp) >= 2:
				if lista_temp[1] >= memoria_input:
					d.append(lista_temp)
									
		for element in d:
			print("{} está usando {} KB de memoria.".format(element[0], element[1]))
			
	break
