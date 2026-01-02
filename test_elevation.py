import requests
import json

# İsviçre Alplerindeki Rastgele Bazı Zirveler
locations = {
    "Matterhorn Zirvesi": (45.9763, 7.6586),
    "Zermatt Köyü": (46.0207, 7.7491),
    "Gornergrat, Gözlem Evi": (45.9839, 7.7834),
}

def fetch_elevation_data(geo_data):
    """
    Open-Elevation API kullanarak verilen koordinatların
    deniz seviyesinden yüksekliğini (altitude) çeker
    """
    api_url = "https://api.open-elevation.com/api/v1/lookup"
    
    payload = {"locations": []}
    for name, (lat, lon) in geo_data.items():
        payload["locations"].append({"latitude": lat, "longitude": lon})

    try:
        #print("\n NASA SRTM veritabanına bağlanılıyor...")
        response = requests.post(api_url, json=payload, timeout=15)
        
        if response.status_code == 200:
            results = response.json()['results']
            print("\n YÜKSEKLİK ANALİZİ SONUÇLARI:")
            print("-" * 40)
            for i, item in enumerate(results):
                name = list(geo_data.keys())[i]
                print(f"- {name:<25}: {int(item['elevation'])} metre")
        else:
            print("API Hatası:", response.status_code)

    except Exception as e:
        print("Bağlantı sorunu:", e)

if __name__ == "__main__":
    fetch_elevation_data(locations)