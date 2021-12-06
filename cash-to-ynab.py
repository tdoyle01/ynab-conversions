import csv
import os
import operator
import sys
from decimal import Decimal

file = sys.argv[1]
with open(file, 'r') as csvin, open(sys.argv[1] + "-ynab" + '.csv',  'a', newline='') as csvout:
	csvout = csv.writer(csvout, delimiter=',')
	csvout.writerow(["Date", "Payee", "Outflow", "Inflow", "Memo"])
	print("Reading in data")
	reader = csv.reader(csvin, delimiter=',')
	next(reader)
	rows = list(reader)
	rows.pop()
	for row in rows:
		outflow = 0
		inflow = 0
		date = row[1].replace(" ", "")[:10]
		payee = row[12]
		memo = row[11]
		if payee == "":
			payee = memo
			memo = ""
		amount = row[6]
		dollar_amount_stripped = amount.replace("$", "").replace(",", "").replace(" ", "")
		decimal_amount = Decimal(dollar_amount_stripped)
		if decimal_amount < 0:
			inflow = ""
			outflow = abs(decimal_amount)
		else:
			outflow = ""
			inflow = abs(decimal_amount)
		csvout.writerow([date, payee, outflow, inflow, memo])
	print("Converted!")
