import argparse
import mod_scrap
import mod_email
import subprocess

#documentación para parser con argumento -h y su funcionamiento
parser = argparse.ArgumentParser(
     prog='PROG',
     description='''Modo de uso: Con el argumento -s introducirá la página web a la cual
                    se le correrá un script de web scrapping y whois, con el argumento -e
                    introducirá el encabezado del correo del cual mandará de manera automatica.''',
     epilog= '''Autores: Heissel Mendez, Luis Lopez, Diego Vitela
            ''')
parser.add_argument('-s', help='Argumento que toma la dirección del sitio web completo (http://www.ejemplo.com)')
parser.add_argument('-e', help='Argumento que toma el encabezado del correo')
params = parser.parse_args()

#variables que guardan la información obtenida de los arugmentos
dom = params.s
enc = params.e

#función main que corre el suite
def main():
    #manda a llamar el script mod_scrap y corre su función mod_scrap
    mod_scrap.mod_scrap()
    #para la siguiente linea se requiere que de manera manual anote la dirección en donde sé encuentra el script ps1
    p = subprocess.Popen(["powershell",r"C:\Users\user32\Desktop\metadata.ps1"], stdout=subprocess.PIPE)
    print(p.communicate)
    #manda a llamar el script mod_email y corre su función mod_email
    mod_email.mod_email()

if __name__ == "__main__":
    main()
