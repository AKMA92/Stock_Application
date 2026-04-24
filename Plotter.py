import pandas as pd
import matplotlib.pyplot as plt


class Plotter:

    def __init__(self, data):
        self.data = data


    def plot(self):
        # 1. Time Series holen
        daily_prices  = self.data["Time Series (Daily)"]

        # 2. Letzte 10 Tage nehmen
        last_10 = list(daily_prices .items())[:10]

        dates = []
        closes = []

        # 3. Daten vorbereiten
        for date, values in last_10:
            dates.append(date)
            closes.append(float(values["4. close"]))

        # 4. DataFrame erstellen
        unsorted_prices_df = pd.DataFrame({
            "date": dates,
            "close": closes
        })

        # 5. Datum sortieren (wichtig für Plot!)
        sorted_prices_df = unsorted_prices_df.sort_values("date")

        print("DataFrame:")

        print(unsorted_prices_df)

        # Statistik berechnen
        mean_close = sorted_prices_df["close"].mean()
        min_close = sorted_prices_df["close"].min()
        max_close = sorted_prices_df["close"].max()
        std_close = sorted_prices_df["close"].std()

        print("\nStatistiken:")
        print(f"Durchschnittlicher Close Preis: {mean_close:.2f} USD")
        print(f"Tiefster Close Preis: {min_close:.2f} USD")
        print(f"Höchster Close Preis: {max_close:.2f} USD")
        print(f"Standardabweichung: {std_close:.2f}")

        # Symbol holen
        symbol = self.data["Meta Data"]["2. Symbol"]

        # 6. Plot
        plt.plot(sorted_prices_df["date"], sorted_prices_df["close"], marker="o")
        plt.xticks(rotation=45)
        plt.title(f"Aktienkurs {symbol} letzte 10 Tage in USD")
        plt.xlabel("Datum")
        plt.ylabel("Close Preis")
        plt.tight_layout()
        plt.show()