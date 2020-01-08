import unittest
import hansKode

class TestHansKode(unittest.TestCase):

    def setUp(self):
        self.koden = hansKode


    def test_vars(self):

        self.assertIsNotNone(self.koden.user)
        self.assertIsNotNone(self.koden.alias)
        self.assertIsNotNone(self.koden.enemy)
        self.assertIsNotNone(self.koden.greeting)


    def test_outputNames(self):

        if(self.koden.user == "Bruce Wayne"):
            self.assertEqual(self.koden.alias, "Batman")
            self.assertEqual(self.koden.enemy, "The Joker")
            self.assertEqual(self.koden.greeting, "You are the hero Gothamdeserves, but not the one it needs right now")

        elif(self.koden.user == "Katniss Everdeen"):
            self.assertEqual(self.koden.alias, "Mockingjay")
            self.assertEqual(self.koden.enemy, "President Snow")
            self.assertEqual(self.koden.greeting, "May the odds beever in your favour")

        else:
            self.assertEqual(self.koden.alias, "Programmer")
            self.assertEqual(self.koden.enemy, "The Compiler")
            self.assertEqual(self.koden.greeting, "You are the 5%")


    def test_userIsString(self):
        self.assertIs(self.koden.user, str(self.koden.user))


if __name__ == "__main__":
    unittest.main()
