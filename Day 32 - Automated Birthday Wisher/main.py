import smtplib

my_email = "testikra070@gmail.com"
password = "abcdexample"
print("a")
connection = smtplib.SMTP("smtp.gmail.com")
print("b")
connection.starttls()  # Transport Layer Security, message will be encrypted
connection.login(user=my_email, password=password)
# print("d")
connection.sendmail(from_addr=my_email, to_addrs="testikra07@yahoo.com", msg="Hello from gmail!")
# print("e")
# connection.close()
