#WAP to demonstrate multiple return using function

def get_user_info():
    name = "Alice"
    age = 30
    return name,age
user_name , user_age = get_user_info()
print(user_name)
print(user_age)
print("written by Vardaan Valecha 0221BCA068")