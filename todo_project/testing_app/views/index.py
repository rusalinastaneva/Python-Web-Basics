from django.shortcuts import render, redirect

from testing_app.forms.profile import ProfileForm
from testing_app.models import Profile


def index(request):
    if request.method == 'GET':
        context = {
            'profiles': Profile.objects.all(),
            'form': ProfileForm(),
        }
        return render(request, 'testing/index.html', context)
    else:
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profiles')

        context = {
            'profiles': Profile.objects.all(),
            'form': form,
        }

        return render(request, 'testing/index.html', context)
