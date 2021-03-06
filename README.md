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


# Aktuelle Marktdaten f??r Kryptow??hrungen

Go to english installation guide: [ENG](#toeng)  

### Inhaltsverzeichnis
1. [Beschreibung](#Beschreibung)  
2. [Voraussetzungen](#Voraussetzungen)
3. [Installation](#InstallationDE)
4. [Konfiguration](#Konfiguration)
5. [Ausf??hrung](#Ausf??hrung)
6. [Implementierung in MS Excel (Office365)](#ExcelImplementierung)
7. [Daten aktualisieren](#DatenAktualisieren)

 
<a name="Beschreibung"/><br />

## Beschreibung
Das Skript liest aktuelle Marktdaten von beliebigen Kryptow??hrungen ??ber die API von CoinGecko.com aus und erstellt ein Report (JSON-Datei), welcher z.B. f??r die Portfolio??berwachung in Microsoft Excel eingebunden werden kann.

![grafik](https://user-images.githubusercontent.com/22911401/172491176-58283117-706c-4840-b791-6b9b446f3f74.png)

<a name="Voraussetzungen"/><br />

## Voraussetzungen

#### Python - Installation
Das Skript ist in Pyhton programmiert, Phyton muss zur Ausf??hrung auf dem Endger??t installiert sein:
`https://www.python.org/downloads`

#### Python - Packages
F??r die HTTP/HTTPS-Abfragen wird zus??tzlich das Pyhton-Paket "Requests" ben??tigt, Installation unter Windows:
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
Die ZIP-Datei entpacken und an einen gew??nschten Ort abspeichern.

#### Installation via Git
```
git clone https://github.com/Kwaeksler/Current-Marketdata-for-Cryptocurrencies.git
```

<a name="Konfiguration"/><br />

## Konfiguration
In der Datei `Coins.txt` k??nnen die gew??nschten Kryptow??hrungen angegeben werden, welche ausgelesen werden sollen. Bitte ab Zeile drei die Kryptow??hrungen hinzuf??gen. Angegeben werden muss die `API id` der jeweiligen Kryptow??hrung von CoinGecko.com, welche auf der jeweiligen Coin-Seite zu finden ist:
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


In der Datei `getCGData.py` im Bereich `Configuration` kann das Programm konfiguriert werden, dazu k??nnen die Werte der Variablen angepasst werden (*Optional*):

Variable | Erl??uterung
--- | ---
FileCoins | *Angabe einer beliebigen Zeichenkette f??r den Dateinamen, ohne Dateiendung! In dieser Datei m??ssen die gew??nschten Kryptow??hrungen angegeben werden, welche abgefragt werden sollen. Die Datei muss im Format `.txt` vorliegen! Default: `Coins`*
FileJson | *Angabe einer beliebigen Zeichenkette f??r den Dateinamen, ohne Dateiendung! In dieser Datei werden die Marktdaten abgespeichert. Default: `CoinData`*
Currency | *Angabe in welcher W??hrung die Marktdaten abgerufen werden sollen. Default: `eur`* <br /> *Weitere M??glichkeiten: `usd`, `btc`, `eth`, uvm.*
Debug | *M??glichkeiten:* <br /> *`True` Das Terminal-Fenster bleibt nach Beendigung des Skriptes ge??ffnet, um den Verlauf und auftretende Fehler einzusehen<br />`False`Das Terminal-Fenster wird nach Beendigung des Skriptes geschlossen*
date_format | *Die Ausgabe der Zeitstempel kann beliebig konfiguriert werden. Default: `%d.%m.%Y` = `08.06.2022`*

(*Die freie API von CoinGecko.com erlaubt nur ca. 50 Abfragen pro Minute. Werden mehr Kryptow??hrungen abgefragt, wird das Programm ??fter untebrochen.*)

<a name="Ausf??hrung"/><br />

## Ausf??hrung
Das Programm kann durch einen Doppelklick auf die Datei `getCGData.py` ausgef??hrt werden. 
<br />
Alternativ ??ber die Kommandozeile: `py getCGData.py`

<a name="ExcelImplementierung"/><br />

## Implementierung in Microsoft Excel (Office 365)
Es ist empfehlenswert ein neues Tabellenblatt f??r die Implementierung einzuf??gen und dort die JSON-Datei zu implementieren:
<br />
`Daten` > `Daten abrufen` > `Aus Datei` > `Von JSON` > `*.JSON-Datei ausw??hlen` > `Importieren`
<br /><br />
Im ge??ffneten Listentool die Rewards `Zu Tabelle` konvertieren:
- Trennzeichen eingeben oder ausw??hlen: `Keine`
- Behandlung zus??tzlicher Spalten: `Als Fehler anzeigen`

#### Spaltennamen, Spalten & Reihenfolge anpassen:
![grafik](https://user-images.githubusercontent.com/22911401/172495028-d47533bb-fabb-44dd-9d73-628953c49406.png)
- ??ber das Symbol neben "Column1" lassen sich die originalen Spaltennamen einblenden (linkes Bild)
- Hier muss der Haken bei `Urspr??nglichen Spaltennamen als Pr??fix verwenden` entfernt werden (mittleres Bild)
- Nicht ben??tigte Spalten k??nnen ausgeblendet werden (mittleres Bild)
- Durch einen Rechtsklick auf eine Spalten??berschrift lassen sich einzelne Spalten in der Reihenfolge verschieben (rechtes Bild)

Der Dialog kann durch Klick auf die Schaltfl??che `Schlie??en & laden` beendet werden. Anschlie??end sollte eine dynmaische Tabelle auf dem Tabellenblatt erscheinen, welche formatiert werden kann.

<a name="DatenAktualisieren"/><br />

## Daten aktualisieren
Durch das Ausf??hren der `getCGData.py`-Datei wird die .JSON-Datei aktualisiert. 
<br />
Anschlie??end kann in Microsoft Excel die vorher eingef??gte Tabelle ??ber `Daten` > `Alle Aktualisieren` aktualisiert werden.
