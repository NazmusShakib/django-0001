from django.test import TestCase
from django.urls import reverse


class CompanyTests(TestCase):
    def test_company_view_status_code(self):
        url = reverse('company.list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
