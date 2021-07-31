from django.shortcuts import render

# Create your views here.
def task(request):
    context = {'task':'active'}
    return render(request, 'skills/skill.html', context)