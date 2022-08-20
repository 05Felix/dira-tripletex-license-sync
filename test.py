import requests
import main

base_url = "https://api.tripletex.io/v2"


konto_passord = "Test-1ICnm3EKy"

auth = {"Authorization": f"Basic {main.encodedToken}"}


def update(id, count):
    requests.put(base_url + "/order/orderline/" + id, headers=auth, json={"count": count})


def get_count(row):
    get = requests.get("https://api.sheety.co/4edeee1f3b1c5955765fa8e479bef1ee/testProduktoppdatering/ark1")
    new_count = get.json()
    return new_count["ark1"][row]["used"]


def get_id(row):
    response = requests.get("https://api.sheety.co/4edeee1f3b1c5955765fa8e479bef1ee/testProduktoppdatering/ark1")
    id = response.json()
    try:
        return str(id["ark1"][row]["#"])
    except:
        return None


n = 0

while get_id(n) is not None:
    update(get_id(n), get_count(n))
    n += 1
