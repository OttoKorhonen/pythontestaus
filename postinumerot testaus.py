import urllib.request
import json
import urllib.parse


def main():
    print_results()


def fetch_data():
    try:
        with urllib.request.urlopen(
            'https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json'
        ) as response:
            responseData = json.loads(response.read().decode())
            return responseData.items()
    except:
        print("Oops... fetch error")


def ask_for_city():
    data = fetch_data()
    kaupunki = input("Anna kaupunki: ")
    haluttu = kaupunki.upper()
    numerot = []
    for x, y in data:
        if y == haluttu:
            numerot.append(x)

    return numerot


def print_results():
    nums = ask_for_city()
    postinumerot = ', '.join([str(n) for n in nums])
    print("Postinumerot: {}".format(postinumerot))


if __name__ == "__main__":
    main()

# annettua nimeä ei löydy lainkaan aineistosta
def test_city_not_found():
    data = fetch_data()
    kaupunki = 'tukholma'  # input("Anna kaupunki: ")
    haluttu = kaupunki.upper()
    numerot = []
    for x, y in data:
        if y == haluttu:
            numerot.append(x)
    
    assert haluttu not in data


# postitoimipaikan nimellä löytyy yksi postinumero
def test_will_return_one_result():
    data = fetch_data()
    kaupunki = 'helsinki'  # input("Anna kaupunki: ")
    haluttu = kaupunki.upper()
    numerot = []
    for x, y in data:
        if y == haluttu:
            numerot.append(x)

    assert len(numerot) < 1

# postitoimipaikan nimellä löytyy useita postinumeroita
def test_ask_for_city():
    # kun kaupunki on Helsinki postinumeroita tulee enemmän kuin 0
    data = fetch_data()
    kaupunki = 'helsinki'  # input("Anna kaupunki: ")
    haluttu = kaupunki.upper()
    numerot = []
    for x, y in data:
        if y == haluttu:
            numerot.append(x)

    assert len(numerot) > 0

#fetch_data funktio tuo dataa
def test_fetch_data_works():
    get_data = fetch_data()

    assert len(get_data) > 0