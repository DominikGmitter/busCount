from unittest import TestCase
from funkcie import pocet_prostriedkov
from funkcie import celkova_cena


class Test(TestCase):
    #def test_pocet_prostriedkov(self):
        #self.fail()

    def test_pocet_prostiedkov_pocet_nie_int(self):
        with self.assertRaises(TypeError):
            pocet_prostriedkov('5')

    def test_pocet_prostriedkov_pocet_16(self):
        vysledok = {'mini': 2, 'bus': 0}
        self.assertEqual(vysledok, pocet_prostriedkov(16))

    def test_pocet_prostriedkov_pocet_30(self):
        vysledok = {'bus': 0, 'mini': 2}
        self.assertEqual(vysledok, pocet_prostriedkov(30))

    def test_pocet_prostriedkov_pocet_int_zaporny(self):
        with self.assertRaises(ValueError):
            pocet_prostriedkov(-5)

    def test_pocet_prostriedkov_pocet_cestujucich_int_nula(self):
        with self.assertRaises(ValueError):
            pocet_prostriedkov(0)

    def test_prostriedkov_1minibus(self):
        vysledok = {'mini': 1, 'bus': 0}
        self.assertEqual(vysledok, pocet_prostriedkov(5))

    def test_prostriedkov_1autobus(self):
        vysledok = {'mini': 0, 'bus': 1}
        self.assertEqual(vysledok, pocet_prostriedkov(49))

    def test_prostriedkov_1minibus_1autobus(self):
        vysledok = {'mini': 1, 'bus': 1}
        self.assertEqual(vysledok, pocet_prostriedkov(52))

    def test_prostriedkov_1minibus_2autobus(self):
        vysledok = {'mini': 1, 'bus': 2}
        self.assertEqual(vysledok, pocet_prostriedkov(103))

    def test_prostriedkov_prave_1autobus(self):
        vysledok = {'mini': 0, 'bus': 1}
        self.assertEqual(vysledok, pocet_prostriedkov(51))

    def test_prostriedkov_prave_1minibus(self):
        vysledok = {'mini': 1, 'bus': 0}
        self.assertEqual(vysledok, pocet_prostriedkov(15))

    def test_celkova_cena_pocet_zaporny(self):
        with self.assertRaises(ValueError):
            celkova_cena(-1, -2.5)

    def test_celkova_cena_1bus_1km(self):
        vysledok = (f'Cena : {0.87} eur')
        self.assertAlmostEqual(vysledok, celkova_cena(50, 1))

    def test_celkova_cena_1minibus_3km(self):
        vysledok = (f'Cena : {1.2} eur')
        self.assertAlmostEqual(vysledok, celkova_cena(14, 3))

    def test_celkova_cena_6bus_1km(self):
        vysledok = (f'Cena : {5.62} eur')
        self.assertAlmostEqual(vysledok, celkova_cena(307, 1))

    def test_celkova_cena_1bus_1minibus_10km(self):
        vysledok = (f'Cena : {12.7} eur')
        self.assertAlmostEqual(vysledok, celkova_cena(53, 10))


