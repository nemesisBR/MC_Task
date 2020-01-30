import random
import os
import requests
from flask import Flask,jsonify,request
import pandas as pd

app = Flask(__name__)

@app.route('/log', methods=['GET','POST'])
def log():
    br = "Bad Request"
    fileNotFound = "File Not Found"

    ch = request.args.get('action')

    if ch == '1':
        name = request.args.get('name')
        age = request.args.get('age')

        try:            
            df = pd.read_csv('logs.csv')
        except:
            
            #Creating a File if not present
            
            temp2 = pd.DataFrame({"name":[],
                             "age":[]})
            temp2.to_csv('logs.csv',index=False)
            

        df = pd.read_csv('logs.csv')

        temp = pd.DataFrame({"name":[name],
                             "age":[age]})

        df = df.append(temp)

        df.to_csv('logs.csv',index=False)

        sucess = "Written to logs.csv"
        
        return jsonify(sucess=sucess)   

    elif ch == '2':
        
        try:            
            df = pd.read_csv('logs.csv')
        except:
            return jsonify(Error=fileNotFound)
        

        name = request.args.get('name')


        names = list(df['name'])
        ages = list(df['age'])

        if name in names:
            index =  names.index(name)

            return jsonify(name=name,
                   age = ages[index])
        else:
            no_name = "Name Not Found"
            return jsonify(Error=no_name)
            
            
            

    else:
        return jsonify(Error= br)
    
    

    



if __name__ == "__main__":
    app.run(debug = True)
