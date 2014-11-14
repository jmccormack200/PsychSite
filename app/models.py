from app import db

class GusName(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	nickname = db.Column(db.String(120), index = False, unique = False)
	episode = db.Column(db.String(120), index = False, unique = False)
	
	def __repr__(self):
		return self.nickname		