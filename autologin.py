import requests
import json
import os

def getAccessTokenEmpresaAutologin():
  idUsuario = os.environ['ID']
  ambiente = os.environ['AMBIENTE']
  usuario = os.environ['USUARIO']
  
  print idUsuario
  print ambiente

  ambientesUrl = {"bm-produccion" :  "https://api.bumeran.com" ,"zj-produccion" : "https://api.zonajobs.com.ar" , "bm-sandbox" : "https://developers.bumeran.com" ,  "bm-lite" : "http://192.168.120.212:8080", "zj-sandbox" : "https://developers.zonajobs.com"}
  
  headers = {'Content-type' : 'application/json', 'Accept' : 'application/json'}
  basepath = ambientesUrl[ambiente] + "/v0/"
  
  url = basepath + "application/oauth2/login?grant_type=client_credentials&client_id=api-developer&client_secret=secret"
  print url
  r = requests.post(url, headers = headers, verify = False)

  print r
  if(r.status_code >= 300):
    print r.status_code
    print r.json()['error_description']
    return
  accessTokenApp = r.json()['access_token']
  print accessTokenApp


  if(usuario == "Empresa"):
    print usuario
    endpointToken = basepath + "application/empresas/token?access_token=" + accessTokenApp
    usuarioId = {'usuarioId': idUsuario} 
  else:
    print usuario
    endpointToken = basepath + "application/postulantes/token?acces_token=" + accessTokenApp
    usuarioId = {"postulanteId": idUsuario} 
  print endpointToken
  r2 = requests.post(endpointToken, headers = headers, verify = False, data = json.dumps(usuarioId))

  print r2
  if(r2.status_code >= 300):
    print r2.status_code
    print r2.json()['error_description']
    return

  accessTokenAutologin = r2.json()['token']
  print accessTokenAutologin

  if(usuario == "Empresa"):
    print usuario
    endpointAutologin = basepath + "application/empresas/autologin?grant_type=autologin&client_id=api-developer&client_secret=secret&token=" + accessTokenAutologin
  else:
    endpointAutologin = basepath + "application/postulantes/autologin?grant_type=autologin&client_id=api-developer&client_secret=secret&token=" + accessTokenAutologin
  
  print endpointAutologin
  r3 = requests.post(endpointAutologin, headers = headers, verify = False)

  print r3
  if(r3.status_code >= 300):
    print r3.status_code
    print r3.json()['error_description']
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
