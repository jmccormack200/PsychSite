from app import app, db, models
from flask import render_template
import random

@app.route('/')
@app.route('/index')
def index():
	randomName = random.randrange(1,105)
	Name = models.GusName.query.get(randomName)
	gus = {'nickname': Name	}
	return render_template('index.html', gus = gus)

	
	