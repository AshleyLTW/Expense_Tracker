import csv, sys, sqlite3

# python3 [script name] [downloaded file]

connection = sqlite3.connect("foo.db")
cursor = connection.cursor()

create = "CREATE TABLE expenses(item text not null);"
cursor.execute(create)

downloadedFile = sys.argv[1]
with open(downloadedFile) as myfile:
	readCSV = csv.DictReader(myfile)
	for row in readCSV:
		item = row['Category']
		
		insert = "INSERT INTO expenses VALUES(?);"
		cursor.execute(insert, (item,)) # Necessary beacuse python sees each char as separate bind values (it is regarded as a grouped expression not a tuple)

cursor.close()
connection.commit()	
connection.close()

# TO DO: make more efficient by creating some sort of dir that stores all the items and then adds them to db in one go