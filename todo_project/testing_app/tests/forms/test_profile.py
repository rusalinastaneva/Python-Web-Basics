from django.test import TestCase

from testing_app.forms.profile import ProfileForm
from testing_app.models import Profile


class ProfileFormTests(TestCase):

    def test_saveProfileForm_whenValidEgn_shouldBeValid(self):
        name = 'Rossy'
        age = 33
        egn = '1234567890'

        data = {
            'name': name,
            'age': age,
            'egn': egn,
        }
        form = ProfileForm(data)
        self.assertTrue(form.is_valid())

    def test_saveProfileForm_whenEgnContainsLetters_shouldBeInvalid(self):
        name = 'Rossy'
        age = 33
        egn = '12Add4567890'

        data = {
            'name': name,
            'age': age,
            'egn': egn,
        }
        form = ProfileForm(data)

        self.assertFalse(form.is_valid())

    def test_saveProfileForm_whenEgnContainsOnlyDigitsBut9_shouldBeInvalid(self):
        name = 'Rossy'
        age = 33
        egn = '123456780'

        data = {
            'name': name,
            'age': age,
            'egn': egn,
        }
        form = ProfileForm(data)

        self.assertFalse(form.is_valid())

    def test_saveProfileForm_whenEgnContainsOnlyDigitsBut11_shouldBeInvalid(self):
        name = 'Rossy'
        age = 33
        egn = '12345678011'

        data = {
            'name': name,
            'age': age,
            'egn': egn,
        }
        form = ProfileForm(data)

        self.assertFalse(form.is_valid())