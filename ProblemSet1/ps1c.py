# # find the best rate of savings to achieve a down payment on $1M house in 36 months
#
# # Get user inputs
# annual_salary = float(120000)  # float(input('Enter your annual salary: '))
# total_cost = float(1000000)
# down_percentage = float(.25)
# semi_annual_raise = float(.07)
# r1 = float(.04)/12
# r = float(.04)


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
