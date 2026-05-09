from datetime import datetime

def calculate_age(birthdate):
    birth_date = datetime.strptime(birthdate, "%d-%m-%Y")
    today = datetime.today()
    age = today.year - birth_date.year

    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    return age

def convert_to_dollars(rupees):
    exchange_rate = 83   
    dollars = rupees / exchange_rate
    return dollars

birthdate = input("Enter birthdate (DD-MM-YYYY): ")
salary_rupees = float(input("Enter salary in rupees: "))

age = calculate_age(birthdate)
salary_dollars = convert_to_dollars(salary_rupees)

print("Age:", age, "years")
print("Salary in Dollars: $", round(salary_dollars, 2))