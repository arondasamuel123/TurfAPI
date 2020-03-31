from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_booking_email(username,receiver):
    subject = 'Booking- Turf Availablity'
    sender = 'isproject.420@gmail.com'
    
    text_content = render_to_string('email/booking_email.txt', {"name": username})
    html_content = render_to_string('email/booking_email.html', {"name": username})
    
    msg = EmailMultiAlternatives(subject, text_content, sender,[receiver])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
    
def confirm_booking_email(username,receiver):
    subject = 'Booking- Turf Availablity'
    sender = 'isproject.420@gmail.com'
    
    text_content = render_to_string('email/confirmed_email.txt', {"name": username})
    html_content = render_to_string('email/confirmed_email.html', {"name": username})
    
    msg = EmailMultiAlternatives(subject, text_content, sender,[receiver])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()