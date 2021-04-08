import http.client


def envoyer_mouvement(mouvement):
    c = http.client.HTTPConnection("127.0.0.1:8000")
    c.request("GET", f"/add/{mouvement}")
    r = c.getresponse()
    print(r.status, r.reason)
    print(r.read())


if __name__ == "__main__":
    envoyer_mouvement("e5")
