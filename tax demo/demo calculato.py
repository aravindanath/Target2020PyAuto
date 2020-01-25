def tax_calculator(gross,state):
    state_tax={"Bs":8,"alska":7,"AP":6}
    net = gross-(gross*.10)
    if state in state_tax:
        net = net-(gross*state_tax[state]/100)
        print("your net income after all heavy taxes is:"+str(net))
        return net
    else:
        print("enter your details correctly!")
        return None

d=tax_calculator(3428734538,"Bs")