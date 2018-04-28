# # find the best rate of savings to achieve a down payment on $1M house in 36 months

# init salary variables
starting_annual_salary = float(input('Enter your annual salary: '))
r = float(.04)
semi_annual_raise = float(.07)

# init pay_in_three_years as True
pay_in_three_years = True

# init house variables
total_cost = float(1000000)
down_percentage = float(.25)
total_down_payment = total_cost * down_percentage

# init search variables
epsilon = 100
bisection_search_steps = 0

# use integers as portion saved percentage
max_portion_saved = 10000
min_portion_saved = 0
best_portion_saved_integer = max_portion_saved


while True:
    bisection_search_steps += 1
    annual_salary = starting_annual_salary
    best_portion_saved = best_portion_saved_integer / 10000
    monthly_saving = (annual_salary / 12) * best_portion_saved
    current_savings = 0
    months_of_saving = 0

    # print(current_savings)
    # print(best_portion_saved_integer)
    while months_of_saving <= 36:
        current_savings += monthly_saving + ((current_savings * r) / 12)
        months_of_saving += 1

        if months_of_saving % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise
            monthly_saving = (annual_salary / 12) * best_portion_saved

    if abs(current_savings - total_down_payment) <= epsilon:
        break

    if current_savings > total_down_payment:
        max_portion_saved = best_portion_saved_integer
    else:
        min_portion_saved = best_portion_saved_integer

    if min_portion_saved >= max_portion_saved:
        pay_in_three_years = False
        break
    best_portion_saved_integer = (max_portion_saved + min_portion_saved) // 2
if pay_in_three_years:
    print('Best savings rate: ', best_portion_saved)
    print('Steps in bisection search: ', bisection_search_steps)
else:
    print('It is not possible to pay the down payment in three years.')
