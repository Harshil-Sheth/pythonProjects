import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Harshil Sheth'
email['to'] = 'rajshah181888@gmail.com'
email['subject'] = 'Hey It\'s from Harshil!!'

email.set_content('I am Harshil!!! U Know ME!!!')


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('harshilshah29599@gmail.com', '181888ok')
    smtp.send_message(email)
    print('All Good!!! Boss!!!')
