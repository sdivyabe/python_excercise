from flask import Flask, render_template, request, redirect, url_for
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def home():
    conn=sql.connect('utube.db')
    conn.row_factory=sql.Row
    cur=conn.cursor()         
    cur.execute("select * from channel")
    data=cur.fetchall()
    return render_template("index.html",datas=data)

@app.route('/add_channel', methods=["GET","POST"])
def add_channel():
    if request.method == "POST":
        s_nextPage = request.form["nextPage"]
        s_name = request.form["name"]
        conn = sql.connect("utube.db")
        cur = conn.cursor() 
        cur.execute("insert into channel (NEXTPAGE,NAME) values(?,?)",(s_nextPage,s_name))
        conn.commit()
        return redirect (url_for('home'))
    return render_template("add_channel.html")

@app.route('/edit_channel/<string:id>', methods=['GET','POST'])
def edit_channel(id):
    if request.method == 'POST':
        pass
        s_nextPage = request.form['nextpage']
        s_name = request.form["name"]
        conn = sql.connect('utube.db')
        cur = conn.cursor()
        cur.execute('update channel set NEXTPAGE=?, NAME=? where ID=?',(s_nextPage,s_name,id))
        conn.commit()
        return (url_for('home'))
    conn = sql.connect('utube.db')
    conn.row_factory= sql.Row
    cur=conn.cursor()
    cur.execute('select * form channel where ID=?',(id,))
    data=cur.fetchone()
    return render_template('edit_channel.html', datas = data)

@app.route('/delete_channel/<string:id>', methods=['GET','POST'])
def delete_channel(id):
    conn=sql.connect('utube.db')
    cur=conn.cursor()
    cur.execute('delete from channel where ID=?',(id,))
    conn.commit()
    return redirect(url_for('home'))

if __name__=="__main__":
  app.run(debug=True)

