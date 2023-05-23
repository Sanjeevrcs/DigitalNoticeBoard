from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from .models import *
from .forms import *
from itertools import chain
from .decorators import unauth_user
from django.contrib.auth import authenticate,login,logout
import json
from django.views.decorators.csrf import csrf_exempt



@unauth_user
def loginpage(request):
    user=''
    text=''
    if request.method == 'POST':
        username = request.POST.get('username');
        password = request.POST.get('password');
        print('user=',username,' password=',password)
        user=authenticate(request,username=username,password=password)
        print('user = ',user)
        if user is not None:
            login(request,user)
            return redirect('main')
        else:
            text="account details doesn't exits"
    
    context={'text':text,'name':user}
    return render(request,'login.html',context)



# @login_required(login_url='login')
def logoutpage(request):
    logout(request)
    return redirect('login')


# @login_required(login_url='login')
def main(request):

    context = {}
    pageform = page()
    l_form = layoutform()
    totalpages = pages.objects.all();
    layout1 = l1.objects.all()
    layout2 = l2.objects.all()
    layout3 = l3.objects.all()
    layout4 = l4.objects.all()
    l_name = layout_name.objects.all()
    
    Totalpages = pages.objects.all().count()
    context = {
        'pageform' : pageform,
        'l_form' : l_form,
        'pages' : totalpages,
        'layout1' : layout1,
        'layout2' : layout2,
        'layout3' : layout3,
        'layout4' : layout4,
        'layout_name' : l_name,
        'Totalpages' : Totalpages
    }
    if request.method == 'POST':
        print("sanjeev");
        return create(request)
    return render(request,'main.html',context)

def create(request):
    if request.method =='POST':
        if 'createpageform' in request.POST:
            page_name = request.POST['pagename']
            print('page_name = ',page_name)
            try:
                checkpage = pages.objects.get(page_name=page_name);                
                return HttpResponse("pagename already exists");
            except:

                form = page(request.POST);
                # print('form is ',form)
                if form.is_valid():
                    form.save()
                    print(' page form validated successfully')
                    return redirect('forms',page_name=page_name)
                    # return redirect('template',page_name=p_name)
                else:
                    print("page name submitting form is not valid")
                    return redirect('forms',page_name=page_name)
        elif 'templatecreateform' in request.POST:
            print('success')
            l_name = request.POST['name']
            print('layout_name = ',l_name)
            try:
                checklayout = layout_name.objects.get(name=l_name);                
                return HttpResponse("pagename already exists");
            except:
                form = layoutform(request.POST);
                # print('form is ',form)
                if form.is_valid():
                    form.save()
                    print(' page form validated successfully')
                    return redirect('elementcreate',l_name=l_name)
                    # return redirect('template',page_name=p_name)
                else:
                    print("page name submitting form is not valid")
                    return redirect('elementcreate',l_name=l_name)
    else:
        return HttpResponse('nothing happened')

    


def data_sort(elem):
    return elem.priority

def template(request,page_name):

    context={}
    
    print('page name = ',page_name)
    
    page = pages.objects.get(pagename=page_name)

    data1=l1.objects.filter(pagename=page)
    data2=l2.objects.filter(pagename=page) 
    data3=l3.objects.filter(pagename=page)
    data4=l4.objects.filter(pagename=page)  

    data = list(chain(data1,data2,data3,data4))

    data.sort(key=data_sort)
    
    print('data = ',data)

    context = {'data':data}

    return render(request,'template.html',context)


def  test(request,page_name):

    context = {}
    page = pages.objects.get(pagename=page_name)
    layout_content_data = custom_layout_data.objects.filter(page_name=page)
    print('custom data = ',layout_content_data)  
    print(custom_layout_data.objects.all())

    arr = []

    for i in layout_content_data:
        print('value is ',i.layout_name)
        if i.layout_name not in arr:
            arr.append(i.layout_name)
    print('arr',arr)
    layout_data = []
    for i in arr:
        name = layout_name.objects.get(name=i)
        layout_data.append(elements_data.objects.filter(layout_name=name)) 

    print(arr)
    print('layout content data is ',layout_content_data)
    print('layout data is',layout_data)

    form_data = {}
    
    for i in arr:    
        form_data[i]  = dynamic_forms_data.objects.get(layout_name=i)
    print('form_data',form_data)    

    data = {}
    for i in arr:
        data[i] = {}

    context={'data':data,'layout_data':layout_data,'layout_content_data':layout_content_data,'form_data':form_data}

    return render(request,'page.html',context)

def forms(request,page_name):
    context={}
    form1=layout1()
    form2=layout2()
    form3=layout3()
    form4=layout4()
    d_form = dynamic_forms_data.objects.all()
    createform = page()
    print(page_name)
    context={  
        'pageform' : createform, 
        'form1':form1,
        'form2':form2,
        'form3':form3,
        'form4':form4,
        'd_form' : d_form,
        }
    
    if request.method=='POST':
        if 'createpageform' in request.POST:
            return create(request)
        request.POST._mutable = True
        if int(request.POST['changing_seconds'])<20:
            request.POST['changing_seconds']=int(request.POST['changing_seconds'])*1000
        pagename = pages.objects.get(pagename=page_name)
        request.POST['pagename'] = pagename
        # request.POST.update({'pagename':page_name})
        print('type is',type(request.POST));
        request.POST._mutable=False
        
        if 'button1' in request.POST:
            for i in request.POST:
                print(request.POST[i])
            form_1=layout1(request.POST,request.FILES)
            if form_1.is_valid():
                form_1.save() 
            else:
                print('wrong');   
        
        elif 'button3' in request.POST:
            for i in request.POST:
                print(request.POST[i])
            form_3=layout3(request.POST,request.FILES)
            if form_3.is_valid(): 
                print('values form form_3',request.POST['changing_seconds'])
                form_3.save()
                
        
        elif 'button2' in request.POST:
            for i in request.POST:
                print(request.POST[i])
            form_2=layout2(request.POST,request.FILES)
            if form_2.is_valid():
                form_2.save()
                print('form submitted')
        
            else:
                print('form not submitted')
        
        
        elif 'button4' in request.POST:
            form_4=layout4(request.POST,request.FILES)
            if form_4.is_valid():
                form_4.save()

        else: 
            # Dynamic_Forms 
            post_data = {}
            file_data = {}
            for k,v in request.POST.items():
                if k  not in ['csrfmiddlewaretoken','priority','changing_seconds','pagename',page_name,request.POST['layout_name'],'layout_name']:
                    file_data[k] = str(v)
            post_data["priority"] = request.POST['priority']
            post_data["changing_seconds"] = request.POST['changing_seconds']
            for k,v in request.FILES.items():
                if v.content_type.startswith('image/'):
                    image = Imagefield.objects.create(content=v)
                    image.save()
                    print(image.returnUrl())
                    image_path = image.returnUrl()
                    file_data[k] = image_path
                elif v.content_type.startswith('video/'):    
                    video = videofield.objects.create(content=v)
                    video.save()
                    print(video.returnUrl())
                    video_path = video.returnUrl()
                    file_data[k] = video_path
                
            l_name = layout_name.objects.get(name=request.POST['layout_name'])
            # p_data = json.loads(post_data)
            # f_data = json.loads(file_data)
            data = {"post_data":post_data,"file_data":file_data}
            print('data=',data)
            
            data1 = custom_layout_data.objects.create(data=data,page_name=pagename,layout_name=l_name);
            data1.save(); 

         
    return render(request,'forms.html',context)



def deletepage(request,page_name):
     
    page = pages.objects.get(pagename=page_name)
    page.delete();
    return redirect('main')

def deletelayout(request,id):

    l = layout_name.objects.get(id=id);
    l.delete()
    return redirect('main')

def edit(request,page_name):
    context={}
    # print(page_name)
    pagename = pages.objects.get(pagename=page_name)
    data1=l1.objects.filter(pagename=pagename)
    data2=l2.objects.filter(pagename=pagename) 
    data3=l3.objects.filter(pagename=pagename)
    data4=l4.objects.filter(pagename=pagename)    
    data = list(chain(data1,data2,data3,data4))

    data.sort(key=data_sort)

    formdata= {}
    num=1
    for i in data:
        print('-------',i.__str__())
        if 'l1' in i.__str__():
            formdata[i]=[layout1(instance=i),num,'l1',i.id]
            print(num)
        if 'l2' in i.__str__():
            formdata[i]=[layout2(instance=i),num,'l2',i.id]
            print(num)
        if 'l3' in i.__str__():
            formdata[i]=[layout3(instance=i),num,'l3',i.id]
            print(num)
        if 'l4' in i.__str__():
            formdata[i]=[layout4(instance=i),num,'l4',i.id]
            print(num)
        num+=1
        print('formdata',formdata)
    form_1 = []
    form_2 = []
    form_3 = []
    form_4 = []
    editforms = []
    
    createform = page()
    context={
        'pagename' : page_name,
        'pageform' : createform,
        'formdata' : formdata,
        }
    # print('editforms',editforms)
    if request.method=='POST':
        if 'createpageform' in request.POST:
            return create(request)
        request.POST._mutable=True
        if int(request.POST['changing_seconds'])<20:
            request.POST['changing_seconds'] = int(request.POST['changing_seconds'])*1000
        
        if 'l1' in request.POST:
            id = request.POST['id']
            print('id of the form =',id)
            request.POST.pop('id')
            request.POST._mutable=False
        
            inst = l1.objects.get(id=id)
            form_1=layout1(request.POST,request.FILES,instance=inst)
            if form_1.is_valid():
                form_1.save()
                return redirect('edit',page_name=page_name)
            else:
                print('wrong');   

        elif 'l3' in request.POST:

            id = request.POST['id']
            print('id of the form =',id)
            request.POST.pop('id')
            request.POST._mutable=False
        
            inst = l3.objects.get(id=id)
            form_3=layout3(request.POST,request.FILES,instance=inst)
            if form_3.is_valid(): 
                print('success validation form-3')
                if form_3.save():
                    print('form 3 saved successfully')
                    # return redirect('temp')
                    return redirect('edit',page_name=page_name)
            else:
                print('failed validation form-3')
        
        elif 'l2' in request.POST:
            id = request.POST['id']
            print('id of the form =',id)
            request.POST.pop('id')
            request.POST._mutable=False
        
            inst = l2.objects.get(id=id)
            form_2=layout2(request.POST,request.FILES,instance=inst)
            if form_2.is_valid():
                form_2.save()
                print('form submission ok....')
                return redirect('edit',page_name=page_name)
            else:
                print('form not submitted')
        
        elif 'l4' in request.POST:

            id = request.POST['id']
            print('id of the form =',id)
            request.POST.pop('id')
            request.POST._mutable=False
        
            inst = l4.objects.get(id=id)
            form_4=layout4(request.POST,request.FILES,instance=inst)
            if form_4.is_valid():
                form_4.save()
                return redirect('edit',page_name=page_name)

    return render(request,'edit.html',context)
    

def custom_template(request,l_name):

    context={}
    createform = page()
    context = {
        'pageform' : createform,
        'form' : dynamic_form
    }
    if request.method == 'POST':
        if 'createpageform' in request.POST:
            return create(request)
        form = dynamic_form(request.POST)
        if form.is_valid():
            form.save()
        else:
            print('form not validated')
    return render(request,'create_templates.html',context)


def newlayout(request,l_name):
    
    name = layout_name.objects.get(name=l_name)
    data = elements_data.objects.get(layout_name=name)
    context = {
        'data' : data
    }
    print('data is ===',data)
    return render(request,'test.html',context)

@csrf_exempt 
def elementcreate(request,l_name):
    if request.method == 'POST':
        data = request.POST['data']
        name = layout_name.objects.get(name=l_name)

        print('data2', json.loads(request.POST['data2']))
        
        contentdata = dynamic_forms_data.objects.create(data=json.loads(request.POST['data2']),layout_name=name)
        contentdata.save()
        data_object = elements_data.objects.create(data=data,layout_name=name)
        data_object.save()
        print('post data = ',data)
        context = {
            'data' : data
        }

    return render(request,'custom_templates.html')


def testing(request):
    context = {}
    return render(request,'testing.html',context)

def Template1(request):
    return render(request,'layout1.html')

def Template2(request):
    return render(request,'layout2.html')

def Template3(request):
    return render(request,'layout3.html')

def Template4(request):
    return render(request,'layout4.html')

{# 



# @login_required(login_url='login')
# def temp(request):
#     context={}
#     data1=temp1.objects.all()
#     data2=temp2.objects.all()
#     print('data-1=',data1)
#     print('/n data-2=',data2)
#     data = list(chain(data1, data2))
#     print('data=',data)
#     context={'data':data}
#     return render(request,'temp.html',context)

# def layout_1(request):
#     context={}
    
#     return render(request,'layout_1.html',context)

# @login_required(login_url='login')
# def main(request):
#     context={}
#     form1=layout1()
#     form2=layout2()
#     form3=layout3()
#     form4=layout4()

#     context={
#         'form1':form1,
#         'form2':form2,
#         'form3':form3,
#         'form4':form4
#         }
#     if request.method=='POST':
        
#         request.POST._mutable=True
#         request.POST['changing_seconds']=int(request.POST['changing_seconds'])*1000
#         request.POST._mutable=False 
        
#         if 'button1' in request.POST:
#             form_1=layout1(request.POST,request.FILES,instance=request.POST.id)
#             if form_1.is_valid():
#                 form_1.save()    
        
#         elif 'button3' in request.POST:
#             form_3=layout3(request.POST,request.FILES)
#             if form_3.is_valid(): 
#                 print('values form form_3',request.POST['changing_seconds'])
#                 form_3.save()
        
#         elif 'button2' in request.POST:
#             form_2=layout2(request.POST,request.FILES)
#             if form_2.is_valid():
#                 form_2.save()
        
#         elif 'button4' in request.POST:
#             form_4=layout4(request.POST,request.FILES)
#             if form_4.is_valid():
#                 form_4.save()

#     return render(request,'1.html',context)
}