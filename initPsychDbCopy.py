from app import db, models

#open "quotes.txt" to read in the files
#notes, reading first line induces weird errors
#ignore it for now and repeating the entry at the end

#currently hard coded, should be updated
max_lines = 106
f = open("quotes.txt", "r")
garbage = f.readline()

users = models.GusName.query.all()

for u in users:
	db.session.delete(u)
db.session.commit

for a in range(1, 105):
	
	rawQuote = f.readline()
	
	splitStr = rawQuote.split('-')
	
	quote = models.GusName(id = a, nickname = splitStr[1], episode = splitStr[0])
	print a
	print quote
	print '\n'
	db.session.add(quote)

		
db.session.commit()

users = models.GusName.query.all()
for u in users:
	print ("*******")
	print(u)
	print('\n')
