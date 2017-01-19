import requests
import json


headers = {'Content-type' : 'application/json', 'Accept' : 'application/json'}

endpoint = "https://developers.zonajobs.com/v0/application/oauth2/login"
url = "https://developers.zonajobs.com/v0/application/oauth2/login?grant_type=client_credentials&client_id=api-developer&client_secret=secret"
r = requests.post(url, headers = headers, verify = False)



accessTokenApp = r.json()['access_token']



endpointEmpresasToken = "https://developers.zonajobs.com/v0/application/empresas/token?access_token=" + accessTokenApp
usuario = {'usuarioId': 543287} 

r2 = requests.post(endpointEmpresasToken, headers = headers, verify = False, data = json.dumps(usuario))



accesTokenAutologin = r2.json()['token']



endpointEmpresasAutologin = "https://developers.zonajobs.com/v0/application/empresas/autologin?grant_type=autologin&client_id=api-developer&client_secret=secret&token=" + accesTokenAutologin

r3 = requests.post(endpointEmpresasAutologin, headers = headers, verify = False)

empresaToken = r3.json()['access_token']
print empresaToken
