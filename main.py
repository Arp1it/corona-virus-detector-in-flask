from flask import Flask, render_template, request
import pickle
app = Flask(__name__)

with open("model.pkl", "rb") as f:
    clf = pickle.load(f)
@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        mydict = request.form
        fever = int(mydict['fever'])
        Age = int(mydict['Age'])
        bodypain = int(mydict['bodypain'])
        diffBreath = int(mydict['diffBreath'])
        runnyNose = int(mydict['runnyNose'])

        infection = [fever, bodypain, Age, runnyNose, diffBreath]
        infProb = clf.predict_proba([infection])[0][1]
        infProb = infProb*10
        return render_template('show.html', inf=round(infProb, 5))
    # print(int(infProb*100))
    return render_template('index.html')
    # return "Hello World" + str(infProb)

if __name__=="__main__":
    app.run(debug=True)