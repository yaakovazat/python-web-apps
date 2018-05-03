# This is to calculate age by seconds

def age_seconds(age):
    seconds = int(age)*365*24*16*60
    return  "You have already leaved for: {} seconds !".format(seconds)

age=input("Please Enter Your age: ")
seconds=age_seconds(age)
print(seconds)