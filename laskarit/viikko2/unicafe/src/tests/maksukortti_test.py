import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")
    
    def test_saldo_kasvaa_oikein(self):
        self.maksukortti.lataa_rahaa(500)
        self.assertEqual(str(self.maksukortti), "saldo: 15.0")
    
    def test_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(str(self.maksukortti), "saldo: 5.0")
    
    def test_saldo_ei_mene_negatiiviseksi(self):
        self.maksukortti.ota_rahaa(1100)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")
    
    def test_ota_rahaa_palautusarvo_raha_riitti(self):
        palautusarvo = self.maksukortti.ota_rahaa(500)
        self.assertEqual(palautusarvo, True)
    
    def test_ota_rahaa_palautusarvo_raha_ei_riittanyt(self):
        palautusarvo = self.maksukortti.ota_rahaa(1100)
        self.assertEqual(palautusarvo, False)