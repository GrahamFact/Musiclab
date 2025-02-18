import requests

artists = [
    "Dilo, Matthias Meyer and Patlac",
    "SevenDoors",
    "Jonas Saalbach, Chris Robin",
    "Kai Anschau feat. Mallory N",
    "Le Carousel",
    "Maceo Plex",
    "Mano Le Tough",
    "Marcus Worgull, Peter Pardeike",
    "Marian Herzog, Modshape",
    "Mr FijiWiji",
    "Peter Pardeike, Olderic",
    "Sandrino & Frankey",
    "Super Flu - Mygut",
    "Solar Fields",
    "100 Day Delay",
    "Abiogenesis",
    "Agiovono",
    "Air Shaper",
    "AK",
    "Midtro, James Stailey",
    "Andy Leech",
    "Arros",
    "Astronaut Ape",
    "Asura",
    "Azaleh",
    "BlauDisS",
    "Blurre",
    "C.J Catalizer",
    "CARBON BASED LIFEFORMS",
    "Cell",
    "Chasing Dreams",
    "Chronos, OkoloSna",
    "Connect.ohm",
    "Crystal Vibe",
    "Electus",
    "ELV",
    "Ethan Gold",
    "Ether",
    "Fading Language",
    "Fugamu",
    "H.U.V.A. Network",
    "Hazy"
]

api_url = "http://127.0.0.1:8000/api/artist/"


for artist in artists:
    data = {
        "name": artist,
        "bio": "",
        "country": ""
    }
    response = requests.post(api_url, json=data)

    if response.status_code == 201:
        print(f"Успешно добавлен: {artist}")
    else:
        print(f"Ошибка при добавлении {artist}: {response.status_code}, {response.text}")
