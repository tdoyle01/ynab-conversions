# only for files with no registration code

import csv
import os
import operator
import sys

file = sys.argv[1]
with open(file, 'r') as csvin, open(sys.argv[1] + "-ynab" + '.csv',  'a', newline='') as csvout:
	csvout = csv.writer(csvout, delimiter=',')
	csvout.writerow(["Date", "Payee", "Outflow", "Inflow"])
	print("Reading in data")
	reader = csv.reader(csvin, delimiter=',')
	next(reader)
	rows = list(reader)[3:]
	for row in rows:
		csvout.writerow([row[0], row[4], row[5], row[6]])
	print("Converted!")
