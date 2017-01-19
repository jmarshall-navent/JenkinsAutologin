import requests
import json


headers = {'Content-type' : 'application/json', 'Accept' : 'application/json'}

endpoint = "https://developers.zonajobs.com/v0/application/oauth2/login"
url = "https://developers.zonajobs.com/v0/application/oauth2/login?grant_type=client_credentials&client_id=api-developer&client_secret=secret"
r = requests.post(url, headers = headers, verify = False)

print r
print r.json()

accessTokenApp = r.json()['access_token']
print accessTokenApp


endpointEmpresasToken = "https://developers.zonajobs.com/v0/application/empresas/token?access_token=" + accessTokenApp
usuario = {'usuarioId': 543287} 

r2 = requests.post(endpointEmpresasToken, headers = headers, verify = False, data = json.dumps(usuario))
print r2
print r2.json()


accesTokenAutologin = r2.json()['token']
print accessTokenAutologin
