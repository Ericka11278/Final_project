import smtplib, ssl
"""
This method is supposed to send an email receipt to the customer, I imported smtplib a built in python module
to send emails in python. it is a bit fishy because it makes you login to an email account to send emails so I created a sample one
Also in order to recieve the email you have to turn off a security feature in your google account


 Args: 
    user (str): email adress which is the user name for the sample email
    passw(str): a password for the sample email
    sender(str) : user or basically the sample email address im using to send to myself
    message(str): the message being sent to the user 
    port(int): the server used in google email system
"""
def read_email():
    """
    This method separates the user from the password in the txt file and returns it
    Returns:
        user and passw from the tt file

    """
    user = passw = ""
    with open("sample_email.txt", "r") as f:
        file = f.readlines()
        user = file[0].strip
        passw = file[1].strip
    
    return user, passw
port = 456
sender, password = read_email()
sender = "practicehw237@gmail.com"
recieve = sender

message = """\
Subject : Your Receipt from JEB
This is your receipt

-Thank you JEB Tema

"""

context = ssl.create_default_context()
print(" Message sending.. ")
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, recieve, message)
print(" Message sent! ")