import pickle
from flask import Flask, render_template, request
import os

app = Flask(__name__)
@app.route('/')

def home():

	return render_template('home.html')


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
    
        ph = float(request.form['ph value'])
        Temperature = float(request.form['Temperature'])
        B.O.D = float(request.form['B.O.D'])
        D.O = float(request.form['D.O'])
        fecalcaliform = float(request.form['fecalcaliform'])
        Conductivity = float(request.form['Conductivity'])
        Totalcaliform = float(request.form['Totalcaliform'])
        Nitratenann = float(request.form['Nitratenann'])
        Nitritenann = float(request.form['Nitritenann'])

       
        val = np.array([ph, Temperature, B.O.D, D.O, fecalcaliform, Conductivity, Totalcaliform, Nitratenann,Nitritenann])

        
        model_path = os.path.join('models', 'xgboost.sav')
        scaler_path = os.path.join('models', 'scaler.sav')

        model = pickle.load(open(model_path, 'rb'))
        scc = pickle.load(open(scaler_path, 'rb'))

        data = scc.transform([val])

        res = model.predict(data)

        if res == 1:
            outcome = 'Potable'
        else:
            outcome = 'not potable'
        return render_template('Inputform.html', result=outcome)
    return render_template('Inputform.html')
def predict():

    if request.method == 'POST':

    	message = request.form['message']

    	data = [message]

    	vect = cv.transform(data).toarray()

    	my_prediction =randomforestregression.predict(vect)
        return render_template('potable.html', prediction=my_prediction)
    else
     return render_template('nonpotable.html', prediction=my_prediction)


if __name__ == "__main__":
    app.run(debug=True)