from django import forms
from .models import Computer,ComputerHistory,Operating_system


class ComputerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ComputerForm, self).__init__(*args, **kwargs)
        self.fields['operating_system'].empty_label = "-SELECT OS-"


    class Meta:
        model=Computer
        #fields="__all__"
        fields=['computer_name','IP_address','operating_system','MAC_address','users_name','location','purchase_date']

class ComputerSearchForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ComputerSearchForm, self).__init__(*args, **kwargs)
        self.fields['computer_name'].required = False

    class Meta:
        model=Computer
        fields=['computer_name','export_to_CSV']
        labels={
            'export_to_CSV':'Export to CSV'
        }


    class Meta:
        model=ComputerHistory
        fields=['computer_name','users_name','export_to_CSV']
        labels={
            'export_to_CSV':'Export to CSV'
        }


class OperatingSystemForm(forms.ModelForm):
    class Meta:
        model = Operating_system
        fields = ['operating_system']


