from django.shortcuts import render, redirect

# Create your views here.

from pets.forms.comment_form import CommentForm
from pets.forms.pet_form import PetForm
from pets.models import Pet, Like, Comment


def list_pets(request):
    context = {
        'pets': Pet.objects.all(),
    }
    return render(request, 'pet_list.html', context)


def details_or_comment_pet(request, pk):
    pet = Pet.objects.get(pk=pk)

    if request.method == 'GET':
        context = {
            'pet': pet,
            'form': CommentForm(),
        }
        return render(request, 'pet_detail.html', context)
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(text=form.cleaned_data['text'])
            comment.pet = pet
            comment.save()
            return redirect('pet details or comment', pk)
        context = {
            'pet': pet,
            'form': form,
        }
        return render(request, 'pet_detail.html', context)


def like_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    like = Like(test=str(pk))
    like.pet = pet
    like.save()
    return redirect('pet details or comment', pk)


def comment_pet(request, pk):
    # pet = Pet.objects.get(pk=pk)
    # comment = Comment
    pass


def persist(request, pet, template_name, redirect_path):
    if request.method == 'GET':
        form = PetForm(instance=pet)
        context = {
            'form': form,
            'pet': pet,
        }
        return render(request, f'{template_name}.html', context)
    else:
        form = PetForm(request.POST, instance=pet)

        if form.is_valid():
            form.save()
            if template_name == 'pet_create':
                return redirect(redirect_path)
            return redirect(redirect_path, pet.id)
        context = {
            'form': form,
        }
        return render(request, f'{template_name}.html', context)


def create_pet(request):
    return persist(request, Pet(), 'pet_create', 'list pets')


def edit_pet(request, pk):
    return persist(request, Pet.objects.get(pk=pk), 'pet_edit', 'pet details or comment')


def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)

    if request.method == "GET":
        context = {
            'pet': pet,
        }
        return render(request, 'pet_delete.html', context)
    else:
        pet.delete()
        return redirect('list pets')

# def create_pet(request):
#     # Return empty form
#     if request.method == 'GET':
#         form = PetForm()
#
#         context = {
#             'form': form,
#         }
#         return render(request, 'pet_create.html', context)
#
#     else:
#         # Create the pet
#         form = PetForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             return redirect('list pets')
#         context = {
#             'form': form,
#         }
#         return render(request, 'pet_create.html', context)
#
# def edit_pet(request, pk):
#     pet = Pet.objects.get(pk=pk)
#
#     if request.method == "GET":
#         form = PetForm(instance=pet)
#
#         context = {
#             'pet': pet,
#             'form': form,
#         }
#         return render(request, 'pet_edit.html', context)
#     else:
#         form = PetForm(request.POST, instance=pet)
#
#         if form.is_valid():
#             form.save()
#             return redirect('pet details or comment', pk)
#
#         context = {
#             'form': form,
#         }
#         return render(request, 'pet_edit.html', context)
