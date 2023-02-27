import sqlite3 as sql
from functools import wraps
from flask import session,flash,redirect,url_for

import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

fx = os.path.join(BASE_DIR, "Pharmacy.db")

def list_dcream():
	with sql.connect(fx) as db:
		qry = 'select * from Drug where D_Form="Cream"'
		result = db.execute(qry)
		return result

def list_dtablet():
	with sql.connect(fx) as db:
		qry = 'select * from Drug where D_Form="Tablet"'
		result = db.execute(qry)
		return result

def list_dcapsule():
	with sql.connect(fx) as db:
		qry = 'select * from Drug where D_Form="Capsule"'
		result = db.execute(qry)
		return result

def list_dsyrup():
	with sql.connect(fx) as db:
		qry = 'select * from Drug where D_Form="Syrup"'
		result = db.execute(qry)
		return result

def list_dpowder():
	with sql.connect(fx) as db:
		qry = 'select * from Drug where D_Form="Powder"'
		result = db.execute(qry)
		return result

def list_all():
	with sql.connect(fx) as db:
		qry = 'select * from Drug'
		result = db.execute(qry)
		return result

def insert_drug(D_ID,D_Name,D_Form,D_Dose,D_Expired):
	with sql.connect(fx) as db:
		qry = 'insert into Drug (D_ID,D_Name,D_Form,D_Dose,D_Expired) values (?,?,?,?,?)'
		db.execute(qry,(D_ID,D_Name,D_Form,D_Dose,D_Expired))

def insert_patient(a,b,c,d,e):
	with sql.connect(fx) as db:
		qry = 'insert into Patients (Pat_Name,Pat_Address,Pat_DateBirth,Pat_PhoneNo,Pat_Medrecord) values (?,?,?,?,?)'
		db.execute(qry,(a,b,c,d,e))

def update_human(a,b,c,d,e,f):
	with sql.connect(fx) as db:
		qry = 'update Patients set Pat_Name=?,Pat_Address=?,Pat_DateBirth=?,Pat_PhoneNo=?,Pat_Medrecord=? where Pat_ID=?'
		db.execute(qry,(a,b,c,d,e,f))


def del_drug(noID):
	with sql.connect(fx) as db:
		qry ='delete from Drug where D_ID=?'
		db.execute(qry,(noID,))

def grep_drug(noID):
	with sql.connect(fx) as db:
		qry = 'select * from Drug where D_ID=?'
		result = db.execute(qry,(noID,)).fetchone()
		return (result)

def update_drug(D_ID,D_Name,D_Form,D_Dose,D_Expired):
	with sql.connect(fx) as db:
		qry = 'update Drug set D_Name=?,D_Form=?,D_Dose=?,D_Expired=? where D_ID=?'
		db.execute(qry, (D_Name,D_Form,D_Dose,D_Expired,D_ID))

def get_pat():
	with sql.connect(fx) as db:
		qry  = 'select * from Patients'
		result = db.execute(qry)
		return result

def del_patient(noID):
	with sql.connect(fx) as db:
		qry ='delete from Patients where Pat_ID=?'
		db.execute(qry,(noID,))

def grep_patient(noID):
	with sql.connect(fx) as db:
		qry = 'select * from Patients where Pat_ID=?'
		result = db.execute(qry,(noID,)).fetchone()
		return (result)

def addpre(a,b,c,d):
	with sql.connect(fx) as db:
		qry = 'insert into Prescription (Pat_ID,D_ID,Pre_Quantity,Payment) values (?,?,?,?);'
		db.execute(qry, (a,b,c,d))

def get_info(noID):
	with sql.connect(fx) as db:
		qry = 'SELECT Patients.Pat_Name, Patients.Pat_DateBIrth, Patients.Pat_PhoneNo ,Patients.Pat_Address, Patients.Pat_Medrecord from Prescription, Patients where Prescription.Pat_ID = Patients.Pat_ID and Prescription.Pat_ID=?'
		result = db.execute(qry,(noID,)).fetchone()
		return (result)

def getpred(noID):
	with sql.connect(fx) as db:
		qry = 'SELECT Drug.D_Name, Drug.D_Form, Drug.D_Dose, Drug.D_Expired, Prescription.Pre_Quantity, Prescription.Payment from Prescription, Patients, Drug where Prescription.Pat_ID = Patients.Pat_ID and Prescription.D_ID = Drug.D_ID and Prescription.Pat_ID=?'
		result = db.execute(qry,(noID,))
		return (result)

def getmoney(noID):
	with sql.connect(fx) as db:
		qry = 'SELECT sum(Prescription.Payment) from Prescription, Patients, Drug where Prescription.Pat_ID = Patients.Pat_ID and Prescription.D_ID = Drug.D_ID and Prescription.Pat_ID=?'
		result = db.execute(qry,(noID,)).fetchone()
		return (result)

def find_get(a):
	with sql.connect(fx) as db:
		qry = 'select * from Patients where Pat_Name=?'
		result = db.execute(qry,(a,)).fetchone()
		return (result)

def verify(username,password):
	if username == 'admin' and password == 'admin':
		return True
	else:
		return None

def get_money():
	with sql.connect(fx) as db:
		qry = 'SELECT sum(Prescription.Payment) from Prescription, Patients, Drug where Prescription.Pat_ID = Patients.Pat_ID and Prescription.D_ID = Drug.D_ID and Prescription.Pat_ID="1"'
		result = db.execute(qry,).fetchone()
		return (result)

def login_required(f):
  @wraps(f)
  def wrap(*args, **kwargs):
    if 'logged_in' in session:
        return f(*args, **kwargs)
    else:
        flash("You need to login first")
        return redirect(url_for('home'))
  return wrap

def getinfo(g):
	with sql.connect(fx) as db:
		qry = 'SELECT Patients.Pat_Name, Patients.Pat_DateBIrth, Patients.Pat_PhoneNo ,Patients.Pat_Address, Patients.Pat_Medrecord from Prescription, Patients where Prescription.Pat_ID = Patients.Pat_ID and Patients.Pat_Name=?'
		result = db.execute(qry,(g,)).fetchone()
		return (result)

def get_pred(g):
	with sql.connect(fx) as db:
		qry = 'SELECT Drug.D_Name, Drug.D_Form, Drug.D_Dose, Drug.D_Expired, Prescription.Pre_Quantity, Prescription.Payment from Prescription, Patients, Drug where Prescription.Pat_ID = Patients.Pat_ID and Prescription.D_ID = Drug.D_ID and Patients.Pat_Name=?'
		result = db.execute(qry,(g,))
		return (result)

def get_money(g):
	with sql.connect(fx) as db:
		qry = 'SELECT sum(Prescription.Payment) from Prescription, Patients, Drug where Prescription.Pat_ID = Patients.Pat_ID and Prescription.D_ID = Drug.D_ID and Patients.Pat_Name=?'
		result = db.execute(qry,(g,)).fetchone()
		return (result)