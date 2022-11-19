from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template("index1.html")


@app.route('/input', methods=['GET', 'POST'])
def form_example():
    # handle the POST request
    if request.method == 'POST':
        loc = request.form.get('loc')
        state = request.form.get('state')
        temp = request.form.get('temp')
        doi = request.form.get('doi')
        ph = request.form.get('ph')
        cond = request.form.get('cond')
        bod = request.form.get('bod')
        nit = request.form.get('nit')
        fcoli = request.form.get('fcoli')
        tcoli = request.form.get('tcoli')
        wph = float(ph or 0) * float(0.165 or 0)
        wdo = float(doi or 0) * float(0.281 or 0)
        wbdo = float(bod or 0) * float(0.234 or 0)
        wfcoli = float(fcoli or 0) * float(0.09 or 0)
        wcond = float(cond or 0) * float(0.281 or 0)
        wqi = float(wph) + float(wdo) + float(wbdo) + float(wfcoli) + float(wcond)
        wq = int(wqi)
        if wq in range(95, 100):
            ll = " Excellent, The predicted value is ";
        elif wq in range(89, 94):
            ll = "Very good, The predicted value is";
        elif wq in range(80, 88):
            ll = "Good, The predicted value is";
        elif wq in range(65, 79):
            ll = "Fair, The predicted value is ";
        elif wq in range(45, 64):
            ll = "Marginal, The predicted value is ";
        else:
            ll = "Poor, The predicted value is";

        return render_template("pass11.html", l=loc, s=state, t=temp, d=doi, p=ph, c=cond, b=bod, n=nit, f=fcoli,
                               tc=tcoli,
                               wqi=wqi, ll=ll)


if __name__ == '__main__':
    app.debug = True
    app.run()
