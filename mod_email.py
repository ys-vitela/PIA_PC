def mod_email():
        import yagmail
        from main import enc
        import socket
        import re

        #con el archivo tct creado en el script mod_scrap, lo abrimos y lo sometemos a un regex
        #para solo pasar a la variable "host" un string que es solamente la ip
        f = open('ip.txt','r')
        for i in f:
                li = re.findall(r"(\w{3}\d)\.(\w{4})\.(\w{2})(\s+)(\d+)?.(\d+)?.(\d+)?.(\d+)",i)
        for value in li:
                host = (f'{value[4]}.{value[5]}.{value[6]}.{value[7]}')
        f.close()

        #abrimos un socket para hacer un escaneo de puerto con la variable "host"
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        begin=78
        end= 80
        #creamos un archivo txt el cual nos guarda la información sobre el estado de los puertos del 79-80
        arch=open('info_puerto_escaneado.txt','w')
        for i in range(begin,end):
                result = sock.connect_ex((host,i))
                z = ("puerto", i, "cerrado \n")
                ip =  " ".join([str(elem) for elem in z])
                arch.write(ip)
                if result == 0:
                        t = ("El puerto:" , i, "Esta abierto \n")
                        pn =  " ".join([str(elem) for elem in t])
                        arch.write(pn)
        arch.close()

        #mandamos un email con la variable "enc" la cual contiene la innformación del argumento -e
        sender_email = 'test.pc.fcfm@gmail.com'
        receiver_email = 'heissel12@hotmail.com'

        subject = 'Documento con ip disponible'
        doc= 'info_puerto_escaneado.txt'

        sender_password = "fcfm.123"

        yag = yagmail.SMTP(user=sender_email, password=sender_password)

        contents = 'Te anexo un documento txt con la verificacion si la ip se encuentra levantada'

        yag.send(to=receiver_email, subject=enc, contents=contents, attachments=doc)
