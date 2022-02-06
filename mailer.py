import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "MySQL Backup Successful"
body = "MySQL database backup successfully done "
sender_email = "dr@fast-pay.cash"
#receiver_email = "mdkibria@fastsolutioninc.com, ovi@fastsolutioninc.com, shuvo@fastsolutioninc.com"
receiver_email = "shuvo@fastsolutioninc.com, onik@fastsolutioninc.com, mdkibria@fastsolutioninc.com"
user = "AKIAVKLR75GZYEUUYW6B"
password = "BBxBbp4UnIE/7IuAGZFMnHtuCZvlDRURosYTOngSX+A8"

# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
##message["Bcc"] = receiver_email  # Recommended for mass emails

# Add body to email
message.attach(MIMEText(body, "plain"))

##filename = "/root/python/replicationStatus.txt"  # In same directory as script

# Open PDF file in binary mode
##with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
##    part = MIMEBase("application", "octet-stream")
##    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email
##encoders.encode_base64(part)

# Add header as key/value pair to attachment part
##part.add_header(
##    "Content-Disposition",
##   f"attachment; filename= replicationStatus.txt",
##)

# Add attachment to message and convert message to string
##message.attach(part)
text = message.as_string()

# Log in to server using secure context and send email
context = ssl.create_default_context()
with smtplib.SMTP("email-smtp.eu-west-1.amazonaws.com", 587) as server:
    server.starttls(context=context)
    server.login(user, password)
##    server.sendmail(sender_email, receiver_email, text)
    server.sendmail(sender_email, ["shuvo@fastsolutioninc.com", "onik@fastsolutioninc.com", "mdkibria@fastsolutioninc.com"], text)
