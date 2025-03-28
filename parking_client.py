# Instalar el módulo requests haciendo desde una terminal: pip install requests
import requests


# Función para registrar usuario
def registerUser(url,id,password,program,role):    
    response=requests.post(url+'/register',data=f'id={id}&password={password}&program={program}&role={role}')
    return response.content.decode('utf-8')



# Función para obtener el código QR
def getQR(url,id,password):    
    response=requests.get(url+'/getqr',data=f'id={id}&password={password}')
    return response.content

# Función para enviar el código QR y así permitir el ingreso
def sendQR(url,qr_image):
    headers = {'Content-type': 'image/png', 'Slug': qr_image}
    response = requests.post(url+"/sendqr", data=open(qr_image, 'rb'), headers=headers)    
    return response.content



