# Changelog

## Viikko 3

Paljon on koodia, mutta ei vielä paljon toiminnallisuutta

### Pelissä
- Pelikenttä näkyy ruudun kulmassa
- Peli luo yhden tornin ruudun keskelle jota voi raahata hiirellä
- Torneja voi luoda lisää aloittamalla hiirellä raahaamisen "Place Tower"-napista

### Projekti
- Hahmoteltiin ja jaoteltiin koodia paketteihin ja luokkiin
- Kaikkia paketteja ja luokkia ei vielä käytetä
- Kansiosta `assets` löytyy pelin tekstuureja ja tasot sisältävä `json`-tiedosto
- Funktiossa `main` vielä paljon toiminnallisuutta joka tarkoitus siirtää omiin luokkiinsa

### Koodi
- Lisättiin funktio `main`, joka pyörittää peliä
- Lisättiin luokka `helpers.level_loader.LevelLoader`, joka lataa pelikentän `json`-tiedostosta
- Lisättiin tyhjä luokka `helpers.ui_helper.UiHelper`, jonka on ehkä tarkoitus tulevaisuudessa auttaa kätttöliittymän kanssa 
- Lisättiin luokka `game_objects.field.Field`, joka luo ja piirtää pelikentän
- Lisättiin luokka `game_objects.tower.Tower`, joka vastaa tornin käsittelystä
- Lisättiin tiedostoon `game_objects.tiles` luokat `GenericTile`, `PathTile`, `BuildableTile`, ja `BaseTile`, joita on tarkoitus tulevaisuudessa käyttää pelikentän ruutujen käsittelyyn
- Lisättiin luokka `ui.buttons.GenericButton`, joka auttaa nappien tekemisessä
- Lisättiin luokka `ui.buttons.TowerButton`, joka tekee napin jolla voi luoda tornin
- Lisättiin tyhjä luokka `ui.tower_select.TowerselectScreen`, jonka on tulevaisuudessa tarkoitus käsitellä tornien luomiseen käytettäviä nappeja
- Lisättiin tyhjä luokka `ui.buttons.MenuButton`, jonka on tulevaisuudessa tarkoitus käsitellä käyttöliittymän nappeja
- Lisättiin luokka `logic.event_handler.EventHandler`, joka käy läpi pygamen eventit ja käsittelee ne
- Lisättiin luokka `logic.game_loop.GameLoop`, jonka on tarkoitus tulevaisuudessa huolehtia pelin pyörittämisestä
- Lisättiin tiedostoon `logic.level` tyhjät luokat `Level` ja `LevelScreen`, joiden on ehkä tulevaisuudessa tarkoitus käsitellä pelitasoja
- Lisättiin tyhjä luokka `logic.tower_placement.TowerPlacer`, jonka on tulevaisuudessa tarkoitus auttaa tornien sijoittamisessa pelikentälle
- Lisättiin luokka `render.renderers.Renderer`, joka huolehtii ruudun piirtämisestä
- Lisättiin tiedostoon `render.renderers` luokat `GenericRenderer`, `UiRenderer`, ja `GameRenderer`, joiden on tarkoitus tulevaisuudessa auttaa pelikentän ja käyttöliittymän piirtämisessä

Saatoin missata jotain, tuli kirjoitettua sen verran koodia
