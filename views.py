from django.shortcuts import render
from .models import DictionaryDb
from .forms import DictionaryForm
def home(request):

    if request.method=="POST":
        form=DictionaryForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_letters=DictionaryDb.objects.all().order_by('letter')
            return render(request,'index.html',{'all_letters':all_letters})
    else:

        all_letters=DictionaryDb.objects.all().order_by('letter')
        return render(request,'index.html',{'all_letters':all_letters})
def posts(request,pk_test):
    post=DictionaryDb.objects.get(letter=pk_test)
    return render(request,'posts.html',{'post':post})
