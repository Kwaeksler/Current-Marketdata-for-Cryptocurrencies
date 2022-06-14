<a name="toeng"/><br />

# Current Marketdata for Cryptocurrencies
Go to german installation guide: [GER](#German)  
### Table of contents
1. [Description](#Description)  
2. [Requirements](#Requirements)
3. [Installation](#InstallationEN)
4. [Configuration](#Configuration)
5. [Execution](#Execution)
6. [Implementation in MS Excel (Office365)](#ExcelImplementation)
7. [Refresh Data](#RefreshData)

 
<a name="Description"/><br />

## Description
The script reads current market data of any cryptocurrencies via the API of CoinGecko.com and creates a report (JSON file). which can be included e.g. for portfolio monitoring in Microsoft Excel.

![grafik](https://user-images.githubusercontent.com/22911401/172491176-58283117-706c-4840-b791-6b9b446f3f74.png)

<a name="Requirements"/><br />

## Requirements

#### Python - Installation
The skript is written in Pyhton. Phyton must be installed on the end device to run:
`https://www.python.org/downloads`

#### Python - Packages
For the HTTP/HTTPS queries the Pyhton package "Requests" is additionally required, installation under Windows:
```
WIN + R
cmd.exe
pip install requests
```
<a name="InstallationEN"/><br />

## Installation
#### Manuel installation
Download the current GitHub repository at: <br /> `https://github.com/Kwaeksler/Current-Marketdata-for-Cryptocurrencies` > `Code` > `Download ZIP`
<br /><br />
Unzip the ZIP file and save it to a desired location.

#### Installation via Git
```
git clone https://github.com/Kwaeksler/Current-Marketdata-for-Cryptocurrencies.git
```

<a name="Configuration"/><br />

## Configuration
In the file `Coins.txt` the desired cryptocurrencies can be specified. Please add the cryptocurrencies from line three. The `API id` of the cryptocurrency from CoinGecko.com must be specified, which can be found on the respective coin page:
<br />

![grafik](https://user-images.githubusercontent.com/22911401/172491888-3d822e39-6d93-4e4b-8e1b-1a0788ac33f7.png)

<br />
Example configuration:

```
Enter Coins (API-ID from CoinGecko.com) - Only one value per line:
------------------------------------------------------------------
bitcoin
ethereum
tether
binancecoin
```

<br />


In the file `getCGData.py` in the area `Configuration` the program can be configured. For this purpose the values of the variables can be adjusted (*optional*):

Variable | Explanation
--- | ---
FileCoins | *Specification of a string for the file name, without file extension! In this file the desired cryptocurrencies must be specified, which are to be queried. The file must be in the format `.txt`! Default: `Coins`*
FileJson | *Specification of a string for the file name, without file extension! The report will be stored in this file. Default: `CoinData`*
Currency | *Specification in which currency the market data should be retrieved. Default: `eur`* <br /> *More options: `usd`, `btc`, `eth`, ...*
Debug | *Possibilities:* <br /> *`True` The terminal window remains open after the script is finished to view the history and any errors that occur<br />`False`The terminal window will be closed after the script is finished*
date_format | *The output of the timestamps can be configured as desired. Default: `%d.%m.%Y` = `08.06.2022`*

(*The free API of CoinGecko.com allows only about 50 queries per minute. If more cryptocurrencies are queried, the program is interrupted more often.*)

<a name="Execution"/><br />

## Execution
The program can be executed by double-clicking on the file `getCGData.py`. 
<br />
Alternatively via command line: `py getCGData.py`

<a name="ExcelImplementation"/><br />

## Implementation in Microsoft Excel (Office 365)
It is recommended to insert a new spreadsheet for implementation and implement the JSON file there:
<br />
`Data` > `Get Data` > `From File` > `From JSON` > `Select *.JSON-File` > `Import`
<br /><br />
Transform the Rewards `to Table`:
- Select or enter delimiter: `None`
- How to handle extra columns: `Show as errors`

#### Customize column names, columns & order:
![grafik](https://user-images.githubusercontent.com/22911401/172082397-94196be0-ae65-415b-87af-88a120317a54.png)
- Via the symbol next to "Column1" the original column names can be shown (left picture)
- Here you have to uncheck 'Use original column name as prefix' (middle image)
- Columns that are not needed can be hidden (middle image)
- By right-clicking on a column header, individual columns can be moved in the order (right image)

The dialog can be closed by clicking the `Close & Load` button. Afterwards a dynmaic table should appear on the spreadsheet, which can be formatted.

<a name="RefreshData"/><br />

## Refresh data
Running the `getCGData.py` file will update the .JSON file. 
<br />
Then, in Microsoft Excel, the previously inserted table can be updated via `Data` > `Update all`.


<br />
<hr style="border:2px solid gray">
<br /><br /><br /><br />
<a name="German"/><br />


# Aktuelle Marktdaten für Kryptowährungen

Go to english installation guide: [ENG](#toeng)  

### Inhaltsverzeichnis
1. [Beschreibung](#Beschreibung)  
2. [Voraussetzungen](#Voraussetzungen)
3. [Installation](#InstallationDE)
4. [Konfiguration](#Konfiguration)
5. [Ausführung](#Ausführung)
6. [Implementierung in MS Excel (Office365)](#ExcelImplementierung)
7. [Daten aktualisieren](#DatenAktualisieren)

 
<a name="Beschreibung"/><br />

## Beschreibung
Das Skript liest aktuelle Marktdaten von beliebigen Kryptowährungen über die API von CoinGecko.com aus und erstellt ein Report (JSON-Datei), welcher z.B. für die Portfolioüberwachung in Microsoft Excel eingebunden werden kann.

![grafik](https://user-images.githubusercontent.com/22911401/172491176-58283117-706c-4840-b791-6b9b446f3f74.png)

<a name="Voraussetzungen"/><br />

## Voraussetzungen

#### Python - Installation
Das Skript ist in Pyhton programmiert, Phyton muss zur Ausführung auf dem Endgerät installiert sein:
`https://www.python.org/downloads`

#### Python - Packages
Für die HTTP/HTTPS-Abfragen wird zusätzlich das Pyhton-Paket "Requests" benötigt, Installation unter Windows:
```
WIN + R
cmd.exe
pip install requests
```
<a name="InstallationDE"/><br />

## Installation des Skriptes
#### Manuelle Installation
Download des aktuellen GitHub Repositories unter: <br /> `https://github.com/Kwaeksler/Current-Marketdata-for-Cryptocurrencies` > `Code` > `Download ZIP`
<br /><br />
Die ZIP-Datei entpacken und an einen gewünschten Ort abspeichern.

#### Installation via Git
```
git clone https://github.com/Kwaeksler/Current-Marketdata-for-Cryptocurrencies.git
```

<a name="Konfiguration"/><br />

## Konfiguration
In der Datei `Coins.txt` können die gewünschten Kryptowährungen angegeben werden, welche ausgelesen werden sollen. Bitte ab Zeile drei die Kryptowährungen hinzufügen. Angegeben werden muss die `API id` der jeweiligen Kryptowährung von CoinGecko.com, welche auf der jeweiligen Coin-Seite zu finden ist:
<br />

![grafik](https://user-images.githubusercontent.com/22911401/172491888-3d822e39-6d93-4e4b-8e1b-1a0788ac33f7.png)

<br />
Beispielkonfiguration:

```
Enter Coins (API-ID from CoinGecko.com) - Only one value per line:
------------------------------------------------------------------
bitcoin
ethereum
tether
binancecoin
```

<br />


In der Datei `getCGData.py` im Bereich `Configuration` kann das Programm konfiguriert werden, dazu können die Werte der Variablen angepasst werden (*Optional*):

Variable | Erläuterung
--- | ---
FileCoins | *Angabe einer beliebigen Zeichenkette für den Dateinamen, ohne Dateiendung! In dieser Datei müssen die gewünschten Kryptowährungen angegeben werden, welche abgefragt werden sollen. Die Datei muss im Format `.txt` vorliegen! Default: `Coins`*
FileJson | *Angabe einer beliebigen Zeichenkette für den Dateinamen, ohne Dateiendung! In dieser Datei werden die Marktdaten abgespeichert. Default: `CoinData`*
Currency | *Angabe in welcher Währung die Marktdaten abgerufen werden sollen. Default: `eur`* <br /> *Weitere Möglichkeiten: `usd`, `btc`, `eth`, uvm.*
Debug | *Möglichkeiten:* <br /> *`True` Das Terminal-Fenster bleibt nach Beendigung des Skriptes geöffnet, um den Verlauf und auftretende Fehler einzusehen<br />`False`Das Terminal-Fenster wird nach Beendigung des Skriptes geschlossen*
date_format | *Die Ausgabe der Zeitstempel kann beliebig konfiguriert werden. Default: `%d.%m.%Y` = `08.06.2022`*

(*Die freie API von CoinGecko.com erlaubt nur ca. 50 Abfragen pro Minute. Werden mehr Kryptowährungen abgefragt, wird das Programm öfter untebrochen.*)

<a name="Ausführung"/><br />

## Ausführung
Das Programm kann durch einen Doppelklick auf die Datei `getCGData.py` ausgeführt werden. 
<br />
Alternativ über die Kommandozeile: `py getCGData.py`

<a name="ExcelImplementierung"/><br />

## Implementierung in Microsoft Excel (Office 365)
Es ist empfehlenswert ein neues Tabellenblatt für die Implementierung einzufügen und dort die JSON-Datei zu implementieren:
<br />
`Daten` > `Daten abrufen` > `Aus Datei` > `Von JSON` > `*.JSON-Datei auswählen` > `Importieren`
<br /><br />
Im geöffneten Listentool die Rewards `Zu Tabelle` konvertieren:
- Trennzeichen eingeben oder auswählen: `Keine`
- Behandlung zusätzlicher Spalten: `Als Fehler anzeigen`

#### Spaltennamen, Spalten & Reihenfolge anpassen:
![grafik](https://user-images.githubusercontent.com/22911401/172495028-d47533bb-fabb-44dd-9d73-628953c49406.png)
- Über das Symbol neben "Column1" lassen sich die originalen Spaltennamen einblenden (linkes Bild)
- Hier muss der Haken bei `Ursprünglichen Spaltennamen als Präfix verwenden` entfernt werden (mittleres Bild)
- Nicht benötigte Spalten können ausgeblendet werden (mittleres Bild)
- Durch einen Rechtsklick auf eine Spaltenüberschrift lassen sich einzelne Spalten in der Reihenfolge verschieben (rechtes Bild)

Der Dialog kann durch Klick auf die Schaltfläche `Schließen & laden` beendet werden. Anschließend sollte eine dynmaische Tabelle auf dem Tabellenblatt erscheinen, welche formatiert werden kann.

<a name="DatenAktualisieren"/><br />

## Daten aktualisieren
Durch das Ausführen der `getCGData.py`-Datei wird die .JSON-Datei aktualisiert. 
<br />
Anschließend kann in Microsoft Excel die vorher eingefügte Tabelle über `Daten` > `Alle Aktualisieren` aktualisiert werden.
