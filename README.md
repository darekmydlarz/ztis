# Uruchomienie aplikacji
W lokalnym środowisku:
```
pip install -r requirements.txt
foreman run python hello.py
```

# Użycie
GET http://flask-ztis.herokuapp.com/consume

Powoduje następujące operacje:
* zarejestrowanie w generatorze zdarzeń
* zapisanie wynikow w bazie danych
* uruchomienie klasteryzacji
* wyslanie wynikow do logow: `http://immense-refuge-2812.herokuapp.com/results` w formacie:
```
"uuid": klasa-klasteryzacji
```

Przykladowy wynik:
```
{"1586b0a5d4c44560998822324241fc66": 1, 
"2243f4bad94c4fe599d082f7094a72fa": 2,
"c7d9c8ba67ac4be388cf84a4ea5f0ef3": 0, 
...}

```
* Wyniki dostepne takze pod adresem `http://flask-ztis.herokuapp.com/result`

## ZTIS
### List wszystkich danych
[GET] http://flask-ztis.herokuapp.com/  
[GET] http://flask-ztis.herokuapp.com/data

### Dodanie nowego wpisu
[POST] http://flask-ztis.herokuapp.com/data

Np.:
```
curl -X POST [url] -d "data=tekst"
```

### Mock generatora danych
[GET] http://flask-ztis.herokuapp.com/mock

### Konsumowanie eventow
[POST] http://flask-ztis.herokuapp.com/consume

Np.:
```
curl -X POST [url] -d "address=http://flask-ztis-herokuapp.com/mock"
```
