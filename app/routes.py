from app import app, db
import string
import random
from app.forms import UrlForm
from app.models import URL
from flask import render_template, request, redirect, abort

#@app.route('/index', methods=['POST', 'GET'])
@app.route('/', methods=['POST', 'GET'])
def index():
    def gen():
        chars = string.ascii_letters + string.digits
        length = 3
        code = ''.join(random.choice(chars) for x in range(length))
        print('verifying', code)
        exists = db.session.query(db.exists().where(URL.short_url == code)).scalar()
        if not exists:
            print('New Code is ', code)
            return code
    code = gen()
    while code is None:
        code = gen()
    
    if request.method == 'POST' and code is not None:
        form = UrlForm(request.form)
        print('will try validating')
        if form.validate():
            print('form is valid')
            u = URL(short_url=code, original_url=form.original_url)
            url = form.save_url(u)
            db.session.add(url)
            db.session.commit()
            return render_template('success.html', code=code, old=url.original_url)
    else:
        print('request is GET')
        form = UrlForm()

    return render_template('index.html', form=form)


@app.route('/<new>')
def redirect_to_old(new):
    new = URL.query.filter_by(short_url=new).first()
    if new is None:
        abort(404)
    else:
        new.hits = new.hits + 1
        db.session.add(new)
        db.session.commit()
    return redirect(new.original_url)

@app.route('/stats')
@app.route('/stats/<int:page>')
def stats(page=1):
    stats = URL.query.order_by(URL.id.desc()).paginate(page, 10, False)
    return render_template('stats.html', stats=stats)


@app.errorhandler(404)
def page_not_found():
    return render_template('404.html'), 404
