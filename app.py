from flask import Flask,render_template,request
import pandas as pd
from models import predict_di
app=Flask(__name__)

@app.route("/")
def name():
    return render_template('home.html')

@app.route("/result", methods=["POST","GEt"])
def home( ):
    if request.method=="POST":
        a=int(request.form["year"])
        b=int(request.form["fuel"])
        c=int(request.form["seller_type"])
        d=float(request.form["transmission"])
        e=float(request.form["owner"])
        df={"year":[a],
        "fuel":[b],
        "seller_type":[c],
        "transmission":[d],
        "owner":[e],
        }
        data=pd.DataFrame(df)
        data_1=predict_di(data)
    return render_template('sub.html',data=data_1)





if __name__ == "__main__":
    app.run( debug=True )
