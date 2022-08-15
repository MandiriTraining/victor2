from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	# return 'Web App with Python Flask!'
	name = 'Rosalia'
	return render_template('index.html', title='Welcome', username=name)

app.run(host='0.0.0.0', port=81)
