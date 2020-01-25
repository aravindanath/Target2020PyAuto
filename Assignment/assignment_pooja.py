def taxcalculator(state,gross):
    state_tax={"NY":4,"BOS":3,"CL":5}
    netIncome=gross-(gross*.10)

    if state in state_tax:
        netIncome=netIncome-(gross*(state_tax[state]/100))
        print("your net income " + str(netIncome))
        return netIncome
    else:
        print("enter ur details correctly")
        return none

d= taxcalculator ("NY",100000)

