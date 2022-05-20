# loan_principal = 'Loan principal: 1000'
# final_output = 'The loan has been repaid!'
# first_month = 'Month 1: repaid 250'
# second_month = 'Month 2: repaid 250'
# third_month = 'Month 3: repaid 500'
#
# # write your code here
# print(loan_principal)
# print(first_month)
# print(second_month)
# print(third_month)
# print(final_output)

loan_principal = int(input('Enter the loan principal:\n> '))
input_action = input('What do you want to calculate?\ntype "m" for number of monthly payments,\ntype "p" for the monthly payment:\n> ')

if input_action == 'm':
    count_moth = int(input('Enter the monthly payment:\n> '))

elif input_action == 'p':
    count_moth = int(input('Enter the number of months:\n> '))
    print(f'Your monthly payment = {int(loan_principal / count_moth)}')