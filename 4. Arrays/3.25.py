import matplotlib.pyplot as plt

# f(x)=x^2-3
x=[]
y=[]
for n in range(-100,101):
    x.append(n)
    y.append(n*n-3)
plt.plot(x,y)
plt.show()
