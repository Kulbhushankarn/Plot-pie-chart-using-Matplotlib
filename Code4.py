from matplotlib import pyplot as plt

country=["India", "Pakistan","Myanmmar","Bhutan","Nepal"]

population=[200,100,50,20,30]

plt.pie(population,labels=country)
plt.title("population")
plt.plot(country,population)
plt.show()
