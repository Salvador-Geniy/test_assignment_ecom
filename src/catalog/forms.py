from django import forms

from catalog.models import GoodModel, ImageModel


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class GoodCreateForm(forms.ModelForm):
    images = MultipleFileField()
    short_description = forms.CharField(max_length=100, empty_value="")
    name = forms.CharField(max_length=100)
    description = forms.Textarea()
    price = forms.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        model = GoodModel
        fields = ('category', 'name', 'description', 'price', 'images', 'short_description')



