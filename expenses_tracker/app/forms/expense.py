from django import forms

from app.forms.common import DisabledFormMixin
from app.models import Expense


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        # fields = '__all__'
        exclude = ('profile',)


# Make all the fields in Expense form Read Only & Disabled when deleting
class DeleteExpenseForm(ExpenseForm, DisabledFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        DisabledFormMixin.__init__(self)
