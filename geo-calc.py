from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import geocoder as gc
import time
import os

def geocalc():
    try:
        os.system("cls")
        geocoder = Nominatim(user_agent="Dev: Diogo S. Lourenço")

        print("DIGITE A LOCALIZAÇÃO DE ORIGEM E A LOCALIZAÇÃO DE DESTINO")
        print("PARA CALCULAR A DISTÂNCIA ENTRE AS LOCALIDADES")
        print()
        print("OBS: DEIXE VAZIO PARA USAR SUA PRÓPRIA LOCALIZAÇÃO")
        print()
        print("by Diogo S. Lourenço")
        print()
        print('------------------------------------------------------------')
        print()
        print("Localização de origem: ")
        location = input("$ ")
        location = location.upper()

        def auto_loc():
            g = gc.ip('me')

            city = g.city
            city.upper()

            estado = g.state
            estado.upper()

            pais = g.country
            pais.upper()

            return city, estado, pais

        print()
        print("Localização de destino: ")
        destino = input("$ ")
        destino = destino.upper()

        if location is None or location == "" or location == " ":
            print("\nColetando endereço IP...")
            time.sleep(1)

            print("Obtendo localização origem...")
            time.sleep(1)

            location = auto_loc()
            print('----------------------------------')
        
        if destino is None or destino == "" or destino == " ":
            print("\nColetando endereço IP...")
            time.sleep(1)

            print("Obtendo localização destino...")
            time.sleep(1)

            destino = auto_loc()
            print('----------------------------------')

        origem = geocoder.geocode(location)
        dest = geocoder.geocode(destino)

        def cord_origem(loc_orig):
            if loc_orig is not None:
                lat_orig = loc_orig.latitude
                log_orig = loc_orig.longitude

                return lat_orig, log_orig
            else:
                erro = print(
                    "Houve um erro em sua localização de origem. Tente novamente.")
                return erro

        def cord_dest(loc_dest):
            if loc_dest is not None:
                lat_dest = loc_dest.latitude
                log_dest = loc_dest.longitude

                return lat_dest, log_dest
            else:
                erro = print(
                    "Houve um erro em seu endereço de destino. Tente novamente.")
                return erro

        def calc(origem, destino, cord_orig, cord_dest):
            distance = geodesic(cord_orig, cord_dest).kilometers
            distance = "{:.2f}".format(distance)

            result = print(
                f"A distância entre {origem} e {destino} é de {distance} Km(quilômetros).")
            return result

        cord_orig = cord_origem(origem)
        cord_des = cord_dest(dest)
        os.system("cls")
        print()
        calc(location, destino, cord_orig, cord_des)

    except Exception as ex:
        os.system("cls")
        print("Houve um erro inesperado. Tente novamente.")

geocalc()
