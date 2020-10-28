# program to split email to username and domain name
# made by itsmeevil

print("***Email Splitter***")

email = input("Enter an email: ")

sliced = email.split("@") # split string at "@" - e.g = ["username", "domain name"]

username = sliced[0] # get username from sliced array
domain_name = sliced[1] # get domain name from sliced arrray

print("\nUsername: ", username, "\nDomain name: ", domain_name) # but ofc i can also get array info here
