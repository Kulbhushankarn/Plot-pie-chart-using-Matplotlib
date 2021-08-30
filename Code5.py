from matplotlib import pyplot as plt

country=["India", "Pakistan","Myanmmar","Bhutan","Nepal"]

population=[200,100,50,20,30]
e=[0,0.2,0,0,0]

plt.pie(population,labels=country,explode=e,shadow=True)
plt.title("Population")
plt.plot(country,population)
plt.show()
