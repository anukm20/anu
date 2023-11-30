# import re
# terms="gulugulu"
# a=re.search(terms,"hallo gulugulu")
# print(a)


"""re matched or notmachted"""
# import re
# terms="['a-zA-Z0-9']nurag"
# a=re.match(terms,"anurag")
# if a:
#     print("matched")
# else:
#     print("not matched")



"""dot anu charector"""
# import re
# terms="['a-zA-Z0-9']....."
# a=re.match(terms,"anurag")
# if a:
#     print("matched")
# else:
#     print("not matched")



""" """
# import re
# terms="^anurag+$"
# a=re.search(terms,"anuraggg")
# if a:
#     print("matched")
# else:
#     print("not matched")


"""date"""
# import re
# a=str(input("enter tha date: "))
# terms="^[012]\d|3[01]-[0]\d|1[012]-\d{4}$"
# b=re.search(terms,a)
# if b:
#     print("valid")
# else:
#     print("not valid")


"""date ZERO not"""
# import re
# a=str(input("enter tha date: "))
# terms="^([^00]|[0][1,9]|[12][1,9]|3[1]|[123][0])(-|.|/)([^00]|[0][1,9]|1[012])(-|.|/)([^0000]\d{4})$"
# b=re.search(terms,"11-11-0000")
# if b:
#     print("valid")
# else:
#     print("not valid")


"""email validation"""
import re
a=str(input("enter tha email: "))
terms="^([a-zA-Z]{12}\d{3})[@]([a-z]{10}[.])([in]|[com])$"
b=re.search(terms,a)
if b:
    print("valid")
else:
    print("not valid")