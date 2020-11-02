from django.core.exceptions import ValidationError


def validate_does_contain_spaces(value):

    # any - Return True if bool(x) is True for any value x in the iterable.
    result = any(' ' in x for x in value)

    if result:
        raise ValidationError('Cannot contain spaces')