
import math

class Calculator():

    def add(self,i,j):
        sum = i+j;
        return sum

    def sub(self,i,j):
        subs = i-j;
        return subs

    def mul(self,i,j):
        mu = i*j;
        return mu


class SciCalculator():

    def calPi(self):
        print("Pi value ",math.pi)

    def calSq(self,g):
        print("Sq root",math.sqrt(g))

    def mul(self, i, j):
        mu = i * j;
        return mu


class homework(SciCalculator,Calculator):

    def hm1(self):
        val =self.add(30,40)
        print("Addition of two numbers ", val)





