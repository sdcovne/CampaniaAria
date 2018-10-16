from flask import Flask, render_template, redirect, url_for, request
from flask_mail import Mail, Message
from cities import City, loc_list
import geocoder
import csv
import modules
import local_settings


app = Flask(__name__)


comune = ''

app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'sebastiano.davide26@gmail.com',
	MAIL_PASSWORD = local_settings.MAIL_PASSWORD
	)


mail = Mail(app)

@app.route('/')
def home():

    
    return render_template('home.html')

@app.route('/search', methods = ['POST', 'GET'])
def search():
    if request.method == "POST":
        comune = request.form["q"]
    else:
        comune = request.args.get('q')

    return redirect(url_for('.comune', city_name = comune))


@app.route('/localize', methods = ['POST', 'GET'])
def localize():

    ip = request.environ['REMOTE_ADDR']
    ip_location =  geocoder.ip(ip)
    comune =  ip_location.city

    return redirect(url_for('.comune', city_name = comune))



@app.route('/comune')
def comune():

    global comune

    comuni_data = csv.reader(open('csv/COMUNI_COORDINATE_1.csv', 'r'))

    poll_dict = {}

    modules.write_csv()

    date = modules.get_date()
    
    o3_data = csv.reader(open('csv/pollution_data/o3.csv', 'r'))
    no2_data = csv.reader(open('csv/pollution_data/no2.csv', 'r'))
    pm10_data = csv.reader(open('csv/pollution_data/pm10.csv', 'r'))

    c = request.args.get('city_name')

    
    for com in comuni_data:
        if com[0] == c:
            comune = City(com[0],[float(com[1]), float(com[2])])


    nearest_loc = modules.get_nearest_loc(comune, loc_list)

    nearest_loc_dist = round(nearest_loc[0],1)
    
    pm10 = modules.get_value(pm10_data, nearest_loc[1])

    try:
        o3 = modules.get_value(o3_data, nearest_loc[1])
        no2 = modules.get_value(no2_data, nearest_loc[1])
        poll_dict.update({'PM10':pm10, 'o3':o3, 'no2':no2})
    except:
        poll_dict.update({'pm10':pm10})

    pm10_pct = (pm10/50)*100
    
    return render_template("comune.html", c = c, n = nearest_loc[1].decode('utf-8'), d = nearest_loc_dist, pm10 = pm10, pm10_pct = pm10_pct, poll_dict = poll_dict, date = date, int = int )

@app.route("/donazioni")
def donazioni():
    return render_template("donazioni.html")

@app.route("/scrivimi")
def scrivimi():
    return render_template("scrivimi.html")

@app.route("/send_mail", methods = ['POST', 'GET'])
def send_mail():

    sender = request.args.get('m')
    message = request.args.get('mes')
    obj =request.args.get('o')

    msg = Message(obj, sender = sender, recipients=["sebastiano.davide26@gmail.com"])

    msg.body = message + " inviata da {}".format(sender)

    mail.send(msg)

    return ('', 204)

@app.route("/search-top", methods = ['POST', 'GET'])
def search_top():
    if request.method == "POST":
        comune = request.form["st"]
    else:
        comune = request.args.get('st')

    return redirect(url_for('.comune', city_name = comune))

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/salute")
def salute():
    return render_template("salute.html")

if __name__ == '__main__':
	app.run(debug = True, host='0.0.0.0')
	
