from django import forms

from .models import BasimYili,YayinEvi,Kitap
# Sinif,KitapTuru,DersTuru,Kitap

class PersonCreationForm(forms.ModelForm):
    class Meta:
        model = Kitap
        fields = '__all__'


    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['yayinevi'].queryset = YayinEvi.objects.none()
        print('or')
        if 'basimyili' in self.data:
            print('yıl var ')
            try:
                print('deniyoruz...')
                basimyiliId = int(self.data.get('basimyili'))
                self.fields['yayinevi'].queryset = YayinEvi.objects.filter(basimyiliId=basimyiliId).order_by('name')
            except (ValueError, TypeError):
                print("except")
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['yayinevi'].queryset = self.instance.basimyili.yayinevi_set.order_by('name')
        
    
