# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from mail.models import Email_details
import smtplib
from django.views.generic import ListView
# Create your views here.

def send(request):
    if request.method == 'POST':
        comment = request.POST.get('description')
        name1 = request.POST.get('name')
        email1 = request.POST.get('email')
        content = comment + " "+name1
        u = Email_details.objects.create(name=name1, email=email1, description=comment)
        u.save()
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login('sarvanimini@gmail.com', 'mini@241098')
        mail.sendmail('sarvanimini@gmail.com','sarvanimini@gmail.com', content)
        mail.close()
        return render(request, 'mail/mail.html', {})
    return render(request, 'mail/mail.html', {})


class CommentList(ListView):
    template_name = 'mail/display.html'
    model = Email_details
