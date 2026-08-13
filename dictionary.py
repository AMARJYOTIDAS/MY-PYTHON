my_dict={
    "name":"hary",
    "age":22,
    "class":"mca",
    "address":{
        "at":"panasuapada",
        "po":"gopei",
        "dist":"kdp",
        "pin":754223,
    }

}

# print(my_dict)
# print(my_dict["address"])ke
# print(my_dict.keys())# it gives all keys and error or does not debug next line or stop at same line
# print(list(my_dict.values())) #it gives all values
# print(my_dict.get("name")) #it simply retuns none or does not return error

# my_dict.update({"marks":[12,45,98]}) #it simply update the keys or values or add new keys
# print(my_dict)
# my_dict.update({"name":'amar'})
# print(my_dict)
# print(len(my_dict))
marks= {}
x = int(input("enter your mark phy = "))
marks.update({"phy":x})

y = int(input("enter your mark chem = "))
marks.update({"chem":y})

z = int(input("mark of math = "))
marks.update({"math":z})

a = int(input("mark of english = "))
marks.update({"eng":a})
print(marks)

