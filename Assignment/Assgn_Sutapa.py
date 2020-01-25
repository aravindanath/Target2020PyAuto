def taxCalculator(gross,state):
    state_tax={"BOS":8,"NJ":7,"CA":10,"TX":9,"NY":6}
    net = gross-(gross*.10)
    if state in state_tax:
        net = net - (gross * state_tax[state] / 100)
        print("Your net is:" + str(net))
        return net
    else:
        print("Enter your details correctly")
        return none

d = taxCalculator(876549 ,"NJ")