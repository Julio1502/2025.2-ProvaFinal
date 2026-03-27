from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Alô professor, sou Julio Gleison da Silva da turma SO 2025.2</h1>")