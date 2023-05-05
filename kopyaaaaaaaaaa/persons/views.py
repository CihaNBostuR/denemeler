from django.shortcuts import render, redirect, get_object_or_404
from .forms import PersonCreationForm
from .models import BasimYili,YayinEvi

def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            return redirect('person_add')
    return render(request, 'persons/home.html', {'form': form})


# def person_update_view(request, pk):
#     person = get_object_or_404(Person, pk=pk)
#     form = PersonCreationForm(instance=person)
#     if request.method == 'POST':
#         form = PersonCreationForm(request.POST, instance=person)
#         if form.is_valid():
#             return redirect('person_change', pk=pk)
#     return render(request, 'persons/home.html', {'form': form})


# AJAX for yayinevies
def load_yayinevi(request):
    x= request.GET.get('aaa')
    basimyiliId = request.GET.get('basimyiliId')
    print(x)
    yayinevies = YayinEvi.objects.filter(basimyiliId=basimyiliId).all()
    return render(request, 'persons/city_dropdown_list_options.html', {'yayinevies': yayinevies})

    