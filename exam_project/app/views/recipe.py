from django.shortcuts import render, redirect

from app.forms import RecipeForm, DeleteRecipeForm
from app.models import Recipe


def create_recipe(request):
    if request.method == 'GET':
        form = RecipeForm()

        context = {
            'form': form,
        }
        return render(request, 'create.html', context)
    else:
        form = RecipeForm(request.POST)
        context = {
            'form': form,
        }
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'index.html', context)


def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    if request.method == 'GET':
        form = RecipeForm(instance=recipe)

        context = {
            'form': form,
            'recipe': recipe,
        }
        return render(request, 'edit.html', context)
    else:
        form = RecipeForm(request.POST, instance=recipe)

        context = {
            'form': form,
            'recipe': recipe,
        }

        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'edit.html', context)


def delete_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    if request.method == 'GET':
        form = DeleteRecipeForm(instance=recipe)

        context = {
            'form': form,
            'recipe': recipe,
        }
        return render(request, 'delete.html', context)
    else:
        recipe.delete()
        return redirect('index')


def details_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    form = DeleteRecipeForm(instance=recipe)
    ingredients_list = recipe.ingredients.split(', ')

    context = {
        'form': form,
        'recipe': recipe,
        'ingredients_list': ingredients_list,
    }

    return render(request, 'details.html', context)
