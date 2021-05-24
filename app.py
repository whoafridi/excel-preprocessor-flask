from flask import Flask, render_template, request, send_file
import pandas as pd
import openpyxl

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/csgo")
def csgo():
    return render_template('csgo_index.html')

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        file = request.form['upload-file']
        data = pd.read_excel(file)
        data = data.head(6)
        
        def remove_whitespace(s):
            t = s.replace("\n",'')
            name = ''
            points = ''
            count = 0
            for i in t:
                if i == " ":
                    count += 1
                    name += i
                    if count == 2:
                        break
                else:
                    name += i
            return name.rstrip()
        x = data['team1'].apply(remove_whitespace)
        w = data['team2'].apply(remove_whitespace)
        
        def remove_character(s):
            points = ''

            for i in (s[::-1]):
                if i == " ":
                    break
                else:
                    points += i

            return points[::-1]
        y = data['team1'].apply(remove_character)
        z = data['team2'].apply(remove_character)

        def remove_unncessary(s):
            s.replace(' ', '').replace("\n", "")
            return s
        t1_p1 = data['t1-p1'].apply(remove_unncessary)
        t1_p2 = data['t1-p2'].apply(remove_unncessary)
        t1_p3 = data['t1-p3'].apply(remove_unncessary)
        t1_p4 = data['t1-p4'].apply(remove_unncessary)
        t1_p5 = data['t1-p5'].apply(remove_unncessary)
        t2_p1 = data['t2-p1'].apply(remove_unncessary)
        t2_p2 = data['t2-p2'].apply(remove_unncessary)
        t2_p3 = data['t2-p3'].apply(remove_unncessary)
        t2_p4 = data['t2-p4'].apply(remove_unncessary)
        t2_p5 = data['t2-p5'].apply(remove_unncessary)
        pom   = data['pom'].apply(remove_unncessary)

        dict = {'team-1': x, 'team-1-points': y,'team-2': w, 'team-2-points': z, 't1-p1':t1_p1,
                't1-p2':t1_p2,'t1-p3':t1_p3,'t1-p4':t1_p4,'t1-p5':t1_p5,'t2-p1':t2_p1,
                't2-p2':t2_p2,'t2-p3':t2_p3,'t2-p4':t2_p4,'t2-p5':t2_p5,'pom':pom}
        df = pd.DataFrame(dict)
        dataset = df.to_excel("csgo-db-1.xlsx", index=False)
        

        return render_template('data.html', data=data.to_html(index=False),df=df.to_html(index=False))

@app.route("/players")
def player():
    return render_template('player_index.html')

@app.route("/show", methods=['GET','POST'])
def show():
    if request.method == 'POST':
        file = request.form['upload-file']
        df = pd.read_excel(file)
        df = df.head(6)
        def remove_unncessary(s):
            t= s.replace(' ', '').replace("\n", "")
            return t
        x = df['nick-name'].apply(remove_unncessary)

        def remove_avg(s):
            t = s.replace(' ', '').replace("\n", "").replace("%",'').replace("Avg.", '')
            return t
        y = df['rating'].apply(remove_avg)
        w = df['impact'].apply(remove_avg)
        z = df['KAST'].apply(remove_avg)

        dict = {'nick-name': x, 'rating': y, 'impact':w, "KAST": z}
        df1 = pd.DataFrame(dict)
        dataset = df1.to_excel("players-info-1.xlsx", index=False)

        return render_template('player_show.html', df=df.to_html(index=False),df1=df1.to_html(index=False))

if __name__ == '__main__':
    app.run(debug=True)
