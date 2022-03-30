```mermaid
 classDiagram
      MonopoliPeli "1" -- "1" Pelilauta
      MonopoliPeli "1" -- "2..8" Pelaaja
      MonopoliPeli "1" -- "2" Noppa
      Pelaaja "1" -- "1" Pelinappula
      Pelinappula --> "1" Ruutu
      Ruutu -- Ruutu
      Pelilauta "1" -- "40" Ruutu
      class MonopoliPeli
      class Pelilauta
      class Pelaaja
      class Pelinappula
      class Noppa
      class Ruutu
```
