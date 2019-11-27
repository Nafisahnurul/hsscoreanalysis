import os
import mysql.connector
import pandas as pd
import numpy as np

#Import modul Random forest
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")
app.jinja_env.cache = None


db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="aib"
)
df = pd.read_excel("fix.xlsx")
test = pd.read_excel("fix_test.xlsx")

@app.route("/", methods=['GET', 'POST'])
def home():

    if request.method == 'POST':
        print("hihi")
        
    else:
        print("haha")
   
    return render_template(
        
    )

def main():
    
    X=df[['CITY_CODE','COUNTY_CODE','INSPECTION_YEAR']].values
    Y=df['INSPECTION_SCORE']
    #X_train,X_test,Y_train,Y_test=train_test_split(X,Y,random_state=42)
    
    rnd_clf=RandomForestClassifier(n_estimators=100)
    rnd_clf.fit(X,Y)

    test_x0 = 1
    test_x1 = 2
    test_x3 = 2030

    test_x=np.vstack((test_x0,test_x1,test_x3)).T
    test_y1=rnd_clf.predict(test_x)

    print(test_y1)
    
    port = int(os.environ.get('PORT', 8080))

    app.run(debug=True, port=port, host='0.0.0.0')


if __name__ == "__main__":
    main()