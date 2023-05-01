from flask import Flask, render_template, jsonify

JOBS = [
    {
        "id": 1,
        "title": 'Data Scienties',
        "location": 'Remote',
        "salary": "12 000$"
    },
    {
        "id": 2,
        "title": 'Frontend',
        "location": 'Remote',
        "salary": "12 000$"
    },
    {
        "id": 3,
        "title": 'Backend',
        "location": 'Remote',
        "salary": "12 000$"
    },
    {
        "id": 4,
        "title": 'AI',
        "location": 'Remote',
        "salary": "12 000$"
    },

]
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', jobs=JOBS, company_name='Paata')


@app.route('/jobs')
def jobs():
    return jsonify(JOBS)


if __name__ == '__main__':
    app.run(debug=True)
