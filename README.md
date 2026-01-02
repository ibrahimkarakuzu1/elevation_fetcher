#  Python Elevation Fetcher


##  Objective
To move beyond 2D geospatial data by programmatically accessing **Altitude (Elevation)** information. This study serves as the foundational infrastructure for developing 3D pathfinding algorithms and energy-efficient routing models.

## Tech Stack
* **Python**
* **Open-Elevation API:** An open-source alternative to Google Elevation API, utilizing NASA's SRTM (Shuttle Radar Topography Mission) dataset.
* **Requests Module:** For handling HTTP API transactions.

## How It Works
The script accepts a set of latitude/longitude coordinates (e.g., peaks in the Swiss Alps) and queries the DEM database to return the precise elevation in meters.

### Sample Output:
```text
Connecting to NASA SRTM database...

ELEVATION ANALYSIS RESULTS:
----------------------------------------
 Matterhorn Summit      : 4478 meters
 Zermatt Village        : 1608 meters
