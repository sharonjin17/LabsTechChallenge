from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/sj2846')
def sj():
    return '<h1>Sharon Jin</h2><img src="http://cdn.kickvick.com/wp-content/uploads/2015/09/cutest-bunny-rabbits-10.jpg" alt="Cute sleepy bunny :)" style="width:142px;height:142px;"><style>body{background-color:#e085dd}</style>' 


if __name__ == '__main__':
    app.run()
