# pythonspot.com
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
 
# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
import pickle

import numpy as np

class ReusableForm(Form):
    
    indication = TextField('indication',default=np.nan)
    age = TextField('Age:',default=np.nan)
    sex = TextField('Sex:',default=np.nan)
    bmi = TextField('BMI:',default=np.nan)
    ethnicity = TextField('Ethnicity:',default=np.nan)
    height = TextField('Height:' ,default=np.nan)
    weight = TextField('Weight:',default=np.nan)
    htn = TextField('htn:',default=np.nan)
    dm = TextField('dm:',default=np.nan)
    chol = TextField('chol:',default=np.nan)
    total_chol = TextField('total_chol:',default=np.nan)
    ldl = TextField('ldl:',default=np.nan)
    hdl = TextField('hdl:',default=np.nan)
    famhx = TextField('famhx:',default=np.nan)
    smokecurrent = TextField('smokecurrent:',default=np.nan)
    smokepast = TextField('smokepast:',default=np.nan)
    renal_insufficiency = TextField('renal_insufficiency:',default=np.nan)
    creatinine = TextField('creatinine:',default=np.nan)
    pv_disease = TextField('pv_disease:',default=np.nan)
    cv_disease = TextField('cv_disease:',default=np.nan)
    chest_pain = TextField('chest_pain:',default=np.nan)
    exertion = TextField('exertion:',default=np.nan)
    relief = TextField('Relief:',default=np.nan)
    typicality = TextField('typicality:',default=np.nan)
    sob = TextField('sob:',default=np.nan)
    cac = TextField('cac:',default=np.nan)
    
    
@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
    
    #if request.method == 'GET':
#     for k in form:
#         print(k)
#         form[k] = ''

    print (form.errors)
    if request.method == 'POST':
        
        inp_var = []
        for k in request.form:
            print(k)
            inp_var.append(request.form[k])
        
        #print (name, " ", email, " ", password) 
#         if form.validate():
#             # Save the comment here.
#             flash('Thanks for registration ' + name)
#         else:
#             flash('Error: All the form fields are required. ')
        pickle.dump(inp_var,open('inp_var.pkl','wb'))
        
        return result()
    return render_template('hello.html', form=form)


@app.route("/result",methods=['GET'])
def result():
    input_var = pickle.load(open('inp_var.pkl','rb'))
    input_var = np.array([float(i) if len(i)>0 else np.nan for i in input_var ]).reshape(1,-1)
    pickle.dump(input_var,open('blabla.pkl','wb'))
    
    model = pickle.load(open('sigmoid_calib_model2_50_MODEL.pkl','rb'))
    prob = model.predict_proba(input_var)
    return '<p>Probability of event = '+str(prob[0,1])+'<p>'
    

if __name__ == "__main__":
    app.run()