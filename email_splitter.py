# program to split email to username and domain name
# made by itsmeevil

print("***Email Splitter***")

email = input("\nEnter an email: ")

sliced = email.split("@") # split string at "@" which will put it in an array- ["username", "domain name"]

print(f"\nUsername: {sliced[0]}\nDomain name: {sliced[1]}")
