from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from my_app.models import Customer
from my_app.forms import UserForm



class PostTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="admin")
        Customer.objects.create(first_name=self.user1,
                            last_name="Admin",
                            email="we@wearetesting.com",
                            address='1720 E Belmont, Anaheim',
                            cc_number='345566788888')

    def test_customer_is_posted(self):
        """Customer is created"""
        cust1 = Customer.objects.get(last_name="Admin")
        self.assertEqual(cust1.email, "we@wearetesting.com")

    # def test_valid_form_data(self):
    #     form = UserForm({
    #         'email': "Just testing",
    #     })
    #     self.assertTrue(form.is_valid())
    #     custo1 = form.save(commit=False)
    #     Customer.first_name = self.user1
    #     custo1.save()
    #     self.assertEqual(custo1.last_name, "Admin")
    #     self.assertEqual(custo1.text, "Repeated tests make the app foul-proof")

    # def test_blank_form_data(self):
    #     form = UserForm({})
    #     self.assertFalse(form.is_valid())
    #     self.assertEqual(form.errors, {
    #         'email': ['This field is required.'],
    #         'username': ['This field is required.']
    #     })