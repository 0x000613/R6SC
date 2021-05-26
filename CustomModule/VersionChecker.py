import requests
import mkQuery

def versionChecker(prodname):
    URL = "https://api.xeros.dev"
    query = {"api":"vc", "prodname":prodname}
    response = requests.get(mkQuery.mkQuery(URL, query))
    print(response.text)

versionChecker("asdf")