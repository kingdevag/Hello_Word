#Import
import phonenumbers
import os
import folium

#From-Import
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
from dotenv import load_dotenv

load_dotenv()


#Functions

def main():
    key = os.environ['keyphone']
    number = input("Ingresa el Numero a Localizar: $ ")
    sanNumber = phonenumbers.parse(number)
    YLc = geocoder.description_for_number(sanNumber, "en")
    SPn = phonenumbers.parse(number)
    GoC = OpenCageGeocode(key)
    query = str(YLc)
    R = GoC.geocode(query)
    lat = R[0]['geometry']['lat']
    lng = R[0]['geometry']['lng']
    myMap = folium.Map(location=[lat, lng], zoom_start=9)
    print(YLc)
    print(carrier.name_for_number(SPn, "en"))
    print(lat, lng)
    folium.Marker([lat, lng], popup=YLc).add_to((myMap))
    myMap.save('html/Phone_location.html')
    print("Mapa guardado en: html/Phone_location")
    
#Run
if __name__ == '__main__':
    main()