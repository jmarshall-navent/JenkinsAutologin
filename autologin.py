import requests
import json
import os

def getAccessTokenEmpresaAutologin():
  idUsuario = os.environ['ID']
  ambiente = os.environ['AMBIENTE']
  usuario = os.environ['USUARIO']
  clientSecret = os.environ['CLIENT_SECRET']
  clientId = os.environ['CLIENT_ID']
  
  print idUsuario
  print ambiente
  print usuario
  print clientSecret
  print clientId

  ambientesUrl = {}
  
  headers = {'Content-type' : 'application/json', 'Accept' : 'application/json'}
  basepath = ambientesUrl[ambiente] + "/v0/"
  
  url = basepath + "application/oauth2/login?grant_type=client_credentials&client_id=" + clientId + "&client_secret=" + clientSecret
  r = requests.post(url, headers = headers, verify = False)

  if(r.status_code >= 300):
    print r.status_code
    print r.json()['error_description']
    return
  accessTokenApp = r.json()['access_token']


  if(usuario == "Empresa"):
    endpointToken = basepath + "application/empresas/token?access_token=" + accessTokenApp
    usuarioId = {'usuarioId': idUsuario} 
  else:
    endpointToken = basepath + "application/postulantes/token?access_token=" + accessTokenApp
    usuarioId = {"postulanteId": idUsuario} 
  r2 = requests.post(endpointToken, headers = headers, verify = False, data = json.dumps(usuarioId))

  if(r2.status_code >= 300):
    print r2.status_code
    print r2.json()['error_description']
    return

  accessTokenAutologin = r2.json()['token']

  if(usuario == "Empresa"):
    endpointAutologin = basepath + "application/empresas/autologin?grant_type=autologin&client_id=" + clientId + "&client_secret=" + clientSecret + "&token=" + accessTokenAutologin
  else:
    endpointAutologin = basepath + "application/postulantes/autologin?grant_type=autologin&client_id=" + clientId + "&client_secret=" + clientSecret + "&token=" + accessTokenAutologin
  
  r3 = requests.post(endpointAutologin, headers = headers, verify = False)

  if(r3.status_code >= 300):
    print r3.status_code
    print r3.json()['error_description']
    return
    
  token = r3.json()['access_token']
  print '\n \n \n '
  if(usuario == "Empresa"):
    print "acces_token para la empresa con id: " + idUsuario + " y ambiente: " + ambiente
  else:
    print "access_token para el postulante con id: " + idUsuario + " y ambiente: " + ambiente
  print '\n '
  print token
  print '\n '
  print '\n '
