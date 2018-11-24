# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import render_to_string
#
# def send_priority_email(name,receiver):
#     #Creating message subject and sender
#     subject = 'Neighbourhood - High Priority Notification'
#     sender = 'donatello54611@gmail.com'
#
#     #passing in the context variables
#     text_content = render_to_string('email/priority.txt',{"name":name})
#     html_content = render_to_string('email/priority.html',{"name":name})
#
#     msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
#     msg.attach_alternative(html_content,'text/html')
#     msg.send()
