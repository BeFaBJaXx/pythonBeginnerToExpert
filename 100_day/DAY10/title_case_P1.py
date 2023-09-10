def format_name(f_name,l_name):
  a = f_name.lower()
  b = l_name.lower()
  a = a.title()
  b = b.title()
  # print(a + " "+ b) we can do this-1
  # we can do this 2-3
  return a +" " +  b 

f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")

# format_name(f_name,l_name)  we can do this-1
# print(format_name(f_name,l_name)) we can do this-2

# we can do this-3
a = format_name(f_name,l_name)
print(a)


# you can also pass input() as parameter when we cann a function