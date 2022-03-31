Nuolien selitys:
```mermaid
sequenceDiagram
  participant esimerkki
  participant olio
  
  esimerkki -) olio: esimerkki luo olion
  esimerkki ->> olio: esimerkki kutsuu oliota
  activate olio
  olio -->> esimerkki: olio palauttaa jotain esimerkille
  deactivate olio
```


```mermaid
sequenceDiagram
  participant main
  participant laitehallinto
  participant kallen_kortti
  participant rautatietori
  participant ratikka6
  participant bussi244
  participant lippu_luukku
  
  activate main

  main -) laitehallinto: HKLLaitehallinto()
  main -) rautatietori: Lataajalaite()
  main -) ratikka6: Lukijalaite()
  main -) bussi244: Lukijalaite()
  
  main ->> laitehallinto: lisaa_lataaja(rautatietori)
  main ->> laitehallinto: lisaa_lukija(ratikka6)
  main ->> laitehallinto: lisaa_lukija(bussi244)
  
  main -) lippu_luukku: Kioski()
  main ->> lippu_luukku: osta_matkakortti("Kalle")
  activate lippu_luukku
  lippu_luukku -) kallen_kortti: Matkakortti("Kalle")
  lippu_luukku -->> main: kallen_kortti
  deactivate lippu_luukku

  main ->> rautatietori: lataa_arvoa(kallen_kortti, 3)
  activate rautatietori
  rautatietori ->> kallen_kortti: kasvata_arvoa(3)
  rautatietori -->> main: 
  deactivate rautatietori

  main ->> ratikka6: osta_lippu(kallen_kortti, 0)
  activate ratikka6
  ratikka6 ->> kallen_kortti: arvo
  activate kallen_kortti
  kallen_kortti -->> ratikka6: 3
  deactivate kallen_kortti
  ratikka6 ->> kallen_kortti: vahenna_arvoa(1.5)
  ratikka6 -->> main: True
  deactivate ratikka6

  main ->> bussi244: osta_lippu(kallen_kortti, 2)
  activate bussi244
  bussi244 ->> kallen_kortti: arvo
  activate kallen_kortti
  kallen_kortti -->> bussi244: 1.5
  deactivate kallen_kortti
  bussi244 -->> main: False
  deactivate bussi244

  deactivate main
```
