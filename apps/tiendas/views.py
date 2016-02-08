from django.shortcuts import render
from .models import Tienda, Zona
from .forms import TiendaForm, ZonaForm, UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required
def reclama_datos(request):
    print "entra quia"
    tiendas =  Tienda.objects.order_by('-views')

    datos = ()
    tiendas_nombre = []
    visitas = []
    for t in tiendas:
        visitas.append(t.views)
        tiendas_nombre.append(t.nombre)

    datos= tiendas_nombre, visitas
    return JsonResponse(datos, safe=False)


def inicio(request):
    return render(request, 'tiendas/index.html')

@login_required
def inicio(request):
    zona_list = Zona.objects.order_by('nombre')[:5] #orden ascendente a-z, orden descendente z-a con ('-nombre')
    tiendas = Tienda.objects.order_by('-views')[:3]
    context_dict = {'zonas': zona_list, 'tiendas': tiendas}
    return render(request, 'tiendas/index.html', context_dict)


@login_required
def aumentar_visitas_tienda(request,tienda_name_slug):
    try:
        tienda = Tienda.objects.get(slug=tienda_name_slug)
        tienda.views += 1
        zona_aux=tienda.zona
        tienda.save()
        tiendas_list = Tienda.objects.filter(zona=zona_aux)
        tiendas_dict = {'tiendas': tiendas_list,'zona':zona_aux}
        return render(request,'tiendas/mostrartiendas.html',tiendas_dict)
    except Tienda.DoesNotExist:
        tienda = None
        return render(request,'tiendas/mostrartiendas.html')
    
@login_required
def mostrar_tiendas(request,zona_name_slug):
    try:
        zona_aux = Zona.objects.get(slug=zona_name_slug)
        zona_aux.views += 1
        zona_aux.save()
        tiendas_list = Tienda.objects.filter(zona=zona_aux)
        tiendas_dict = {'tiendas': tiendas_list,'zona':zona_aux}
        return render(request, 'tiendas/mostrartiendas.html', tiendas_dict)
    except Zona.DoesNotExist:
        zona_aux = None
        return render(request, 'tiendas/mostrartiendas.html')

@login_required
def add_zona(request):
    if request.method == 'POST':
        form = ZonaForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return inicio(request)

        else:
            print form.errors
    else:
        form = ZonaForm()
        
    return render(request, 'tiendas/add_zona.html', {'form': form})
@login_required
def add_tienda(request, zona_name_slug):

    try:
        zona = Zona.objects.get(slug=zona_name_slug)
    except Zona.DoesNotExist:
        zona = None

    if request.method == 'POST':
        form = TiendaForm(data=request.POST)
        if form.is_valid():
            if zona:
                tienda = form.save(commit=False)
                tienda.zona=zona

                if 'imagen' in request.FILES:
                    print "se coge la imagen"
                    tienda.imagen = request.FILES['imagen']

                tienda.save()
                # probably better to use a redirect here.
                return inicio(request)
        else:
            print form.errors
    else:
        form = TiendaForm()

    context_dict = {'form':form, 'zona': zona}

    return render(request, 'tiendas/add_tienda.html', context_dict)

def register(request):
    print "Registro"
    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True
            return HttpResponseRedirect('/tiendas/')

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'tiendas/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )

def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/tiendas/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your tiendas account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'tiendas/login.html')

@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")

from django.contrib.auth import logout

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    print "Se mete en logout"
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/tiendas/')