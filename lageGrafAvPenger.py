import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import time

from matplotlib import style



def lagMatriseFraHogrente():

	matriseMedDatoOgTotalBelop = []

	with open("Hoyrente.csv") as csvfile:
		lesCSV = csv.reader(csvfile, delimiter=";")
		#print(lesCSV)

		

		var = False
		for rad in lesCSV:
			if (var):
				listeDatoOgBelop = []
				#print(rad)
				listeDatoOgBelop.append(rad[0])
				if (rad[4] != ""):
					listeDatoOgBelop.append(rad[4])
				else:
					listeDatoOgBelop.append(rad[5])

				matriseMedDatoOgTotalBelop.append(listeDatoOgBelop)
			var = True

	#print(matriseMedDatoOgTotalBelop)


	nyMatrise = matriseMedDatoOgTotalBelop[::-1]
	#print(nyMatrise)

	totalMatrise = []
	#totalMatrise.append(['01.09.2013', 4430.7])
	#print(totalMatrise)


	total = 4430.7
	for element in nyMatrise:
		tmpListe = []
		tmpListe.append(element[0])
		element[1] = element[1].replace(",", ".")
		#print(element[1])
		total += float(element[1])
		#print(total)
		tmpListe.append(total)
		totalMatrise.append(tmpListe)

	print(total)
	#print(totalMatrise)
	return(totalMatrise)


def tegnGraf(matrise):
	#print(matrise)
	#plt.plot([1,2,3], [3,2,10])

	style.use("ggplot")

	datoer = []
	belop = []

	for element in matrise:
		datoer.append(element[0])
		belop.append(element[1])

	x = [dt.datetime.strptime(d,'%d.%m.%Y').date() for d in datoer]
	y = belop

	plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
	#plt.gca().xaxis.set_major_locator(mdates.DayLocator())
	plt.plot(x,y)
	plt.gcf().autofmt_xdate()

	print(datoer)
	print(belop)

	plt.show()

def main():
	matrise = lagMatriseFraHogrente()
	#print(matrise)
	tegnGraf(matrise)

main()

