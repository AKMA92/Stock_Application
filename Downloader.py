import json
import requests
import time
import os


class Downloader:
    stock = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&outputsize=compact&apikey=DEIN_KEY"
    cache_file = "stock_cache.json"

    def __init__(self):
        pass

    def get_data(self):
        # Prüfen, ob Cache-Datei existiert
        if os.path.exists(self.cache_file):
            file_time = os.stat(self.cache_file).st_mtime
            current_time = time.time()
            age = current_time - file_time

            # Wenn Datei jünger als 10 Minuten ist -> Cache benutzen
            if age < 600:
                print("Benutze Cache-Datei")
                with open(self.cache_file, "r") as file:
                    return json.load(file)

        # Sonst neue Daten laden
        retries = 4

        for attempt in range(retries):
            try:
                response = requests.get(self.stock)
                response.raise_for_status()
                json_data = json.loads(response.text)

                # Neue Daten in Cache-Datei speichern
                with open(self.cache_file, "w") as file:
                    json.dump(json_data, file, indent=4)

                return json_data

            except Exception as e:
                print(f"Fehler bei Versuch {attempt + 1}: {e}")

                wait_time = 2 ** attempt
                print(f"Warte {wait_time} Sekunden...")
                time.sleep(wait_time)

        print("Maximale Versuche erreicht")
        return None