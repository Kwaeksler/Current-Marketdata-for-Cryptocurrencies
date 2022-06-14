#!/usr/bin/python
# |--------------------------------------------------------------------------------------
# | Repository: Current-Marketdata-for-Cryptocurrencies
# | Description: Read current cryptocurrency data from CoinGecko.com and export it to JSON
# | Version: 1.0
# | Author: Daniel H.
# | Author URI: https://github.com/Kwaeksler
# | License: GNU General Public License v3.0
# |--------------------------------------------------------------------------------------

import json
import time
from datetime import datetime
import os.path
import requests

t1 = time.perf_counter()

### Configuration #############################################################
FileCoins = "Coins"
FileJson = "CoinData"
Currency = "eur"
Debug = True
date_format = "%d.%m.%Y"
###############################################################################

### Check if the files exists and get Coins
FileCoins = FileCoins + ".txt"
FileJson = FileJson + ".json"
filexists = os.path.exists(FileCoins)

if filexists == True:
    f = open(FileCoins, "r")
    fdata = f.read()
    fdata = fdata.split("\n")
else:
    print(f"\nFehler: Die Datei '{FileCoins}' ist nicht vorhanden - Das Programm wurde beendet!\n")
    if Debug == True:
        print("-------------------------------------------------------------------------------")
        print("\nDrücke 'Enter', um das Fenster zu schließen ...")
        input()
    exit()

i = 2
results = []

while i < len(fdata):
    coin = fdata[i]
    if coin:
        r = requests.get(f"https://api.coingecko.com/api/v3/coins/markets?vs_currency={Currency}&ids={coin}", headers={'User-agent':'CGBot'})
        
        if r.status_code == 429:
            print("-------------------------------------------------------------------------------")
            print(f"\nStatus: Zu viele API-Anfragen bei CoinGecko.com - Skript wird für {r.headers['Retry-After']} Sekunden pausiert und anschließend fortgesetzt ...\n")
            print("-------------------------------------------------------------------------------")
            time.sleep(int(r.headers["Retry-After"]))

            print("\nStatus: Das Skript wird fortgesetzt ...\n")
            r = requests.get(f"https://api.coingecko.com/api/v3/coins/markets?vs_currency={Currency}&ids={coin}", headers={'User-agent':'CGBot'})

        CoinData = r.json()

        try:
            name = CoinData[0]['name']
            em = 0
        except IndexError:
            em = 1

        if em == 0:
            ### Format Datetime
            ATH_Date = CoinData[0]['ath_date']
            ATH_Date = datetime.strptime(ATH_Date, "%Y-%m-%dT%H:%M:%S.%fZ").strftime(date_format)
            ATL_Date = CoinData[0]['atl_date']
            ATL_Date = datetime.strptime(ATL_Date, "%Y-%m-%dT%H:%M:%S.%fZ").strftime(date_format)

            data = {
                'Name': name,
                'Symbol': CoinData[0]['symbol'],
                'Price': CoinData[0]['current_price'],
                'Price_Change_%_24h': CoinData[0]['price_change_percentage_24h'],
                'MCAP': CoinData[0]['market_cap'],
                'MCAP_Rank': CoinData[0]['market_cap_rank'],
                'Circ_Supply': CoinData[0]['circulating_supply'],
                'ATH': CoinData[0]['ath'],
                'ATH_Date': ATH_Date,
                'ATH_Change_%': CoinData[0]['ath_change_percentage'],
                'ATL': CoinData[0]['atl'],
                'ATL_Date': ATL_Date,
                'ATL_Change_%': CoinData[0]['atl_change_percentage'],
            }

            results.append(data)
            print(f"Status: Coin-ID {i-1} - Aktuelle Marktdaten von '{name}' wurden erfolgreich abgefragt (Währung: {Currency.upper()})\n")

        else: 
            print(f"Fehler: Angegebener Coin ({coin}) in Zeile {i+1} der Datei '{FileCoins}' nicht gefunden - Bitte überprüfen")

    i = i + 1

### Insert list to JSON-File
with open(FileJson, 'w') as f:
    json.dump(results, f, indent=2, default=str)
f.close()

### Print final statements
filexists = os.path.exists(FileJson)

if filexists == True:
    if len(results) > 0:
        print(f"Status: Die Datei '{FileJson}' wurde erfolgreich erstellt. Es wurden Marktdaten von {len(results)} Kryptowährungen hinzugefügt\n")
    else:
        print(f"\nStatus: In der Datei '{FileCoins}' wurden keine Coins zum auslesen angegeben - Bitte überprüfen\n")
else:
    print(f"Fehler: Die Datei '{FileJson}' konnte nicht erstellt werden, bitte erneut versuchen\n")

### Calculate runtime
t2 = time.perf_counter()
runtime = t2-t1
print("Info: Skript-Laufzeit: %.4f sek.\n" % runtime)

if Debug == True:
    print("-------------------------------------------------------------------------------")
    print("\nDrücke 'Enter', um das Fenster zu schließen ...")
    input()
