import psutil, requests, time, os
from dotenv import load_dotenv

load_dotenv()
API_URL = "https://kaya-api-gfcjfqaqeag2crfv.westeurope-01.azurewebsites.net/items"

while True:
    cpu = psutil.cpu_percent()
    payload = {
        "metric_naam": "CPU_Gebruik",
        "bron": "Monitor_Script",
        "waarde": f"{cpu}%"
    }
    try:
        res = requests.post(API_URL, json=payload)
        print(f"Verzonden! Status: {res.status_code}")
    except Exception as e:
        print(f"Fout: {e}")
    
    time.sleep(5)