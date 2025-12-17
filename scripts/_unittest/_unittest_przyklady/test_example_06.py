import unittest
import sys
import os

class TestDecorators(unittest.TestCase):
    """Przykłady dekoratorów unittest"""
    
    # ===========================================
    # @unittest.skip - ZAWSZE pomija test
    # ===========================================
    
    @unittest.skip("Funkcja jeszcze nie gotowa")
    def test_not_implemented_yet(self):
        """Ten test zostanie ZAWSZE pominięty"""
        # Kod który nie działa
        raise NotImplementedError("TODO: Implement me!")
    
    # ===========================================
    # @unittest.skipIf - pomija JEŚLI warunek prawdziwy 
    # ===========================================
    
    @unittest.skipIf(sys.platform == "win32", "Nie działa na Windows")
    def test_unix_only(self):
        """Pomija na Windows"""
        self.assertTrue(True)  # Prosty test
    
    @unittest.skipIf(sys.version_info < (3, 8), "Wymaga Python 3.8+")
    def test_new_python_feature(self):
        """Pomija na starym Pythonie"""
        self.assertTrue(True)
    
    # ===========================================
    # @unittest.skipUnless - pomija CHYBA ŻE warunek prawdziwy
    # ===========================================
    
    @unittest.skipUnless(sys.platform == "linux", "Tylko na Linuksie")
    def test_linux_only(self):
        """Uruchomi się TYLKO na Linuksie"""
        self.assertTrue(True)
    
    @unittest.skipUnless(os.path.exists("/usr/bin/git"), "Wymaga gita")
    def test_requires_git(self):
        """Uruchomi się TYLKO gdy git zainstalowany"""
        self.assertTrue(True)
    
    # ===========================================
    # @unittest.expectedFailure - test POWINIEN się nie udać
    # ===========================================
    
    @unittest.expectedFailure
    def test_known_bug(self):
        """Ten test MA się nie udać - to oczekiwane!"""
        self.assertEqual(1, 2, "Znany bug - 1 != 2")
    
    @unittest.expectedFailure  
    def test_broken_feature(self):
        """Funkcja jest zepsuta, ale wiemy o tym"""
        broken_function_that_crashes()  # Ta funkcja nie istnieje!
    
    # ===========================================
    # Kombinacje - skip w metodzie
    # ===========================================
    
    def test_conditional_skip_inside(self):
        """Pomijanie wewnątrz testu"""
        if not hasattr(os, 'fork'):
            self.skipTest("os.fork nie dostępny")
        
        # Test który wymaga fork
        self.assertTrue(hasattr(os, 'fork'))


# ===========================================
# CAŁĄ KLASĘ można też skipować
# ===========================================

@unittest.skip("Cała klasa wyłączona")
class TestSkippedClass(unittest.TestCase):
    """Wszystkie testy w tej klasie będą pominięte"""
    
    def test_one(self):
        self.assertTrue(True)
    
    def test_two(self):  
        self.assertTrue(True)


@unittest.skipIf(sys.platform == "win32", "Klasa nie dla Windows")
class TestUnixClass(unittest.TestCase):
    """Cała klasa tylko dla Unix"""
    
    def test_unix_feature(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main(verbosity=2)