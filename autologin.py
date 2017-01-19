import requests
import json
import os

def getAccessTokenEmpresaAutologin():
  idEmpresa = os.environ['ID_EMPRESA']
  ambiente = os.environ['AMBIENTE']
  
  print idEmpresa
  print ambiente
  
  ambientesUrl = {"bm-produccion" :  "https://api.bumeran.com" ,"zj-produccion" : "https://api.zonajobs.com.ar" , "bm-sandbox" : "https://developers.bumeran.com" ,  "bm-lite" : "http://192.168.120.212:8080", "zj-sandbox" : "https://developers.zonajobs.com"}
  
  headers = {'Content-type' : 'application/json', 'Accept' : 'application/json'}
  basepath = ambientesUrl[ambiente] + "/v0/"
  
  url = basepath + "application/oauth2/login?grant_type=client_credentials&client_id=api-developer&client_secret=secret"
  print url
  r = requests.post(url, headers = headers, verify = False)

  print r
  if(r.status_code >= 300):
    break;
  accessTokenApp = r.json()['access_token']



  endpointEmpresasToken = basepath + "application/empresas/token?access_token=" + accessTokenApp
  usuario = {'usuarioId': idEmpresa} 
  print endpointEmpresasToken
  r2 = requests.post(endpointEmpresasToken, headers = headers, verify = False, data = json.dumps(usuario))

  print r2
  if(r2.status_code >= 300):
    break;

  accesTokenAutologin = r2.json()['token']



  endpointEmpresasAutologin = basepath + "application/empresas/autologin?grant_type=autologin&client_id=api-developer&client_secret=secret&token=" + accesTokenAutologin

  r3 = requests.post(endpointEmpresasAutologin, headers = headers, verify = False)

  print r3
  if(r3.status_code >= 300):
    break;
    
  empresaToken = r3.json()['access_token']
  print '\n \n \n '
  print "acces_token para la empresa con id: " + idEmpresa + " y ambiente: " + ambiente
  print '\n '
  print empresaToken
  print '\n '
  print '\n '
