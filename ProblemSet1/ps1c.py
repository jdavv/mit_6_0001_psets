# # find the best rate of savings to achieve a down payment on $1M house in 36 months

# init salary variables
start_annual_salary = float(120000)  # float(input('Enter your annual salary: '))
r1 = float(.04)/12
r = float(.04)
semi_annual_raise = float(.07)
monthly_salary = start_annual_salary / 12

# init house variables
total_cost = float(1000000)
down_percentage = float(.25)
total_down_payment = total_cost * down_percentage

# init search variables
epsilon = 100
bisection_search_steps = 0
max_portion_saved = 10000
min_portion_saved = 0


while True:
    bisection_search_steps += 1
    current_savings = 0
    months_of_saving = 0
    current_savings += monthly_salary
    current_savings += (current_savings * r / 12)
    print(current_savings)

# Example from lecture #3 slides for bisection search

# cube = 27
# epsilon = 0.01
# num_guesses = 0
# low = 0
# high = cube
# guess = (high + low) / 2.0
# while abs(guess**3 - cube) >= epsilon:
#     if guess**3 < cube:
#         low = guess
#     else:
#         high = guess
#     guess = (high + low) / 2.0
#     num_guesses +=1
# print('num_guesses = ', num_guesses)
# print(guess, 'is close to the cube root of', cube)


