import requests, json,os
from datetime import datetime

url_station_inf = "https://velib-metropole-opendata.smovengo.cloud/opendata/Velib_Metropole/station_information.json"
url_station_status = "https://velib-metropole-opendata.smovengo.cloud/opendata/Velib_Metropole/station_status.json"

# fonction pour extraire les données de station
def extract_data(url,feeds): 
    response=requests.get(url)  
    data = response.json()
    horodatage = datetime.now().strftime("%Y%m%d_%H%M%S")
    chemin = f"ingestion/raw/{feeds}_{horodatage}.json"
    with open(chemin, 'w', encoding='utf-8') as f:
        json.dump(response.json(), f, ensure_ascii=False, indent=4)
    return data        

extract_data(url_station_inf, "information")
extract_data(url_station_status, "status")
    

