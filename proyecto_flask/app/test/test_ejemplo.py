import unittest
from metodo import calculo_primo

class Test_Funciones(unittest.TestCase):

    def test_primo(self):
        self.assertEqual(calculo_primo(3),'1, 2, 3, ','Error no coinciden')
        self.assertEqual(calculo_primo(10),'1, 2, 3, 5, 7, ','Error no coinciden')
        self.assertEqual(calculo_primo(11),'1, 2, 3, 5, 7, 11, ','Error no coinciden')
        self.assertEqual(calculo_primo(20),'1, 2, 3, 5, 7, 11, 13, 17, 19, ','Error no coinciden')
        self.assertEqual(calculo_primo(35),'1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, ','Error no coinciden')

if __name__ == '__main__':
    unittest.main()