

def taxCaluculator(gross,state):

    state_tax={"BOS":9.9,"NJ":8.3,"Tx":7.99,"CA":10.3,"NY":6.43}

    net = gross - (gross * .10)

    if state in state_tax:
        net = net - (gross * state_tax[state] / 100)
        print("Your net income after all the heavy taxes is : " + str(net))
        return net
    else:
        print("Enter your details correctly!")
        return none


d = taxCaluculator(7388276,"NJ")