from matplotlib import pyplot as plt

country=["India", "Pakistan","Myanmmar","Bhutan","Nepal"]

population=[200,100,50,20,30]

plt.bar(country,population,color="skyblue",width=0.4,align="center")
plt.title("population")
plt.plot(country,population)
plt.show()
