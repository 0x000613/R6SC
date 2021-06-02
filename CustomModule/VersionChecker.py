import requests
import CustomModule.mkQuery

def versionChecker(prodname):
    URL = "https://api.xeros.dev"
    query = {"api":"vc", "prodname":prodname}
    response = requests.get(CustomModule.mkQuery.mkQuery(URL, query))
    return response.text