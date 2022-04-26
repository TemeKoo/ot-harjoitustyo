# Alustava vaatimusmäärittely

## Sovelluksen kuvaus

Sovelluksesta on tarkoitus tulla Tower Defense tyylinen peli, joka on toteutettu pygamella.

## Suunnitellut toiminnallisuudet

### Ennen peliä

- [ ] Pelissä on jonkinlainen aloitusnäyttö
  - [ ] Pelaaja pystyy valitsemaan tason sekä vaikeusasteen ja aloittamaan pelin
  - [ ] Pelaaja pystyy vaihtamaan mahdollisia asetuksia
  - [ ] Pelaaja pystyy sammuttamaan pelin
- Mahdollisia asetuksia
  - [ ] Näppäinten toimintojen vaihtaminen
  - [ ] Resoluution vaihtaminen

### Pelissä

- Pelin tavoite on puolustaa reitin päässä olevaa tukikohtaa, jonka viholliset koittavat tuhota. 
- [x] Puolustaminen tapahtuu torneilla, joita pelaaja voi rakentaa reitin ulkopuolelle.
- [x] Kun pelaaja aloittaa pelin, vihollisia alkaa tulla aaltoina reitin toisesta päästä tukikohtaa päin
- [x] Kun vihollinen on tornin kantaman sisällä, torni voi ampua ja vahingoittaa vihollista.
- [ ] Jos vihollinen pääsee tukikohtaan asti, tukikohta vahingoittuu.
- [ ] Pelaaja häviää tason, jos tukikohta tuhoutuu.
- [ ] Pelaaja voittaa tason, jos hän saa päihitettyä kaikki vihollisaallot.

## Ideoita

- Ideoita tornityypeistä
  - [x] Tavallinen torni, joka voi ampua kerralla yhtä vihollista
  - [ ] Räjähdetorni, joka ampuu hitaammin kuin tavallinen torni, mutta ammus vahingoittaa montaa vihollista
  - [ ] Tarkka-ampujatorni, joka ampuu erittäin hitaasti, mutta tekee paljon vahinkoa pitkällä kantamalla
  - [ ] Aluetorni, joka voi kerralla vahingoittaa kaikkia vihollisia kantamansa sisällä

- Ideoita vihollistyypeistä
  - [x] Normaali vihollinen: keskiverto nopeus, keskiverto kestävyys 
  - [ ] Parvi: nopeita, heikkoja, tulee suurissa määrissä
  - [ ] Tankki: hitaita, kestäviä
  - [ ] Pomo: erittäin kestävä, tulee yksin
