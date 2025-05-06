list=[1234,"disj@kb","bjhbh"]

list2= [ i for i in list if i==1234]
print(list2)

dict={"diksha":"123@", "priti":"154@", "sheefa":"745"}
new_dict={name:password for name,password in dict.items() if name=="diksha"}
print(new_dict)
# v