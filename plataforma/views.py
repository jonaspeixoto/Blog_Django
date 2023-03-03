from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,Usuario
from .forms import PostForm, UsuarioForm
def blog(request):
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request, 'home.html', context)


def criar_post(request):

    if request.method == 'GET':
        print('metodo get')
        form = PostForm()

    elif request.method == 'POST':
        print( 'entrei')
        form = PostForm(request.POST,request.FILES)
        # file = request.FILES.get('imagem_post')
        # print(file)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            imagem_post = form.cleaned_data['imagem_post']
            resumo = form.cleaned_data['resumo']
            conteudo = form.cleaned_data['conteudo']
            post = Post(titulo=titulo, imagem_post=imagem_post, resumo=resumo, conteudo=conteudo)
            post.save()
            return HttpResponse('formulario enviado')

    return render(request, 'criar_post.html', {'form':form})

def listar_post(request, id):
    posts = Post.objects.get(pk=id)
    context = {
        'posts':posts 
    }

    return render(request, 'listar_post.html', context)

def login(request):
    return render(request, 'usuario/login.html')

def cadastro(request):

    if request.method == 'GET':
        form = UsuarioForm()
        

    elif request.method == 'POST':
        form = UsuarioForm(request.POST)

        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            usuario = Usuario(nome=nome, email=email, senha=senha)
            usuario.save()
            return HttpResponse('enviado')

    return render(request, 'usuario/cadastro.html', {'form':form})
