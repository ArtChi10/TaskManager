from django.shortcuts import render
from django.views import View
# Create your views here.


class Menu(View):
    def get(self, request):
        return render(request, 'main/main.html')