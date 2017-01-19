import requests
import json
import os

def getAccessTokenEmpresaAutologin( ):
  idEmpresa = os.environ['ID_EMPRESA']
  ambiente = os.envirot['AMBIENTE']
  
  ambientesUrl = {"bm-qa" :  "apiqa.navent.com" , "bm-sandbox" : "https://developers.bumeran.com" ,  "bm-lite" : "192.168.120.212:8080", "zj-sandbox" : "https://developers.zonajobs.com"}
  
  headers = {'Content-type' : 'application/json', 'Accept' : 'application/json'}
  basepath = ambientesUrl[ambeinte] + "/v0/"
  
  url = basepath + "application/oauth2/login?grant_type=client_credentials&client_id=api-developer&client_secret=secret"
  r = requests.post(url, headers = headers, verify = False)



  accessTokenApp = r.json()['access_token']



  endpointEmpresasToken = basepath + "application/empresas/token?access_token=" + accessTokenApp
  usuario = {'usuarioId': idEmpresa} 

  r2 = requests.post(endpointEmpresasToken, headers = headers, verify = False, data = json.dumps(usuario))



  accesTokenAutologin = r2.json()['token']



  endpointEmpresasAutologin = basepath + "application/empresas/autologin?grant_type=autologin&client_id=api-developer&client_secret=secret&token=" + accesTokenAutologin

  r3 = requests.post(endpointEmpresasAutologin, headers = headers, verify = False)

  empresaToken = r3.json()['access_token']
  print '\n \n \n '
  print "acces_token para la empresa con id: " + idEmpresa + " y portal: " + portal
  print '\n '
  print empresaToken
  print '\n '
  print '\n '
