from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required()
def contact(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('content', '')
    
            template = get_template('contact/contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)
    
            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['cjhugo1991@hotmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            messages.success(request, "You have sucessfully contacted our team, we will get back to you ASAP")
            return redirect('home')

    return render(request, 'contact/contact.html', {'form': form_class})