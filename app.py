# pythonspot.com
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField,SelectField

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
    

class ContactForm(Form):
    
    
    indication = SelectField('indication',default='',choices=[('',''),('1','chest pain')\
                                                                  ,('2','Dyspnea'),('3','Asymptomatic')\
                                                                 ,('4','Preoperative'),('5','EP'),\
                                                                 ('6','Congenital'),('7','Other')])
    age = TextField('Age:',default='')
    sex = SelectField('Sex:',default='',choices=[('',''),\
                                                     ('1','Male'),\
                                                      ('0','Female')
                                                    ])
    bmi = TextField('BMI:',default='')
    ethnicity = SelectField('Ethnicity:',default='',choices=[('',''),\
                                                     ('1','Caucasian'),\
                                                      ('2','Africa'),\
                                                      ('3','Latin America'),\
                                                      ('4','Munich'),\
                                                      ('5','South Asian'),\
                                                      ('6','Middle Eastern'),\
                                                      ('7','Other or mixed')
                                                    ])

    height = TextField('Height:' ,default='')
    weight = TextField('Weight:',default='')
    htn = SelectField('htn:',default='',choices=[('',''),('1','Yes'),('0','No')])
    dm = SelectField('dm:',default='',choices=[('',''),('1','Yes'),('0','No')])
    chol = SelectField('chol:',default='',choices=[('',''),('1','Yes'),('0','No')])
    total_chol = TextField('total_chol:',default='')
    ldl = TextField('ldl:',default='')
    hdl = TextField('hdl:',default='')
    famhx = SelectField('famhx:',default='',choices=[('',''),('1','Yes'),('0','No')])
    smokecurrent =SelectField('smokecurrent:',default='',choices=[('',''),('1','Yes'),('0','No')])
    smokepast = SelectField('smokepast:',default='',choices=[('',''),('1','Yes'),('0','No')])
    renal_insufficiency = SelectField('renal_insufficiency:',default='',choices=[('',''),('1','Yes'),('0','No')])
    creatinine = TextField('creatinine:',default='')
    pv_disease = SelectField('pv_disease:',default='',choices=[('',''),('1','Yes'),('0','No')])
    cv_disease = SelectField('cv_disease:',default='',choices=[('',''),('1','Yes'),('0','No')])
    chest_pain = SelectField('chest_pain:',default='',choices=[('',''),('1','Yes'),('0','No')])
    exertion = SelectField('exertion:',default='',choices=[('',''),('1','Yes'),('0','No')])
    relief = SelectField('Relief:',default='',choices=[('',''),('1','Yes'),('0','No')])
    typicality = SelectField('typicality:',default='',choices=[('',''),('1','noncardiac'),\
                                                                 ('2','atypical'),('0','no pain'),\
                                                                ('3','typical')])
    sob = SelectField('sob:',default='',choices=[('',''),('1','Yes'),('0','No')])
    cac = TextField('cac:',default='')
    submit = SubmitField("Send")
    


@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ContactForm(request.form)
    
    #if request.method == 'GET':
#     for k in form:
#         print(k)
#         form[k] = ''

    #print (form.errors)
    if request.method == 'POST':
        
        inp_var = []
        for k in request.form:
            #print(k)
            inp_var.append(request.form[k])
        
        #print (name, " ", email, " ", password) 
#         if form.validate():
#             # Save the comment here.
#             flash('Thanks for registration ' + name)
#         else:
#             flash('Error: All the form fields are required. ')
        pickle.dump(inp_var[:-1],open('inp_var.pkl','wb'))
        
        return result()
    return render_template('hello2.html', form=form)


@app.route("/result",methods=['GET'])
def result():
    input_var = pickle.load(open('inp_var.pkl','rb'))
    #print(input_var)
    
    p=input_var
    
    for i in range(0,len(p)):
        if p[i]=='':
            p[i]=np.nan
        else:
            p[i]=float(p[i])

    input_var = np.array(p).reshape(1,-1)
    pickle.dump(input_var,open('blabla.pkl','wb'))
    
    model = pickle.load(open('sigmoid_calib_model2_50_MODEL.pkl','rb'))
    prob = model.predict_proba(input_var)
    #return '<p>Probability of event = '+''.join([str(i) for i in input_var])+'<p>'
    
    return '<p>Probability of event = '+str(prob[0,1])+'<p>'
    

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80)
