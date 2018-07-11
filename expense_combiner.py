import csv, sys, sqlite3

# python3 [script name] [downloaded file]

connection = sqlite3.connect("foo.db")
cursor = connection.cursor()

create = "CREATE TABLE Expenses(item text not null, date text not null, amount float not null);"
cursor.execute(create)

downloadedFile = sys.argv[1]
with open(downloadedFile) as myfile:
	readCSV = csv.DictReader(myfile)
	for row in readCSV:
		item = row['Category']
		date = row['Date']
		amount = row['Value']
		
		insert = "INSERT INTO expenses VALUES('" + item + "', '" + date + "', " + amount + ");"
		cursor.execute(insert) 

cursor.close()
connection.commit()	
connection.close()

# TO DO: make more efficient by creating some sort of dir that stores all the items and then adds them to db in one go