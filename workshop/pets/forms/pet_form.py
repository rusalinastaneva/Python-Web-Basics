from django import forms

from pets.models import Pet


class PetForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_form_control_class_to_all_fields()

    def add_form_control_class_to_all_fields(self):

        for (_, field) in self.fields.items():
            if 'class' in field.widget.attrs:
                field.widget.attrs['class'] = field.widget.attrs['class'] + 'form-control'
            else:
                field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Pet
        fields = '__all__'
        widgets = {
            'image_url': forms.TextInput(
                attrs={
                    'id': 'img_input',
                }
            )
        }
