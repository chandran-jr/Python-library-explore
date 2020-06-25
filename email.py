import smtplib

email = smtplib.SMTB('smtp.gmail.com', 587)

email.starttls()

email.login("sender_email_id","sender_password")

message = "the message"

email.sendmail("sender_email_id", "reciever_email_id",message)

email.quit()
