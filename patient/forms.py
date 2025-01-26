from django.forms import ModelForm
from .models import Patient

class QucikPatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['name','age','gender','details','medicine_detail','amount','next_visit']

    def __init__(self, *args, **kwargs):
        super(QucikPatientForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

class PatientForm(ModelForm):
    class Meta:
        model =  Patient
        fields = ['name','age','gender','mobile','address','details','medicine_detail','amount','note','next_visit']

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        self.fields['next_visit'].required = False
        self.fields['address'].widget.attrs['rows'] = '5'
        self.fields['details'].widget.attrs['rows'] = '5'
        self.fields['medicine_detail'].widget.attrs['rows'] = '5'
        self.fields['note'].widget.attrs['rows'] = '3'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
