# Output functions
# Seperator Function:

no1, no2, no3, no4  = 10, 20, 30, 40
print(no1, no2, no3, no4, sep = "/")

# End Function:

print(no1, no2, no3, no4, end = "/  ")

print("Deepika", end = "* ")

print("vennandur")


#Formatted Strings

# %i, %d, %f, %s

no1, no2, no3, no4  = 10, 20, 30, 40

print("no1 value %i" %no1)
print("no1 value %d" %no1)

name = 'Titikksha'
print("hi", name)
print("hi %s" %name)

print("no1 value is %d and no2 value is %d" %(no1,no2))

value = 3.14

print("value is %f" %value)


# Replacement Operators {}

name= "gowtham"

city= 'coimbatore'

acc_no = 16576836

print("hi", name, "your acc_no is ", acc_no )

print("hi {0} your acc_no is {1} and you are from {2}".format (name, acc_no, city))

print("hi {a} your acc_no is {b} and you are from {c}".format (a=name, b=acc_no, c=city))

print("hi {} your acc_no is {} and you are from {}".format (name, acc_no, city))
