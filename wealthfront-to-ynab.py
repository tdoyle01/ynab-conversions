import csv
import sys
from decimal import Decimal

file = sys.argv[1]
with open(file, 'r') as csvin, open(sys.argv[1] + "-ynab" + '.csv',  'a', newline='') as csvout:
	csvout = csv.writer(csvout, delimiter=',')
	csvout.writerow(["Date", "Payee", "Outflow", "Inflow", "Memo"])
	print("Reading in data")
	reader = csv.reader(csvin, delimiter=',')
	next(reader)
	for row in reader:
		date = row[0]
		payee = row[1]
		memo = row[2]
		amount = Decimal(row[3])
		if amount < 0:
			inflow = ""
			outflow = abs(amount)
		else:
			outflow = ""
			inflow = amount
		csvout.writerow([date, payee, outflow, inflow, memo])
	print("Converted!")
