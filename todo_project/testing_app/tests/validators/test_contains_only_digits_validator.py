from django.core.exceptions import ValidationError
from django.test import TestCase

from testing_app.validators import contains_only_digits


class ContainsOnlyDigitsValidatorTests(TestCase):
    def test_validate_whenValueContainsOnlyDigits_shouldDoNothing(self):
        contains_only_digits('123')
        self.assertTrue(True)

    def test_validate_whenValueIsEmpty_shouldDoNothing(self):
        contains_only_digits('')
        # This can be skipped in this case:
        # self.assertTrue(True)

    def test_validate_whenValueContainsLetters_shouldDoNothing(self):
        with self.assertRaises(ValidationError) as context:
            contains_only_digits('34f')
        self.assertIsNotNone(context.exception)