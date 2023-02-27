import sqlite3 as sql
from model import *

from flask import Flask,render_template,request,redirect,jsonify
app = Flask(__name__)
app.secret_key = "fadzniaidil"
#---------------------------------------------------------------

@app.route('/')
def home():
	if not session.get('logged in'):
		return render_template('login.html')
	else:
		return render_template('home.html')

@app.route('/home',methods=['POST'])
def getlogin():
	if verify(request.form['username'],request.form['password']):
		session['logged in'] = True
		return render_template('home.html')
	else:
		flash('wrong password!')
		return render_template('login.html',message='Invalid Username or Password!')

@app.route('/main')
def main():
	return render_template('home.html')

@app.route('/logout')
def logout():
	session['logged in'] = False
	return home()

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/product')
def list_product():
	data_cream = list_dcream()
	data_tablet = list_dtablet()
	data_capsule = list_dcapsule()
	data_syrup = list_dsyrup()
	data_powder = list_dpowder()
	data_all = list_all()
	option=['Cream','Tablet','Capsule','Syrup','Powder']
	row=['']*5
	return render_template(
		'product.html',
		data_cream=data_cream,
		data_tablet=data_tablet,
		data_capsule=data_capsule,
		data_syrup=data_syrup,
		data_powder=data_powder,
		data_all=data_all,
		row=row,
		option=option)

@app.route('/goAdd',methods=['GET','POST'])
def insert_product():
	D_ID = request.form['D_ID']
	D_Name = request.form['D_Name']
	D_Form = request.form['D_Form']
	D_Dose = request.form['D_Dose']
	D_Expired = request.form['D_Expired']

	if request.method == 'POST':
		insert_drug(D_ID,D_Name,D_Form,D_Dose,D_Expired)
		return redirect('/product')

@app.route('/patAdd',methods=['GET','POST'])
def add_patient():
	a = request.form['name']
	b = request.form['address']
	c = request.form['bday']
	d = request.form['nophone']
	e = request.form['medrec']

	if request.method == 'POST':
		insert_patient(a,b,c,d,e)
		return redirect('/patient')

@app.route('/purge/<noID>')
def del_d(noID):
	del_drug(noID)
	return redirect('/product')

@app.route('/nano/<noID>')
def nano_d(noID):
	sudo = grep_drug(noID)
	status = '1'
	option=['Cream','Tablet','Capsule','Syrup','Powder']
	return render_template('nano.html',sudo=sudo,option=option)

@app.route('/goUpdate',methods=['GET','POST'])
def sudo_nano():
	D_ID = request.form['D_ID']
	D_Name = request.form['D_Name']
	D_Form = request.form['D_Form']
	D_Dose = request.form['D_Dose']
	D_Expired = request.form['D_Expired']


	if request.method=='POST':
		update_drug(D_ID,D_Name,D_Form,D_Dose,D_Expired)
		return redirect('/product')

@app.route('/patient')
def list_pat():
	list_data = get_pat()
	return render_template('patient.html',list_data=list_data)

@app.route('/patient_add')
def gopat():
	return render_template('addpat.html')

@app.route('/purge_patient/<noID>')
def del_p(noID):
	del_patient(noID)
	return redirect('/patient')

@app.route('/nano_patient/<noID>')
def nano_p(noID):
	sudo = grep_patient(noID)
	return render_template('human.html',sudo=sudo)

@app.route('/human',methods=['GET','POST'])
def human():
	a = request.form['name']
	b = request.form['address']
	c = request.form['bday']
	d = request.form['nophone']
	e = request.form['medrec']
	f = request.form['id']

	if request.method == 'POST':
		update_human(a,b,c,d,e,f)
		return redirect('/patient')

@app.route('/prescription')
def prescription():
	data_cream = list_dcream()
	data_tablet = list_dtablet()
	data_capsule = list_dcapsule()
	data_syrup = list_dsyrup()
	data_powder = list_dpowder()
	pat_data = get_pat()
	list_pat = get_pat()
	return render_template(
		'prescription.html',
		data_cream=data_cream,
		data_tablet=data_tablet,
		data_capsule=data_capsule,
		data_syrup=data_syrup,
		data_powder=data_powder,
		pat_data=pat_data,
		list_pat=list_pat
		)

@app.route('/preInsert',methods=['GET','POST'])
def pre_script_ion():
	a = request.form['a']
	b = request.form['b']
	c = request.form['c']
	d = request.form['d']

	if request.method == 'POST':
		addpre(a,b,c,d)
		return redirect('/prescription')

@app.route('/info/<noID>')
def info(noID):
	a = get_info(noID)
	b = getpred(noID)
	c = getmoney(noID)
	return render_template('result.html',a=a,b=b,c=c)

@app.route('/result')
def result():
	return render_template('result.html')

@app.route('/search',methods=['GET','POST'])
def search():
	if request.method == 'POST':
		g = request.form['a'] 
		a = getinfo(g)
		b = get_pred(g)
		c = get_money(g)
		return render_template('result.html',a=a,
		b=b,
		c=c)
	else:
		return render_template('search.html')


#---------------------------------------------------------------

if __name__ == "__main__":
	
	app.run(debug=True)
