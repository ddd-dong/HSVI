from flask import Flask, render_template

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about_us')
def aboutus():
    return render_template('about_us.html')

@app.route('/work_with_us')
def rounded():
    return render_template('wantyou.html')

@app.route('/explainVtuber')
def explainVtuber():
    return render_template('whatv.html')

@app.errorhandler(404)
def erro404(e):
    return render_template('404.html'),404



if __name__=="__main__":
    app.run(debug=True, port=80) #host='0.0.0.0'