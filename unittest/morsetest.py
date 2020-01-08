import unittest
import morse

class TestDigtinary(unittest.TestCase):

    def test_morsekode(self):
        #tjekker om det er den korekte type
        self.assertIsInstance(morse.morseCode, dict)

        #tjekker om alle keys er tal eller bogstaver
        for e in morse.morseCode.keys():
            self.assertIsTrue(e.isalpha() or e.isdigit() or e in ".,-!?: ", msg ="testen er felet ved: " + e)

        # kontrolere at alle values er morse tegn
        for e in morse.morseCode.values():
            self.assertTrue("." in e or "-" in e or e == "")
            self.assertFalse(e.isalpha())


class testTranslate(unittest.TestCase):

    def test_translate(self):
        


if __name__ == "__main__":
    unittest.main()
