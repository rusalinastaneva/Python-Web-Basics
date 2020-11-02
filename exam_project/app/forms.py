from django import forms

from app.common import DisabledFormMixin
from app.models import Recipe


class RecipeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(RecipeForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Recipe
        fields = '__all__'


class DeleteRecipeForm(RecipeForm, DisabledFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        DisabledFormMixin.__init__(self)
