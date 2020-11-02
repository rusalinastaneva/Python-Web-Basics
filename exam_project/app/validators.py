from django.core.exceptions import ValidationError


def validate_time_is_negative_or_zero(value):

    if value <= 0:
        raise ValidationError('Please insert a positive value. Time cannot be negative or zero!')
