from django.shortcuts import render
from django.http import HttpResponse
import random
import names



def generate_students():
    return {
        f'student_{i+1}': [names.get_first_name(), names.get_last_name(), round(random.uniform(1.0, 4.0), 1), random.randint(1, 4)]
        for i in range(100)
    }

def students_page(request):
    students = generate_students()
    return render(request, 'students/students_page.html', {'students': students})
    
def main_page(request):
    student = dict(student = random.choice(list(generate_students().values())))
    return render(request, 'students/main_page.html', {'student': student})
    
