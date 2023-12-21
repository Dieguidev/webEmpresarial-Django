from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm()
    #* este if hace que aparezcan los campos ya enviados
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get("name", "")
            email = request.POST.get("email", "")
            content = request.POST.get("content", "")
            #* enviamos el correo y redireccionamos
            email = EmailMessage(
                "La Caffetiera: Nuevoi mensaje de contacto",
                f"De {name} <{email}>\n\nEscribió:\n\n{content}",
                "no-contestar@inbox.mailtrap.io",
                ["diegogaraycullas@gmail.com"],
                reply_to=[email]
            )
            
            try:
                email.send()
                #Redireccionamos a OK
                return redirect(reverse("contact") + "?ok" )
            except:
                #Redireccionamos a FAIL
                return redirect(reverse("contact") + "?fail" )
        
    
    return render(request, "contact/contact.html", {"form": contact_form})