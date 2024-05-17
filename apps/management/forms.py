from django import forms

from apps.management.models import Order


class OrderModelForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('query',)
        widgets = {'query': forms.TextInput(attrs={'placeholder': 'Введите поисковой запроc'})}
        labels = {'query': ''}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control text-center'})
