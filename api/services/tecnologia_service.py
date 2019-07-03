from ..models import Tecnologia

def listar_tecnologias():
    tecnologias = Tecnologia.objects.all()
    return tecnologias

def cadastrar_tecnologia(tecnologia):
    return Tecnologia.objects.create(nome=tecnologia.nome)