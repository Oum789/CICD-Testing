from flask import Flask

app = Flask(__name__)

@app.route('/getcode')
def get_code():
    team = 'group5: นิ่งไว้'
    return team

@app.route('/plus/<int:a>/<int:b>')
def plus(a, b):
    return str(a + b)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
