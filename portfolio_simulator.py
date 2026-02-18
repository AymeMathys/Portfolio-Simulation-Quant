import math
#We try to simulate a portfolio management with starting balance, a monthly withdrawal and for a determined time
#The goal is to know if the client will gain or lose money, we will be able to tell if he can live with his interests without diminishing his starting balance

balance = starting_balance= float(input("Enter the starting balance : "))
monthly_return = (1+0.008) #this is about 10% per year
monthly_withdrawals = P = float(input("How much you want to withdraw every month ? : "))
investment_horizon = int(input("For how long you want to keep your portfolio ? (in months) : ")) 
whole_bank_fees = 0
# the management fees are set at 1.2% of the balance, paid once every year
print(f"Your starting balance {balance}€, the monthly return is {monthly_return}, your monthly withdrawal is {monthly_withdrawals}€, fees of 1.2% will be applied everywhere out of your balance, all of this during {investment_horizon} months.")
for i in range(investment_horizon) :
    if (i+1)%12 != 0 :
        balance = balance*monthly_return-monthly_withdrawals
    else :
        management_fees = balance*0.012
        balance = balance*monthly_return-monthly_withdrawals-management_fees
        whole_bank_fees += management_fees
    print(f"At month {i+1}, you have {balance:.2f}€")
    if balance <=0 :
            print(f"Your balance is inferior to 0 at month {i+1}, you live above your interests")
            break
if balance >= starting_balance :
            print(f"Your ending balance is ({balance:.2f}) is superior to your starting balance ({starting_balance:.2f}) ")
            print(f"You gained {balance-starting_balance:.2f}€")
            print("Congrats ! You can now live out of your interests without losing your starting balance")
            print(f"The management fees cost a total of {whole_bank_fees:.2f}€ in {int(investment_horizon/12)} years")
else :
             print(f"Your final balance is inferior to your initial balance, you lost {abs(balance-starting_balance):.2f}€")
             print("If you don't want to lose the starting balance, withdraw less money")
             print(f"The management fees cost a total of {whole_bank_fees:.2f}€ in {int(investment_horizon/12)} years")
