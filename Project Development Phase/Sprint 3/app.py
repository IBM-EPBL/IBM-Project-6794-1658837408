from flask import Flask , render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('inputform.html')

@app.route('/',  methods =['POST'])
def getvalue():
    loc = request.form['loc']
    state = request.form['state']
    temp = request.form['temp']
    do = request.form['do']
    ph = request.form['ph']
    cond = request.form['cond']
    bod = request.form['bod']
    nit = request.form['nit']
    fcoli= request.form['fcoli']
    tcoli = request.form['tcoli']
    wph = float(ph) * float(0.165)
    wdo = float(do) * float(0.281)
    wbdo =float(bod) *float(0.234)
    wfcoli= float(fcoli) * float(0.09)
    wcond = float(cond) * float(0.281)
    wqi = float(wph)+float(wdo)+float(wbdo)+float(wfcoli)+float(wcond)


    return render_template('pass1.html', l=loc, s=state, t=temp, d=do, p=ph, c=cond, b=bod, n=nit, f=fcoli, tc=tcoli, wqi=wqi)


if __name__ == '__main__':
    app.run()



