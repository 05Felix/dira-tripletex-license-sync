import requests

base_url = "https://api.tripletex.io/v2"

consumerToken = "eyJ0b2tlbklkIjoyMDEwLCJ0b2tlbiI6InRlc3QtNmY1NDRhZGMtODNmMy00NGRlLWE0MmEtY2EyMTBiZDdkNjYwIn0="
employeeToken = "eyJ0b2tlbklkIjozMjc3LCJ0b2tlbiI6InRlc3QtYTNhODI5YzItNDA2Ny00NGIzLWEzMzktNjUxNTQ4ZmQyYjcwIn0="
sessionToken = "eyJ0b2tlbklkIjoyMDI4NDQ4MSwidG9rZW4iOiJ0ZXN0LWIzNzEwZWFiLTQ3MzAtNGFkZC1hMWU4LTIzZWY1MzY3MTI4YSJ9"
encodedToken = "MDpleUowYjJ0bGJrbGtJam95TURJNE5EUTRNU3dpZEc5clpXNGlPaUowWlhOMExXSXpOekV3WldGaUxUUTNNekF0TkdGa1pDMW" \
               "hNV1U0TFRJelpXWTFNelkzTVRJNFlTSjk="

konto_passord = "Test-1ICnm3EKy"

auth = {"Authorization": f"Basic {encodedToken}"}

ids = ["1279487", "1279489", "1279491"]


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
