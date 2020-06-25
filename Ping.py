import subprocess

dominio = input("Ingrese un dominio: ")

p = subprocess.run(['ping', dominio],  capture_output = True, encoding = 'cp850' )

resultado = p.stdout.strip()

index_IP = resultado.find('[')

index_end = resultado.find(']')

resultado = resultado[(index_IP + 1):index_end]

print('Su IP es : {}'.format(resultado))

print("Su IP es: {}".format(resultado))
