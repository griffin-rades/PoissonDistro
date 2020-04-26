import math

#Enter a lambda value and calculate the probability until 99.99% has been found
def poisson(x):
    i = 0;
    total = 0;
    while(total < .9999):
        total += math.exp(-x)*((x**i)/math.factorial(i)) #Poisson Distro Formula
        
        print(i, math.exp(-x)*((x**i)/math.factorial(i)))
        i += 1;

        
        
