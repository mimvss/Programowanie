# sin(x)
x=[]
y=[]
for deg in range(361):
    x.append(deg)
    y.append(math.sin(math.radians(deg)))
plt.plot(x,y)
plt.show()
