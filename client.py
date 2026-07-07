import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")


def geocode_address(address: str) -> dict:
    resp = requests.get(
        "https://maps.googleapis.com/maps/api/geocode/json",
        params={"address": address, "key": API_KEY},
        timeout=10
    )
    resp.raise_for_status()
    data = resp.json()

    if data["status"] != "OK":
        raise ValueError(f"Geocoding failed for '{address}': {data['status']}")

    location = data["results"][0]["geometry"]["location"]
    return {
        "lat": location["lat"],
        "lng": location["lng"],
        "resolved_address": data["results"][0]["formatted_address"]
    }