import string
import random

if __name__ == "__main__":
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    # s4 = string.punctuation
    print("Welcome to password genarator. Created by Redwan\n")
    service_name = input("Enter the site for your password: ")
    pws = int(input("Enter your password length\n"))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    file = open("pass.txt" , "a")
    file.write(f"\n{service_name} : ")
    file.write("".join(random.sample(s, pws)))
    file.close()
    print("Password has been saved in the file.\n")
    print("Thank you for using this program")

        ## File will be saved in C:\Users\your directory name\pass.txt ##

