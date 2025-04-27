import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from todor import create_app

class ToDoTestCase(unittest.TestCase):
    def setUp(self):
        """Configuración antes de cada prueba"""
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()

    def test_homepage(self):
        """Probar que la página principal carga correctamente"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        """Probar que la página de login carga correctamente"""
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()


class ToDoTestCase(unittest.TestCase):
    def setUp(self):
        """Configuración antes de cada prueba"""
        self.app = create_app()
        self.app.testing = True
        self.client = self.app.test_client()

    def test_homepage(self):
        """Probar que la página principal carga correctamente"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        """Probar que la página de login carga correctamente"""
        response = self.client.get('/auth/login')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
