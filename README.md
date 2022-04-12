# Ohjelmistotekniikka, harjoitustyö 

Tämä on harjoitustyöni Helsingin Yliopiston kurssille [Ohjelmistotekniikka](https://ohjelmistotekniikka-hy.github.io/).

# Tower Defense peli (nimi ei lopullinen)


## Dokumentaatio

[Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](dokumentaatio/tyoaikakirjanpito.md)

[Changelog](dokumentaatio/changelog.md)

[Arkkitehtuuri](dokumentaatio/arkkitehtuuri.md)

## Asennus

1. Asenna Poetry: https://python-poetry.org/
2. Kloonaa repositorio omalle koneellesi
3. Asenna projektin riippuvuudet Poetryllä komennolla:
```
poetry install
```

## Komennot

Aja ohjelma:
```
poetry run invoke start
```
Suorita testit:
```
poetry run invoke test
```
Luo testikattavuusraportti:
```
poetry run invoke coverage-report
```
