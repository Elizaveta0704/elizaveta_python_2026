# Section 1

name = "Elizaveta"
age = 38
height = 5.9
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))
print ()

# Section 2

user_name = input("What is your name? ")
birth_year = int(input("What year were you born? "))
year_now = 2026
approximate_age = year_now - birth_year
print(f"Hi, {user_name}! You are approximately {approximate_age} years old.")
print()
# Section 3

notebook_price = float (input("What price is your notebook? "))
quantity = int(input ('How many notebooks? '))
total_price = notebook_price * quantity
print(f"{notebook_price} × {quantity} = {total_price}")
print()
# Section 4:

item_name = "Notebook"
price = 19.99
quantity = 3

total = price * quantity

print("===========================")
print("          RECEIPT")
print("===========================")
print(f"Item:      {item_name}")
print(f"Price:     ${price}")
print(f"Quantity:  {quantity}")
print("---------------------------")
print(f"Total:     ${total}")
print("===========================")
print()

#Section 5

name = input("your name: ")
hometown = input("your hometown: ")
hobby = input("your hobby: ")
fun_fact =   input("fun fact about you: ")
birth_year = int (input("What year were you born? "))
profile_age = 2026 - birth_year

print("╔══════════════════════════════╗")
print(f"      PROFILE:  {name}")
print("╚══════════════════════════════╝")
print(f"Hometown: {hometown}")
print(f"Hobby:  {hobby}")
print(f"Fun fact:  {fun_fact}")
print(f"Age: {profile_age}")
