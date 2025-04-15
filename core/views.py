from django.shortcuts import render, redirect
from .forms import ForumusersForm, LoginForm, EditProfileForm
from .models import Forumusers

def home(request, section=None):
    sections = {
        None: {'template': 'core/menuprincipal_wiki.html', 'title': 'Inicio', 'stylesheet': 'core/css/estilo.css'},
        'animals': {'template': 'core/Animales.html', 'title': 'Animales', 'stylesheet': 'core/css/Animales.css'},
        'map': {'template': 'core/Lugarestf.html', 'title': 'Mapa', 'stylesheet': 'core/css/lugares.css'},
        'enemys': {'template': 'core/Enemigos.html', 'title': 'Enemigos', 'stylesheet': 'core/css/Enemigos.css'},
        'buildings': {'template': 'core/Construcciones.html', 'title': 'Construcciones', 'stylesheet': 'core/css/Construcciones.css'},
        'plants': {'template': 'core/Flora.html', 'title': 'Plantas', 'stylesheet': 'core/css/flora.css'},
        'weapons': {'template': 'core/Armas.html', 'title': 'Armas', 'stylesheet': 'core/css/Armas.css'},
        'consumables': {'template': 'core/Consumibles.html', 'title': 'Consumibles', 'stylesheet': 'core/css/Consumibles.css'},
        'history': {'template': 'core/historia.html', 'title': 'Historia', 'stylesheet': 'core/css/historia.css'},
    }
    section_data = sections.get(section, sections[None])
    context = {
        'current_section': section,
        'title': section_data['title'],
        'stylesheet': section_data['stylesheet'],
    }
    return render(request, section_data['template'], context)

def forum(request):
    return render(request, 'core/forowiki.html', {
        'title': 'Foro',
        'stylesheet': 'core/css/foro.css'
    })

def signup(request):
    if request.method == 'POST':
        form = ForumusersForm(request.POST)
        confirm_password = request.POST.get('password_confirm')
        if form.is_valid():
            if form.cleaned_data['password'] == confirm_password:
                form.save()
                return redirect('home')
            else:
                form.add_error('password', 'Las contraseñas no coinciden')
    else:
        form = ForumusersForm()
    return render(request, 'core/registro_wiki.html', {
        'title': 'Registrarse',
        'stylesheet': 'core/css/login.css',
        'form': form
    })
    
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = Forumusers.objects.get(email=email, password=password)
                request.session['user_id'] = user.id
                return redirect('home')
            except Forumusers.DoesNotExist:
                form.add_error(None, 'Email o contraseña incorrectos')
    else:
        form = LoginForm()
    return render(request, 'core/inicio_sesion_wiki.html', {
        'title': 'Iniciar Sesión',
        'stylesheet': 'core/css/login.css',
        'form': form
    })

def account(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    try:
        user = Forumusers.objects.get(id=user_id)
        if request.method == 'POST':
            form = EditProfileForm(request.POST, instance=user)
            if form.is_valid():
                cleaned_data = form.cleaned_data
                if cleaned_data.get('username'):
                    user.username = cleaned_data['username']
                    print(f"Actualizando username a: {user.username}")
                if cleaned_data.get('email'):
                    user.email = cleaned_data['email']
                    print(f"Actualizando email a: {user.email}")
                if cleaned_data.get('password'):
                    user.password = cleaned_data['password']
                user.save()
                return redirect('account')
        else:
            form = EditProfileForm(instance=user)
        return render(request, 'core/micuentatf.html', {
            'title': 'Mi Cuenta',
            'stylesheet': 'core/css/micuenta.css',
            'user': user,
            'form': form
        })
    except Forumusers.DoesNotExist:
        return redirect('login')