# Get user inputs
annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))

# set interest rates and down payment percentage
r = float(.04)
down_percentage = float(.25)

# calculate down payment
portion_down_payment = total_cost * down_percentage
# print('portion_down_payment:', portion_down_payment)

# calculate monthly salary, and what percent of that will be saved
monthly_salary = annual_salary / 12
month_principal = monthly_salary * portion_saved
# print('monthly_salary:', monthly_salary)
# print('month_principal', month_principal)

# starting with 0 in savings also start month count
current_savings = 0
months_of_saving = 0
# print('current_savings', current_savings)

# loop until current_savings is = to portion_down_payment adding increasing current savings by 1 month_principal
# and calculating interest
while current_savings <= portion_down_payment:
    months_of_saving += 1
    current_savings += month_principal
    current_savings += (current_savings * r / 12)

# print how many months it will take to save
print('Number of months: ', months_of_saving)
