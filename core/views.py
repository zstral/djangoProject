from django.shortcuts import render

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
    return render(request, 'core/registro_wiki.html', {
        'title': 'Registrarse',
        'stylesheet': 'core/css/csslogin/login.css'
    })

def login(request):
    return render(request, 'core/inicio_sesion_wiki.html', {
        'title': 'Iniciar Sesión',
        'stylesheet': 'core/css/csslogin/login.css'
    })

def account(request):
    return render(request, 'core/micuentatf.html', {
        'title': 'Mi Cuenta',
        'stylesheet': 'core/css/micuenta.css'
    })