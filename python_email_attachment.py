import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
import getpass

def send_email(email_sender,email_password):
    msg = MIMEMultipart()


    try:
        #Connect to the Gmail sever and login into Gmail#
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(email_sender, email_password)
        print("Please enter email receiver's address: ")
        email_receiver = input()
        print("Enter subject: ")
        subject = input()
        print("Enter email body: ")
        body = input()

        """attachment feature"""
        print("Attachment file address: ")
        try:
            attachment_address = input()
            file_address = attachment_address
            attachment = open(file_address, 'rb')
            part = MIMEBase('application', 'octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= " + os.path.basename(file_address))
            msg.attach(part)
        except Exception:
            pass

        """
        use MIMEText to make it more like a real email
        The MIMEText will make sure the mail showing 
        from:
        to:
        and subject: 
        """
        msg['From'] = email_sender
        msg['To'] = email_receiver
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        server.sendmail(email_sender, email_receiver, text)
        server.quit()
        print('Success: Email sent from Python!')
    except:
        print("Email failed to send.")

def main():
    print("Hello! Welcome to python email!")
    """
    test code
    
    print("Please enter your Gmail address: ")
    email_sender = input()
    print("Please enter your Gmail password: ")
    email_password = input()
   
    email_sender='yanglitestemail@gmail.com'
    email_password='ly19890726'

    """
    print("Please enter your Gmail address: ")
    email_sender = input()
    print("Please enter your Gmail password: ")
    email_password = getpass.getpass()

    send_email(email_sender, email_password)

if __name__ == "__main__":main()
