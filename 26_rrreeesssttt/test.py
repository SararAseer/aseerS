#Sarar Aseer
#SoftDev1 pd8
#26_rrreeesssttt
#2018-11-15

from flask import Flask, render_template  
import urllib.request
import json
import ssl



app = Flask(__name__)

@app.route('/')
def index():
                     context = ssl._create_unverified_context()
                     urla="https://www.boredapi.com/api/activity"
                     qa = urllib.request.Request(urla)
                     qa.add_header('User-Agent','Mozilla/5.0')
                     fa =  urllib.request.urlopen(qa,context=context)                     
                     rra = fa.read() 
                     dra = rra.decode() 
                     dataa = json.loads(dra)             
                     urlb="http://api.icndb.com/jokes/random"
                     qb = urllib.request.Request(urlb)
                     qb.add_header('User-Agent','Mozilla/5.0')
                     fb =  urllib.request.urlopen(qb,context=context)  
                     rrb = fb.read() 
                     drb = rrb.decode() 
                     datab = json.loads(drb)
                     urlc="http://api.open-notify.org/iss-now.json"
                     qc = urllib.request.Request(urlc)
                     qc.add_header('User-Agent','Mozilla/5.0')
                     fc =  urllib.request.urlopen(qc,context=context)                     
                     rrc = fc.read() 
                     drc = rrc.decode() 
                     datac = json.loads(drc)       
                     return render_template("test2.html", acitvity=datab['value']['id'],price=datab['value']['joke'], a=datac['iss_position']['latitude'], b=datac['iss_position']['longitude'], c=datac['message'],d=datac['timestamp'],  e=dataa['activity'], f=dataa['price'])
if __name__ == '__main__':
                     app.debug = True
                     app.run()

