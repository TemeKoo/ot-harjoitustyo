import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(500)

    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)
    
    def test_kassapaate_alustetaan_oikein(self):
        self.assertEqual((self.kassapaate.kassassa_rahaa, self.kassapaate.edulliset, self.kassapaate.maukkaat), (100000, 0, 0))
    
    def test_kateisosto_edullinen_onnistuu_tasarahalla(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual((vaihtoraha, self.kassapaate.kassassa_rahaa, self.kassapaate.edulliset), (0, 100240, 1))
    
    def test_kateisosto_edullinen_onnistuu_vaihtorahalla(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual((vaihtoraha, self.kassapaate.kassassa_rahaa, self.kassapaate.edulliset), (260, 100240, 1))

    def test_kateisosto_edullinen_ei_onnistu(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual((vaihtoraha, self.kassapaate.kassassa_rahaa, self.kassapaate.edulliset), (200, 100000, 0))


    def test_kateisosto_maukas_onnistuu_tasarahalla(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual((vaihtoraha, self.kassapaate.kassassa_rahaa, self.kassapaate.maukkaat), (0, 100400, 1))

    def test_kateistosto_maukas_onnistuu_vaihtorahalla(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual((vaihtoraha, self.kassapaate.kassassa_rahaa, self.kassapaate.maukkaat), (100, 100400, 1))

    def test_kateisosto_maukas_ei_onnistu(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual((vaihtoraha, self.kassapaate.kassassa_rahaa, self.kassapaate.maukkaat), (300, 100000, 0))

    def test_korttiosto_edullinen_onnistuu(self):
        palautusarvo = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual((palautusarvo, self.maksukortti.saldo, self.kassapaate.edulliset), (True, 260, 1))

    def test_korttiosto_edullinen_ei_onnistu(self):
        self.maksukortti.ota_rahaa(300)
        palautusarvo = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual((palautusarvo, self.maksukortti.saldo, self.kassapaate.edulliset), (False, 200, 0))

    def test_korttiosto_maukas_onnistuu(self):
        palautusarvo = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual((palautusarvo, self.maksukortti.saldo, self.kassapaate.maukkaat), (True, 100, 1))

    def test_korttiosto_maukas_ei_onnistu(self):
        self.maksukortti.ota_rahaa(200)
        palautusarvo = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual((palautusarvo, self.maksukortti.saldo, self.kassapaate.maukkaat), (False, 300, 0))

    def test_kortin_lataaminen_toimii(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 200)
        self.assertEqual((self.maksukortti.saldo, self.kassapaate.kassassa_rahaa), (700, 100200))
    
    def test_kortin_lataaminen_ei_onnistu_negatiivisella(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual((self.maksukortti.saldo, self.kassapaate.kassassa_rahaa), (500, 100000))