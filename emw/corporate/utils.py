from django.core.mail import EmailMessage
from django.contrib import messages
from django.shortcuts import render, redirect


def send_email(request, name, email, subject, textarea):
    try:
        subject = subject
        recipient_list = ['emwwebmaster2020@gmail.com', ]
        email_body = """\
        <html>
        <head> </head>
        <body>
            <h2>New Contact Us Message</h2>
            <p>name: %s</p>
            <p>email: %s</p>
            <p>Message: %s</p>
        </body>
        </html>
        """ % (name, email, textarea,)
        mail = EmailMessage(
            subject,
            email_body,
            'EMW',
            recipient_list,
        )
        mail.content_subtype = "html"
        mail.send()
        messages.success(request, 'Message successfully sent.')
        return redirect('corporate:contact')
    except Exception as e:
        messages.error(
            request, 'Something went wrong please use the following email:  admin@emw.co.zw')
        return redirect('corporate:contact')
        print(e)
