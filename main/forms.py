from django.forms import ModelForm
from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from ckeditor.widgets import CKEditorWidget

def calmax():
    n1=l1.objects.all().count();
    n2=l2.objects.all().count();
    n3=l3.objects.all().count();
    n4=l4.objects.all().count();
    return(n1+n2+n3+n4+1);



class layout1(ModelForm):
    class Meta:
        model=l1
        fields='__all__'  

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            if field == 'changing_seconds':
                new_data={
                'class':'form-control',
                'placeholder' : 'in seconds',
                'min': '0',
                'max': '20',
                'class':'form-control'
            }
            elif field == 'priority' :
                new_data = {
                    'min': '0',
                    'max': calmax,
                    'class':'form-control'
                }
            # elif field == 'page':
            #     new_data = {
            #         'editable' : 'false',
            #         'class' : 'form-control'
            #     }
            else:
                new_data={
                    'class':'form-control'
                }
            self.fields[str(field)].widget.attrs.update(new_data)

class layout2(ModelForm):

    

    class Meta:
        model=l2
        fields='__all__'  
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            if field == 'changing_seconds':
                new_data={
                'class':'form-control',
                'placeholder' : 'in seconds',
                'min': '0',
                'class':'form-control'
            }
            elif field == 'priority' :
                new_data = {
                    'min': '0',
                    'max': calmax,
                    'class':'form-control'
                }
            elif field == 'page':
                new_data = {
                    'editable' : 'False',
                    'class' : 'form-control'
                }
            else:
                new_data={
                    'class':'form-control'
                }
            self.fields[str(field)].widget.attrs.update(new_data)


class layout3(ModelForm):
    class Meta:
        model=l3
        fields='__all__'  

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            if field == 'changing_seconds':
                new_data={
                'class':'form-control',
                'placeholder' : 'in seconds',
                'min': '0',
                'class':'form-control'
            }
            elif field == 'priority' :
                new_data = {
                    'min': '0',
                    'max': calmax,
                    'class':'form-control'
                }
            elif field == 'page':
                new_data = {
                    'editable' : 'False',
                    'class' : 'form-control'
                }
            else:
                new_data={
                    'class':'form-control'
                }
            self.fields[str(field)].widget.attrs.update(new_data)
        

class layout4(ModelForm):
    class Meta:
        model=l4
        fields='__all__'  

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            if field == 'changing_seconds':
                new_data={
                'class':'form-control',
                'placeholder' : 'in seconds',
                'min': '0',
                'max': '20',
                'class':'form-control'
            }
            elif field == 'priority' :
                new_data = {
                    'min': '0',
                    'max': calmax,
                    'class':'form-control'
                }
            elif field == 'page':
                new_data = {
                    'editable' : 'False',
                    'class' : 'form-control'
                }
            else:
                new_data={
                    'class':'form-control'
                }
            self.fields[str(field)].widget.attrs.update(new_data)

class page(ModelForm):
    # content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model=pages
        fields='__all__'  
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
                new_data = {
                    # 'editable' : 'False',
                    'class' : 'form-control'
                }

        self.fields[str(field)].widget.attrs.update(new_data)


class layoutform(ModelForm):
    class Meta:
        model = layout_name
        fields = '__all__'


class dynamic_form(ModelForm):
    class Meta:
        model = dynamic_forms
        fields = '__all__'
        
class custom_data(ModelForm):
    class Meta:
        model = custom_layout_data
        fields = '__all__'

class Charfields(ModelForm):
    class Meta:
        model = charfield
        fields = '__all__'

class Imagefields(ModelForm):
    class Meta:
        model = Imagefield
        fields = '__all__'

class Videofields(ModelForm):
    class Meta:
        model = videofield
        fields = '__all__'