from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage, send_mail
from django.template.loader import get_template
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings


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
            
            subject = 'Thanks for getting in touch!'
            message = 'Thank you for contacting Photos of Ireland. We will get back to you as soon as we can'
            from_email = settings.EMAIL_HOST_USER
            to_email = [contact_email]

            send_mail(subject,message,from_email,to_email,fail_silently=True)
    
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