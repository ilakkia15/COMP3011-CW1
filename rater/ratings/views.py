from django.shortcuts import render
from django.http import HttpResponse
from .models import Professor, Module, Instance, Student, Rating
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# Override the default CSRF protection in Django.
@csrf_exempt
def HandleRegisterRequest(request):
    """
    Handle a register request.

    Args:
        request (HttpRequest object): The HttpRequest object.

    Returns:
        HttpResponse object: The content to be returned.
    """

    # TODO: Potentially include status code in HttpResponse objects.

    # Check whether the request is a POST request.
    if request.method == 'POST':
        # Get the username, email and password from the POST request.
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Retrieve a student that already exists with the given username.
        student_with_username = Student.objects.filter(username=username)
        # Retrieve a student that already exists with the given email.
        student_with_email = Student.objects.filter(email=email)

        # Filter through the data for a student with the given username.
        if student_with_username.exists():
            return HttpResponse('Error: This username is already taken.')
        
        # Filter through the data for a student with the given email.
        if student_with_email.exists():
            return HttpResponse('Error: This email is already taken.')
        
        # Create a new Student object for the given details.
        student = Student(username=username, email=email, password=password)
        # Save the Student object to the underlying database.
        student.save()

        return HttpResponse('Success: You have been registered.')
    return HttpResponse('Error: Invalid request method.')
    