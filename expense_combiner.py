import csv, sys, sqlite3, re
# import argparse as ap

# python3 [script name] [downloaded file] [date limitation]
# make sure to delete foo.db and output.csv

connection = sqlite3.connect("foo.db")
cursor = connection.cursor()

### Create table
create = "CREATE TABLE Expenses(item text not null, date text not null, amount float not null);"
cursor.execute(create)

### Convert csv to db
downloadedFile = sys.argv[1]
with open(downloadedFile) as myfile:
	readCSV = csv.DictReader(myfile)
	for row in readCSV:
		item = row['Category']
		# Remove the time stamp on dates
		date = row['Date']
		sucDate = re.search(r"\d\d\d\d/\d\d/\d\d", date).group(0)

		# Setting amount
		amount = row['Value']

		# Remove the negative sign 
		if amount[0] == "-":
			amount = amount[1:]

		insert = "INSERT INTO expenses VALUES('" + item + "', '" + sucDate + "', " + amount + ");"
		cursor.execute(insert) 

### Begin writing to new CSV file with date restriction
limiter = sys.argv[2]
with open('output.csv', 'a', newline='') as output:
	writer = csv.writer(output, delimiter=',')
	writer.writerow(['Item', 'Date', 'Amount'])
	### Combine purchases with the same category + date and write it
	for row in cursor.execute("SELECT item, date, sum(amount) FROM expenses WHERE date>'" + limiter + "' GROUP BY date, item ORDER BY item ASC;"):
		writer.writerow(row)
	# ### Combine purchases with the same category and write it
	# for row in cursor.execute("SELECT item, sum(amount) FROM expenses WHERE date>'" + limiter + "' GROUP BY item ORDER BY item ASC;"):
	# 	writer.writerow(row)

# TO DO: get less lazy and actually use argparse to fix this
### Begin writing to new CSV file with no date restriction
# else:
# 	with open('output.csv', 'a', newline='') as output:
# 		writer = csv.writer(output, delimiter=',')
# 		writer.writerow(['Item', 'Date', 'Amount'])
# 		### Combine purchases with the same category + date and write it
# 		for row in cursor.execute("SELECT item, date, sum(amount) FROM expenses GROUP BY date, item ORDER BY date ASC;"):
# 			writer.writerow(row)

cursor.close()
connection.commit()	
connection.close()

# TO DO: make more efficient by creating some sort of dir that stores all the items and then adds them to db in one go