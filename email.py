import smtplib, ssl

def read_email():
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