import sys
import math
import argparse

parser = argparse.ArgumentParser(description='financial calculator')
parser.add_argument('--type', type=str, help='the type of calculation')
parser.add_argument('--principal', type=float, help='principal', default=0)
parser.add_argument('--periods', type=int, help='number of months', default=0)
parser.add_argument('--payment', type=float, help='monthly payment', default=0)
parser.add_argument('--interest', type=float, help='credit_interest', default=0)
args = parser.parse_args()
if args.principal < 0 or args.periods < 0 or args.payment < 0 or args.interest < 0:
    print('Incorrect parameters d')


else:
    if len(sys.argv) != 5:
        print('Incorrect parameters')

    else:
        if args.interest == 0:
            print('Incorrect parameters')
        else:

            if args.type == 'diff':
                if args.payment:
                    print('Incorrect parameters')
                else:
                    # solution
                    # for the first month, m = 1. m stands for month
                    m = 1
                    credit_interest_rate = (args.interest / 100) / 12 * 1
                    f1 = (args.principal / args.periods)  # the 1st part of the formula

                    f2 = (args.principal - (args.principal * (m - 1)) / args.periods)  # the 2nd part of the formula

                    differentiated = math.ceil(
                        f1 + (credit_interest_rate * f2))  # the differentiated payment  of the 1st month
                    print('Month {}: paid out {}'.format(m, int(differentiated)))
                    total_diff = differentiated
                    # for the second month and so on
                    while m != args.periods:
                        m += 1
                        f1 = (args.principal / args.periods)  # the 1st part of the formula

                        f2 = (args.principal - (args.principal * (m - 1)) / args.periods)  # the 2nd part of the formula

                        differentiated = math.ceil(f1 + (
                        credit_interest_rate * f2))  # the differentiated payment  of the 1st month            print('Month {}: paid out {}'.format(m, int(differentiated)))
                        print('Month {}: paid out {}'.format(m, int(differentiated)))
                        total_diff += differentiated

                    overpayment = total_diff - args.principal
                    print('overpayment = {}'.format(int(overpayment)))
            elif args.type == "annuity":
                if args.principal == 0:
                    # solution
                    credit_interest_rate = (args.interest / 100) / 12 * 1

                    f1 = (credit_interest_rate * math.pow((1 + credit_interest_rate), args.periods))
                    f2 = (math.pow((1 + credit_interest_rate), args.periods) - 1)

                    principal = int(math.floor(args.payment / (f1 / f2)))
                    print('Your principal = {}!'.format(principal))
                    total_monthly_payment = args.payment * args.periods
                    overpayment = int(total_monthly_payment - principal)
                    print('overpayment ={} '.format(overpayment))



                elif args.payment == 0:

                    credit_interest_rate = (args.interest / 100) / 12 * 1

                    f1 = (credit_interest_rate * math.pow((1 + credit_interest_rate), args.periods))
                    f2 = (math.pow((1 + credit_interest_rate), args.periods) - 1)
                    n = f1 / f2

                    monthly_payment = int(math.ceil(n * args.principal))
                    print('Your monthly_payment = {}!'.format(monthly_payment))
                    total_monthly_payment = monthly_payment * args.periods
                    overpayment = int(total_monthly_payment - args.principal)
                    print('overpayment = {} '.format(overpayment))


                elif args.periods == 0:
                    nominal_interest = (args.interest / 100) / (12 * 1)
                    f1 = 1 + nominal_interest
                    periods = math.log((args.payment / (args.payment - nominal_interest * args.principal)), f1)
                    periods = math.ceil(periods)
                    years = periods // 12
                    months = (periods % 12)
                    if years == 0:
                        if months == 1:
                            print("you need {} month to repay the credit".format(months))
                        else:
                            print('you need {} months to repay this credit!'.format(months))

                    elif months == 0:
                        if years == 1:
                            print("you need {} year to repay the credit".format(years))
                        else:
                            print('You need {} years to repay this credit!'.format(years))
                    else:
                        if years and months == 1:
                            print("you need {} year and {} month  to repay the credit".format(years, months))
                        elif years == 1:
                            print("you need {} year and {} months  to repay the credit".format(years, months))
                        elif months == 1:
                            print("you need {} years and {} month  to repay the credit".format(years, months))

                        else:
                            print('You need {} years and {} months to repay this credit!'.format(years, months))
                    total_monthly_payment = args.payment * periods
                    overpayment = int(total_monthly_payment - args.principal)
                    print('overpayment = {} '.format(overpayment))
            else:
                print('Incorrect parameters')
