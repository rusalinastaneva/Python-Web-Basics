from django import forms
from django.core.exceptions import ValidationError

from books.models import Book


class BookForm(forms.ModelForm):
    # All the fields will have the class form-control added
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_form_control_class_to_all_fields()

    def add_form_control_class_to_all_fields(self):
        for (_, field) in self.fields.items():
            if 'class' in field.widget.attrs:
                field.widget.attrs['class'] = field.widget.attrs['class'] + 'form-control'
            else:
                field.widget.attrs['class'] = 'form-control'

    def clean_pages(self):
        pages = self.cleaned_data['pages']
        if pages <= 0:
            raise ValidationError(f'Pages should be a positive number. Now they are {pages}')
        return pages

    class Meta:
        model = Book
        # fields = ['title', 'pages', 'author']
        # Show all the fields excluding the mentioned fields:
        # exclude = ['pages']
        fields = '__all__'

# class BookForm(forms.ModelForm):
#     class Meta:
#         model = Book
#         fields = '__all__'
#         widgets = {
#             'title': forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                 }
#             ),
#             'pages': forms.NumberInput(
#                 attrs={
#                     'class': 'form-control',
#                 }
#             ),
#             'description': forms.Textarea(
#                 attrs={
#                     'class': 'form-control',
#                 }
#             ),
#             'author': forms.TextInput(
#                 attrs={
#                     'class': 'form-control',
#                 }
#             ),
#         }
