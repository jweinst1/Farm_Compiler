from flask import Flask, render_template, request
from farm import *
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/playground', methods=['GET', 'POST'])
def playground(result=None, usercode=None):
    if request.args.get('code', None):
        usercode = request.args['code']
        result = process_text(usercode)
    return render_template('playground.html', result=result, usercode=usercode)

def process_text(string):
    trans = Farm.compile_f(string)
    return trans

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

@app.route('/guide', methods=['GET', 'POST'])
def guide():
    return render_template('guide.html')


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
