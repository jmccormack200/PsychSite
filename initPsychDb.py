from app import db, models

#open "quotes.txt" to read in the files
#notes, reading first line induces weird errors
#ignore it for now and repeating the entry at the end

#currently hard coded, should be updated
max_lines = 106
f = open("quotes.txt".decode('utf8'), "r")
garbage = f.readline()

db.create_all()

for a in range(1, 105):
	
	rawQuote = (f.readline())
	
	splitStr = rawQuote.split('-')
	
	quote = models.GusName(id = a, nickname = splitStr[1].decode('utf-8'), episode = splitStr[0].decode('utf-8'))
	#print a
	#print quote
	#print '\n'
	db.session.add(quote)

	
db.session.commit()


users = models.GusName.query.all()
for u in users:
	print ("*******")
	print(u)
	print('\n')
