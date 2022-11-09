from flask import Flask,render_template,request
import pandas as pd, pickle
data = pd.read_csv("dataset.csv")
app = Flask(__name__)

model = pickle.load(open('Linearmodel.pkl','rb'))
@app.route('/')
def index():
    unis = sorted(data['University Rating'].unique())
    lors = sorted(data['LOR '].unique())
    researchs = sorted(data['Research'].unique())
    sops = sorted(data['SOP'].unique())
    return render_template('index.html',unis=unis,sops =sops, lors = lors, researchs=researchs)



@app.route('/predict',methods = ['post'])
def predict():
    gre = int(request.form.get('gre'))
    tofel = int(request.form.get('tofel'))
    uni = int(request.form.get('uni'))
    sop = float(request.form.get('sop'))
    lor = float(request.form.get('lor'))
    cgpa = float(request.form.get('cgpa'))
    research = int(request.form.get('research'))
    print(gre,tofel,uni,sop,lor,cgpa,research)
    input = pd.DataFrame([[gre,tofel,uni,sop,lor,cgpa,research]],columns=['GRE Score','TOEFL Score','University Rating','SOP','LOR ','CGPA','Research'])
    x = model.predict(input)
    print(str(x))
    return str(x)

if __name__ == '__main__':
    app.run()


# GRE Score,TOEFL Score,University Rating,SOP,LOR ,CGPA,Research,Chance of Admit