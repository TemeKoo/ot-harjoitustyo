```mermaid
 classDiagram
       MonopoliPeli "1" -- "2" Noppa
      Raha "1" -- "1" Pelaaja
      Ruutu -- Ruutu
      Ruutu <|-- Aloitusruutu
      Ruutu <|-- Vankila
      Ruutu <|-- Katu
      Ruutu <|-- AsemaLaitos
      MonopoliPeli "1" -- "1" Pelilauta
      MonopoliPeli "1" -- "2..8" Pelaaja
      Pelaaja "1" -- "1" Pelinappula
      Pelinappula --> "1" Ruutu
      Pelilauta "1" -- "40" Ruutu
      Katu "1" -- "0..4" Talo
      Katu "1" -- "0..1" Hotelli
      Ruutu -- Toiminto
      Toiminto -- Kortti
      SattumaYhteismaa --|> Ruutu
      Kortti "*" -- "*" SattumaYhteismaa
      MonopoliPeli "1" -- "1" Aloitusruutu
      MonopoliPeli "1" -- "1" Vankila
      class MonopoliPeli
      class Pelilauta
      class Pelaaja
      class Pelinappula
      class Noppa
      class Ruutu
      class Aloitusruutu
      class Vankila
      class SattumaYhteismaa
      class AsemaLaitos
      class Katu
      class Toiminto
      class Kortti
      class Talo
      class Hotelli
      class Raha
```
