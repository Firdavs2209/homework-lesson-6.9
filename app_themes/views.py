
from django.shortcuts import render
import os

def theme_list(request):
        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lessons.txt')
        try:
            with open(file_path, 'r') as f:
                return render(request, 'themes/theme_list.html', {'themes': f})
        except FileNotFoundError:
           pass

