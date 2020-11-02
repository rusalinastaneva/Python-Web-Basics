from django.core.exceptions import ValidationError
from django.test import TestCase

from testing_app.models import Profile


class ProfileModelTests(TestCase):

    def test_createProfile_whenValidEgn_shouldCreateTheProfile(self):
        name = 'Rossy'
        age = 33
        egn = '1234567890'

        profile = Profile(
            name=name,
            age=age,
            egn=egn
        )
        profile.full_clean()
        profile.save()

    def test_createProfile_whenEgnContainsLetters_shouldRaise(self):
        name = 'Rossy'
        age = 33
        egn = '12A4567890'

        with self.assertRaises(ValidationError) as context:

            profile = Profile(
                name=name,
                age=age,
                egn=egn
            )
            profile.full_clean()
            profile.save()
        self.assertIsNotNone(context.exception)
