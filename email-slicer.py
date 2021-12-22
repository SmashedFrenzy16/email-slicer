

email = input("Enter your email address: ").strip()

userName = email[:email.index("@")]

domain = email[email.index("@")+1:]

output = "Your username is '{}' and your domain name is '{}'".format(userName, domain)

print(output)
