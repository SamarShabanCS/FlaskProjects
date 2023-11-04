from flask import Flask, request, redirect, url_for
app = Flask(__name__)


@app.route('/onsuc/<name>')
def onsuc(name):
	return "welcome " + name


@app.route('/', methods=['POST', 'GET'])
def index():
	if request.method == 'POST':
		return redirect(url_for('onsuc', name=request.form['name']))
	else:
		print(request.args)
		return redirect(url_for('onsuc', name=request.args.get('name')))
''' video#1,2
@app.route('/login/<int:id>')
def login(id):
	return 'hello samar'+str(id)


@app.route('/')
def helloflask():
	return 'hello flask'

'''
if __name__ == '__main__':
	app.run(debug=True)
