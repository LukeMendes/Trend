import matplotlib.pyplot
import numpy

x = []
dax = [0]
for i in range(500):
    x.append(i)
    if len(dax) != 500:
        while True:
            zufall = numpy.random.randint(0, 1000)
            if zufall <= (dax[i]+50) and zufall >= (dax[i]-50):
                break
        dax.append(zufall)
matplotlib.pyplot.plot(x, dax, color='#43a8ef', linestyle='-', label="Aktienkurs")
matplotlib.pyplot.legend()
matplotlib.pyplot.grid(True)
matplotlib.pyplot.title("Aktien")
matplotlib.pyplot.xlabel("Tage seit beginn")
matplotlib.pyplot.ylabel("Wert in €")
matplotlib.pyplot.savefig("./aktientrend.png")
matplotlib.pyplot.show()