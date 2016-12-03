from django.test import Client, SimpleTestCase


class AdminTest(SimpleTestCase):
    def setUp(self):
        self.client = Client()

    def test_redirects_to_login_page(self):
        response = self.client.get('/admin')
        self.assertRedirects(
            response, '/admin/', status_code=301, target_status_code=302)

    def test_loads_login_page(self):
        response = self.client.get('/admin/login/?next=/admin/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            '<input type="submit" value="Log in" />' in str(response.content))
