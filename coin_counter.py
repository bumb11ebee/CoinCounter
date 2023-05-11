def count_coins(filename):
    """
    Checks every reasonable possible combination of Canadian coins that add up to $3.29
    Twoonie = $2.00
    Loonie = $1.00
    Quarter = $0.25
    Dime = $0.10
    Nickel = $0.05
    Penny = $0.01
    Technically pennies do not exist in Canada any more but this was probably a really old math sheet.
    """
    with open(filename+".csv","w") as wout:
        wout.write("Pennies,Nickels,Dimes,Quarters,Loonies,Twoonies\n")
        combinations = 0
        for twoonie in range(2): #No less than 0 and no greater than 1
            for loonie in range(4):#No less than 0 and no greater than 3
                for quarter in range(14):#No less than 0 and no greater than 13 (13*$.25=3.25)
                    for dime in range(33):#No less than 0 and no greater than 32
                        for nickel in range(65):#No less than 0 and no greater than 64
                            for penny in range(330):#No less than 0 and no greater than 329
                                cash = 1*penny+5*nickel+10*dime+25*quarter+100*loonie+200*twoonie #Add up all of the coins
                                if cash == 329:
                                    #This combination equals $3.29
                                    wout.write(f'{penny},{nickel},{dime},{quarter},{loonie},{twoonie}\n')
                                    combinations+=1
    return combinations

if __name__ == "__main__":
    print("I can write our the combinations of coins to a CSV file.")
    filename = input("What do you want to call the file? ")
    print("Total Combinations = ",str(count_coins(filename)))
