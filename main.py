from flask import Flask, render_template, jsonify
from database import load_jobs, load_job_from_db

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    jobs_ = load_jobs()
    print(jobs_)
    return render_template('home.html', jobs=jobs_, company_name='Paata')


@app.route('/jobs')
def jobs():
    jobs_ = load_jobs()
    return jsonify(jobs_)


@app.route('/job/<id_>')
def show_job(id_):
    job = load_job_from_db(id_)
    if not job:
        return 'Not Found',404
    return render_template('jobpage.html', job=job)


if __name__ == '__main__':
    app.run(debug=True)
