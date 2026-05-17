from flask import Flask, render_template, url_for
from data.db_session import create_session, global_init
from jobs_request import get_jobs

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    context = {'title': '', 'works_list': get_jobs(session)}
    return render_template('index.html', **context)


if __name__ == '__main__':
    global_init('db/mars.sqlite')
    session = create_session()
    app.run(port=8080, host='127.0.0.1', debug=False)
