from django import forms
from .models import MemberInfo, Dependant_info

class MemberInfoForm(forms.ModelForm):
    class Meta:
        model = MemberInfo
        fields = [
        'f_name','l_name','m_name','mwaka','address','residence','gender','married',
        'mwanamke','mwanaume','phone_number','member_id','age','amount','image'
        ]
        widgets = {
            'f_name': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'enter first name'}),
            'l_name': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'enter last name'}),
            'address': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'enter address'}),
            'residence': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'enter area of residence'}),
            'phone_number': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'enter phone number'}),
            'm_name': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'enter middle name'}),
            # 'mwanaume': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'enter idadi ya wanaume'}),
            'member_id': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'enter member ID'}),
            'amount': forms.NumberInput(attrs = {'class':'form-control', 'placeholder':'enter amount'}),
        }

class DependantInfoForm(forms.ModelForm):
    class Meta:
        model = Dependant_info
        fields = [
        'dependant_id','wazazi','watoto_above','watoto_below','watoto_yatima','watoto_wakulea'
        ]
        widgets = {
            # 'dependant_id': forms.TextInput(attrs = {'class':'form-control', 'placeholder':'enter member id'}),
            'wazazi': forms.NumberInput(attrs = {'class':'form-control'}),
            'watoto_above': forms.NumberInput(attrs = {'class':'form-control'}),
            'watoto_below': forms.NumberInput(attrs = {'class':'form-control'}),
            'watoto_yatima': forms.NumberInput(attrs = {'class':'form-control'}),
            'watoto_wakulea': forms.NumberInput(attrs = {'class':'form-control'}),
        }
