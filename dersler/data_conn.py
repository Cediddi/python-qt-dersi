import json
from urllib import request
url = "http://51.15.221.223:8080/"

def mesaj_gonder(isim, mesaj):
    data = json.dumps({"message":mesaj, "sender":isim}).encode()
    rq = request.Request(url, data, headers={'content-type': 'application/json'})
    response = request.urlopen(rq)
    return json.loads(response.read().decode())

def mesaj_al():
    return json.loads(request.urlopen(url).read().decode())
