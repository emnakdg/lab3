dic = {"United Nations Educational, Scientific and Cultural Organization": "UNESCO", "Federal Bureau of Investigation": "FBI"}

user = input("What is the organization's full name ? : ")

try:
    print(dic[user])
except:
    user2 = input("This organization didn't found. Do you want to add? Y/N")

    if user2 == "Y" or user2 == "y" or user2 == "Yes" or user2 == "yes" or user2 == "YES":
        ob = input("Waht is ob? : ")
        dic.update({user : ob})
        print(dic[user])
    else:
        print("Program is closing")