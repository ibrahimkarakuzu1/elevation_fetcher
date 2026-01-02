# Python Elevation Fetcher 

##  Amaç
Coğrafi koordinatların (Enlem/Boylam) 3. boyutu olan **Yükseklik (Altitude)** verisine programatik olarak erişmek. Bu çalışma, 3D rota planlama algoritmaları için bir ön hazırlıktır.

##  Teknoloji
* **Python**
* **Open-Elevation API:** NASA SRTM verisetini kullanan açık kaynaklı API.
* **JSON/Requests:** Veri alışverişi için.

##  Nasıl Çalışır?
Script, belirlenen koordinatları API'ye gönderir ve metre cinsinden yükseklik verisini döndürür.

```bash
# Örnek Çıktı
📍 Matterhorn Zirvesi  : 4478 metre
📍 Zermatt Köyü        : 1608 metre
