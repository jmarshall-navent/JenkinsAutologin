import requests
import json
import os

def getAccessTokenEmpresaAutologin():
  idUsuario = os.environ['ID']
  ambiente = os.environ['AMBIENTE']
  usuario = os.environ['USUARIO']
  
  print idUsuario
  print ambiente
  print usuario

  ambientesUrl = {"bm-produccion" :  "https://api.bumeran.com" ,"zj-produccion" : "https://api.zonajobs.com.ar" , "bm-sandbox" : "https://developers.bumeran.com" ,  "bm-lite" : "http://192.168.120.212:8080", "zj-sandbox" : "https://developers.zonajobs.com"}
  
  headers = {'Content-type' : 'application/json', 'Accept' : 'application/json'}
  basepath = ambientesUrl[ambiente] + "/v0/"
  
  url = basepath + "application/oauth2/login?grant_type=client_credentials&client_id=api-developer&client_secret=secret"
  print url
  r = requests.post(url, headers = headers, verify = False)

  print r
  if(r.status_code >= 300):
    print r.status_code
    return
  accessTokenApp = r.json()['access_token']


  if(usuario == "Empresa"):
    endpointToken = basepath + "application/empresas/token?access_token=" + accessTokenApp
  else:
    endpointToken = basepath + "application/postulantes/token?acces_token" + accessTokenApp
  usuario = {'usuarioId': idUsuario} 
  print endpointToken
  r2 = requests.post(endpointToken, headers = headers, verify = False, data = json.dumps(usuario))

  print r2
  if(r2.status_code >= 300):
    print r2.status_code
    return

  accesTokenAutologin = r2.json()['token']


  if(usuario == "Empresa"):
    endpointAutologin = basepath + "application/empresas/autologin?grant_type=autologin&client_id=api-developer&client_secret=secret&token=" + accesTokenAutologin
  else:
    endpointAutologin = basepath + "application/postulantes/autologin?grant_type=autologin&client_id=api-developer&client_secret=secret&token=" + accesTokenAutologin
  
  r3 = requests.post(endpointAutologin, headers = headers, verify = False)

  print r3
  if(r3.status_code >= 300):
    print r3.status_code
    return
    
  token = r3.json()['access_token']
  print '\n \n \n '
  if(usuario == "Empresa"):
    print "acces_token para la empresa con id: " + idUsuario + " y ambiente: " + ambiente
  else:
    print "access_token para el postulante con id: " + idUsuario + " y ambeinte: " + ambiente
  print '\n '
  print token
  print '\n '
  print '\n '
