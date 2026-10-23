import unittest

from main import app


class PaginaTest(unittest.TestCase):
    def test_pagina_del_ejercicio(self):
        with app.test_client() as client:
            response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_data(as_text=True), "P\u00e1gina de Prueba")


if __name__ == "__main__":
    unittest.main()
