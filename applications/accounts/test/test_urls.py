from applications.accounts.views import RegisterApiView, ChangePasswordApiView, ActivationApiView
from django.urls import reverse, resolve
import unittest

class Test_urls(unittest.TestCase):

    def test_register_is_resolved(self):
        url = reverse('RegisterApiView')
        resolved = resolve(url)
        self.assertEqual(resolved.func.__name__, RegisterApiView.as_view().__name__)

    def test_change_password_is_resolved(self):
        url = reverse('ChangePasswordApiView')
        resolved = resolve(url)
        view_instance = ChangePasswordApiView.as_view()
        self.assertEqual(resolved.func.__name__, view_instance.__name__)

    def test_activation_code_is_resolved(self):
        import uuid
        activation_code = str(uuid.uuid4())
        url = reverse('ActivationApiView', args=[activation_code])
        resolved = resolve(url)
        view_instance = ActivationApiView.as_view()
        self.assertEqual(resolved.func.__name__, view_instance.__name__)








