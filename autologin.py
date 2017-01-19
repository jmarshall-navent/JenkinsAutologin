import requests


headers = {'Content-type' : 'application/json', 'Accept' : 'application/json'}

endpoint = "https://developers.zonajobs.com/v0/application/oauth2/login"
url = "https://developers.zonajobs.com/v0/application/oauth2/login?grant_type=client_credentials&client_id=api-developer&client_secret=secret"
r = requests.post(url, headers = headers, verify = False)

print r
print r.json()

accessTokenApp = r.json()['access_token']
print accessTokenApp


endpointEmpresasToken = "https://developers.zonajobs.com/v0/application/empresas/token?access_token=" + accessTokenApp


r2 = requests.post(endpointEmpresasToken, headers = headers, verify = False, {'usuarioId': 543287} )
print r2
print r2.json()
