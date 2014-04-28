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
