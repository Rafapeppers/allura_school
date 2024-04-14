from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import viewsets
from escola.models import Aluno, Curso
from serializer import AlunoSerializer, CursoSerializer

# Create your views here.

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    # teste 
    
    
class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer    
    
def alunos(request):
    if request.method == 'GET':
        aluno = {'id': 1, 'nome': 'Guilherme'}
        return JsonResponse(aluno)   
