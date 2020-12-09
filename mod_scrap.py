#CODIGO PARA DESCARGAAR IMAGENES DE PAGINA WEB Y EL WHOIS
def mod_scrap():
	import requests
	from bs4 import BeautifulSoup as bs
	import os
	import re
	import whois
	from main import dom

	#crea la directorio "images" donde se guardarán los archivos descargados de la página web
	try:
		os.system("mkdir images")
	except OSError as e:
		if e.errno != errno.EEXIST:
			raise

	#desde main se importa la variable "dom" la cual tiene la información del argumento -s
	page = requests.get(dom)
	soup = bs(page.content, "lxml")

	#busca los archivos img
	imagenes = soup.findAll('img')
	direcciones = []
	for imagen in imagenes:
	    try:
	        direcciones.append(imagen['src'])
	        imagenes = [x for x in direcciones if x.endswith('.jpg')]
	    except KeyError:
	        pass

	#ciclo que guarda los archivos .jpg en la carpeta anteriormente creada "images"
	j = 1
	for x in imagenes:
	    with open('images/%s'%x.split('/')[-1]+'.png', "wb") as f:
	        page = requests.get(x)
	        f.write(page.content)
	    j = j+1

	#función para eliminar espacios de un string
	def eliminaespacios(frase):
		frase = frase.strip()
		count = 0
		while True:
			spa = "  "
			for i in range (20):
				frase = frase.replace (spa, " ")
				spa +=" "
			count +=1
			if count == 10:
				break
			return frase

	#extraemos la información del dominio com la variable "dom"
	#la cual guarda como lista pero la guardamos como string en la variables "ip"
	#para después escribirla en un archivo.txt
	domain_info = whois.whois(dom)
	ip_list = (domain_info.name_servers)
	ip =  " ".join([str(elem) for elem in ip_list])
	ip = eliminaespacios(ip)
	f =  open("ip.txt", "w")
	f.write(ip)
	f.close()
