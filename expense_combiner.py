import csv 
import sys
import sqlite3

# python3 [script name] [downloaded file]

# downloadFile = sys.argv[1]

# with open(downloadFile) as myfile: 
# 	readCSV = csv.DictReader(myfile)
# 	with open('output.csv', 'a', newline='') as output: 
# 		fieldnames = ['Item', 'Date', 'Amount']
# 		writer = csv.DictWriter(csvfile, fieldnames=fieldnames, restval='', delimiter=',')


### Creating the table in output
# def create():
# 	create = "CREATE TABLE Expenses(item text not null, date text not null, amount float not null);"

# 	connection = sqlite3.connect("foo.db")
# 	cursor = connection.cursor()

# 	cursor.execute(create)
	
# 	cursor.close()
# 	connection.commit()
# 	connection.close()

### Converting csv to db
# def convert(downloadedFile):
# 	with open(downloadedFile) as myfile:
# 		readCSV = csv.DictReader(myfile)
# 		for row in readCSV:
# 			date = row['Date']
# 			amount = row['Value']
# 			item = row['Category']
# 			return add(date, amount, item)

# def add(date, amount, category):
# 	connection = sqlite3.connect("foo.db")
# 	cursor = connection.cursor()

# 	cursor.execute("INSERT INTO Expenses VALUES(" + category + "," + date + "," + amount + ";")

# 	cursor.close()
# 	connection.commit()
# 	connection.close()

def convert(downloadedFile):
	connection = sqlite3.connect("foo.db")
	cursor = connection.cursor()

	create = "CREATE TABLE Expenses(item text not null, date text not null, amount float not null);"
	cursor.execute(create)
	# cursor.execute(".import " + downloadedFile + " data")

	with open(downloadedFile) as fin:
		dr = csv.DictReader(fin)
		for row in dr:
			dicts = {'date': row['Date'], 'amount': row['Value'], 'item': row['Category']}
		for i in dicts:
			to_db = (i['date'], i['amount'], i['item'])
	
	cursor.executemany("INSERT INTO Expenses (item, date, amount) VALUES (?, ?);", to_db)

	cursor.close()
	connection.commit()
	connection.close()

# create()
convert(sys.argv[1])