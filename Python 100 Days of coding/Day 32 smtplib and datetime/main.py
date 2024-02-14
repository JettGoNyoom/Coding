import smtplib

myemail = "jettsender@gmail.com"
my_pw = "zrga pswq avwf vhbo"

connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=myemail, password=my_pw)
connection.sendmail(from_addr=myemail, to_addrs="jettreceiver@yahoo.com", msg="Subject:Hello\n\nThis is the body")
connection.close()