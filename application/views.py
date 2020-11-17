from django.shortcuts import render, redirect
from .models import *
from .forms import *
from .serializers import *
from rest_framework.decorators import api_view , permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import JsonResponse

# def teacher_sign_up(request):
#     form = CustomUserCreationForm
#
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get['username']
#             user = User.objects.get(username=username)
#             user.is_student = False
#             user.save()
#             return redirect('/')
#         else:
#             form = CustomUserCreationForm
#     return render(request, 'application/teacher_signup.html', context={'form': form})
#
#
# def student_sign_up(request):
#     form = CustomUserCreationForm
#
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get['username']
#             user = User.objects.get(username=username)
#             user.is_student = True
#             user.save()
#             return redirect('/')
#         else:
#             form = CustomUserCreationForm
#     return render(request, 'application/signup.html', context={'form': form})


def home(request):
    student = Student.objects.all()
    teacher = Teacher.objects.all()
    context = {'student':student, 'teacher':teacher}
    return render(request, 'application/home.html', context)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def teacher_detail(request):
    user = User.objects.get(username=request.user.username)
    if not user.is_student:
        teacher = Teacher.objects.get(user=user)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)
    else:
        return Response({'Error': 'Must be a Teacher'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def student_detail(request):
    user = User.objects.get(username=request.user.username)
    if user.is_student:
        teacher = Student.objects.get(user=user)
        serializer = StudentSerializer(teacher)
        return Response(serializer.data)
    else:
        return Response({'Error': 'You are not a student'})


@api_view(['GET'])
def teacher_one(request,id):
    teacher = Teacher.objects.get(id=id)
    serializer = TeacherSerializer(teacher)
    return Response(serializer.data)


@api_view(['POST'])
def teacher_update(request,id):
    teacher = Teacher.objects.get(id=id)
    data = request.data

    for existing_subject in teacher.subject.all():
        teacher.subject.remove(existing_subject)

    for subjects in data.get('subject', teacher.subject):
        sub = Subject.objects.get(subject=subjects)
        teacher.subject.add(sub)
    teacher.save()
    serializer = TeacherSerializer(teacher)
    return Response(serializer.data)

