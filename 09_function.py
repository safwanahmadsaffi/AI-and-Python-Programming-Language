a=10
b=20
c=9
d=11
gmean=(a*b)/(a+b)
gmean1=(c*d)/(c+d)
print(gmean)
print(gmean1)
def display(k):
    if k > 0:   # Base Case
        display(k - 1)
        print(k)

# Driver Code
a = eval(input("\n\nEnter a Number:"))
display(a)

def my_function(x):
  return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9)) 
