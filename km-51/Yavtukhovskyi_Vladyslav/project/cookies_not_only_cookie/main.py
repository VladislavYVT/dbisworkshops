from datetime import datetime, timedelta
from http import cookies

from flask import Flask, render_template, request, make_response, flash, url_for, redirect, session
from wtf.form.login import UserForm
from wtf.form.NewForm1D import Cr1D, Cr2D, DateB, HistoryForm, upd_test
from wtf.form.registration import  RegistrationForm
from db import User
import io
import random
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from flask import Response
from flask_menu import Menu, register_menu
from matplotlib import dates

uname = 'Vlod'
password = 'xnjnjnj21a'
dsn = 'localhost:1521/xe'

app = Flask(__name__)
app.secret_key = 'dev_key'
Menu(app=app)


def is_login():
    if 'login' in session:
        return True
    elif request.cookies.get('login') is None:
        return False
    else:
        session['login'] = request.cookies.get('login')
        return True


@app.route('/')
@register_menu(app, '.', 'Home')
def index():
    if not is_login():
        return redirect('/login')
    else:
        return render_template('index.html', login=session.get('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if is_login():
        return redirect('/')
    form = UserForm()
    if request.method == 'GET':
        return render_template('login.html', form=form)

    if request.method == 'POST':

        if not form.validate():
            return render_template('login.html', form=form)
        else:
            user = User()
            res = user.login_user(request.form['login'], request.form['password'])
            if res:
                response = make_response(redirect('/'))
                expires = datetime.now()
                expires += timedelta(days=60)
                response.set_cookie('cookie_name', request.form['login'], expires=expires)
                session['login'] = request.form['login']
                return response
            else:
                return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if is_login():
        return render_template('index.html', login = session['login'])
    form = UserForm()
    if request.method == 'GET':
        return render_template('registration.html', form=form)

    if request.method == 'POST':

        if not form.validate():
            return render_template('registration.html', form=form)
        else:
            user = User()
            res = user.reg_user(request.form['login'], request.form['password'])
            if res:
                response = make_response(redirect('/'))
                expires = datetime.now()
                expires += timedelta(days=60)
                response.set_cookie('cookie_name', request.form['login'], expires=expires)
                session['login'] = request.form['login']
                return response
            else:
                if is_login():
                    return render_template('index.html', login=session.get('login'))
                else:
                    return render_template('login.html', form=form)


@app.route('/logout')
@register_menu(app, '.logout', 'Logout', order=9)
def logout():
        response = make_response(redirect('/login'))
        response.set_cookie('cookie_name', '', expires=0)
        session.pop('login', None)
        return response


@app.route('/new_weakness', methods = ['GET', 'POST'])

def n_weak():
    if not is_login():
        return redirect('/login')
    else:
        form = Cr1D()
        if request.method == 'GET':
            return render_template('New1D.html', form=form)

        if request.method == 'POST':
            if not form.validate():
                return render_template('New1D.html', form=form)
            else:
                res = User().new_weak(request.form['data_field'])
                if res:
                    return render_template('index.html', login=session.get('login'))
                else:
                    return render_template('New1D.html', form=form)


@app.route('/new_medicine', methods = ['GET', 'POST'])
def n_med():
    if not is_login():
        return redirect('/login')
    else:
        form = Cr1D()
        if request.method == 'GET':
            return render_template('New1D.html', form=form)

        if request.method == 'POST':
            if not form.validate():
                return render_template('New1D.html', form=form)
            else:
                res = User().new_med(request.form['data_field'])
                if res:
                    return render_template('index.html', login=session.get('login'))
                else:
                    return render_template('New1D.html', form=form)


@app.route('/new_syndrom', methods = ['GET', 'POST'])
def n_synd():
    if not is_login():
        return redirect('/login')
    else:
        form = Cr1D()
        if request.method == 'GET':
            return render_template('New1D.html', form=form)

        if request.method == 'POST':
            if not form.validate():
                return render_template('New1D.html', form=form)
            else:
                res = User().new_synd(request.form['data_field'])
                if res:
                    return render_template('index.html', login=session.get('login'))
                else:
                    return render_template('New1D.html', form=form)



@app.route('/delweakness', methods = ['GET', 'POST'])
def d_weak():
    if not is_login():
        return redirect('/login')
    else:
        form = Cr1D()
        if request.method == 'GET':
            return render_template('New1D.html', form=form)

        if request.method == 'POST':
            if not form.validate():
                return render_template('New1D.html', form=form)
            else:
                res = User().del_weak(request.form['data_field'])
                if res:
                    return render_template('index.html', login=session.get('login'))
                else:
                    return render_template('New1D.html', form=form)


@app.route('/del_medicine', methods = ['GET', 'POST'])
def d_med():
    if not is_login():
        return redirect('/login')
    else:
        form = Cr1D()
        if request.method == 'GET':
            return render_template('New1D.html', form=form)

        if request.method == 'POST':
            if not form.validate():
                return render_template('New1D.html', form=form)
            else:
                res = User().del_med(request.form['data_field'])
                if res:
                    return render_template('index.html', login=session.get('login'))
                else:
                    return render_template('New1D.html', form=form)

@app.route('/del_syndrom', methods = ['GET', 'POST'])
def d_synd():
    if not is_login():
        return redirect('/login')
    else:
        form = Cr1D()
        if request.method == 'GET':
            return render_template('New1D.html', form=form)

        if request.method == 'POST':
            if not form.validate():
                return render_template('New1D.html', form=form)
            else:
                res = User().del_synd(request.form['data_field'])
                if res:
                    return render_template('index.html', login=session.get('login'))
                else:
                    return render_template('New1D.html', form=form)


@app.route('/new_del')
@register_menu(app, '.create_or_delete_msw', 'Create or delete MSW', order=2)
def n_d():
    if not is_login():
        return redirect('/login')
    else:
        form = Cr1D()
        data_weak= User().list_weaks()
        data_synd = User().list_syndromes()
        data_meds = User().list_meds()
        return render_template('New1D.html', form=form, data_w = data_weak, data_s = data_synd, data_m=data_meds)

@app.route('/d2')
@register_menu(app, '.modify_ws_mw', 'Modify data about sydromes of weaknesses and medicines for weaknesses', order=3)
def d2():
    if not is_login():
        return redirect('/login')
    else:
        data_ws = User().list_weak_with_synd()
        data_mw = User().list_medicine_for_weakness()
        form = Cr2D()
        return render_template('New2D.html',form=form, data_ws=data_ws, data_mw=data_mw)


@app.route('/new_weak_has_synd', methods = ['GET', 'POST'])
def w_h_synd():
    if not is_login():
        return redirect('/login')
    else:
        form = Cr2D()
        if request.method == 'GET':
            return render_template('New2D.html', form=form)

        if request.method == 'POST':
            if not form.validate():
                return render_template('New2D.html', form=form)
            else:
                res = User().new_syndrom_of_weakness(request.form['data1_field'], request.form['data2_field'])
                if res:
                    return render_template('index.html', login=session.get('login'))
                else:
                    return render_template('New2D.html', form=form)


@app.route('/med_for_weak', methods = ['GET', 'POST'])
def med_for_wek():
    if not is_login():
        return redirect('/login')
    else:
        form = Cr2D()
        if request.method == 'GET':
            return render_template('New2D.html', form=form)

        if request.method == 'POST':
            if not form.validate():
                return render_template('New2D.html', form=form)
            else:
                res = User().new_medicine_for_weakness(request.form['data1_field'], request.form['data2_field'])
                if res:
                    return render_template('index.html', login=session.get('login'))
                else:
                    return render_template('New2D.html', form=form)


@app.route('/del_weak_has_synd', methods=['GET', 'POST'])
def del_w_h_synd():
    if not is_login():
        return redirect('/login')
    else:
        form = Cr2D()
        if request.method == 'GET':
            return render_template('New2D.html', form=form)

        if request.method == 'POST':
            if not form.validate():
                return render_template('New2D.html', form=form)
            else:
                res = User().del_syndrom_of_weakness(request.form['data1_field'], request.form['data2_field'])
                if res:
                    return render_template('index.html', login=session.get('login'))
                else:
                    return render_template('New2D.html', form=form)


@app.route('/del_med_for_weak', methods=['GET', 'POST'])
def del_med_for_wek():
    if not is_login():
        return redirect('/login')
    else:
        form = Cr2D()
        if request.method == 'GET':
            return render_template('New2D.html', form=form)

        if request.method == 'POST':
            if not form.validate():
                return render_template('New2D.html', form=form)
            else:
                res = User().del_medicine_for_weakness(request.form['data_field'])
                if res:
                    return render_template('index.html', login=session.get('login'))
                else:
                    return render_template('New2D.html', form=form)


@app.route('/user_acc', methods=['GET', 'POST'])
@register_menu(app, '.user_acc', 'Your account', order=7)
def u_acc():
    if not is_login():
        return redirect('/login')
    else:
        log = session.get('login')
        name = User().get_user(log)[0][2]
        date = User().get_user(log)[0][3]
        form2 = Cr2D()
        form1 = Cr1D(data_field = name)
        formd = DateB(data_field = date)


        return render_template('user_acc.html', login = log, form1=form1, form2 = form2, formd = formd)

@app.route('/upd_user_pass', methods=['GET', 'POST'])
def upd_pass():
    if not is_login():
        return redirect('/login')
    else:
        log = session.get('login')
        form = Cr2D()
        if request.method == 'GET':
            return redirect('/user_acc')
        if request.method == 'POST':
            if not form.validate():
                return redirect('/user_acc')
            else:
                res = User().upd_user_pass(log, request.form['data1_field'], request.form['data2_field'])
                if res:
                    return render_template('index.html', login=session.get('login'))
                else:
                    return redirect('/user_acc')




@app.route('/upd_user_birth', methods=['GET', 'POST'])
def upd_birth():
    if not is_login():
        return redirect('/login')
    else:
        log = session.get('login')
        form = DateB()
        if request.method == 'GET':
            return redirect('/user_acc')
        if request.method == 'POST':
                print(request.form['data_field'])
                res = User().upd_user_birth(log,  datetime.strptime(request.form['data_field'], '%Y-%m-%d'))
                if res:
                    return render_template('index.html')
                else:
                    return redirect('/user_acc')

@app.route('/upd_user_name', methods=['GET', 'POST'])
def upd_name():
    if not is_login():
        return redirect('/login')
    else:
        log = session.get('login')
        form = Cr1D()
        if request.method == 'GET':
            return redirect('/user_acc')
        if request.method == 'POST':
            if not form.validate():
                return redirect('/user_acc')
            else:
                res = User().upd_user_name(log, request.form['data_field'])
                if res:
                    return render_template('index.html')
                else:
                    return redirect('/user_acc')


@app.route('/user_history', methods = ['GET', 'POST'])
@register_menu(app, '.user_history', 'History_of_healing', order=1)
def u_history():
    if not is_login():
        return redirect('/login')
    else:
        form = HistoryForm()
        log = session.get('login')
        data = User().user_history(session.get('login'))

        if request.method =='GET':
            form = HistoryForm()
            return render_template('history.html', data = data, form = form)
        if request.method =='POST':
            if not form.validate():
                return redirect('/user_history')
            else:
                form = HistoryForm()
                res = User().new_healing_record(log, request.form['weakness_field'], request.form['medicine_field'], request.form['syndrom_field'], datetime.strptime(request.form['date_diagnosis'], '%Y-%m-%d'), datetime.strptime(request.form['date_begin'], '%Y-%m-%d'), datetime.strptime(request.form['date_end'], '%Y-%m-%d'))
                if res:
                    return render_template('history.html', data = data, form = form)
                else:
                    print('whaat')
                    return render_template('history.html', data = data, form = form)


@app.route('/del_user_history', methods = ['GET', 'POST'])
def del_history():
    if not is_login():
        return redirect('/login')
    else:
        form = HistoryForm()
        log = session.get('login')
        data = User().user_history(session.get('login'))

        if request.method =='GET':
            return render_template('history.html', data = data, form = form)
        if request.method =='POST':
            if not form.validate():
                return redirect('/user_history')
            else:
                res = User().del_healing_record(log, request.form['weakness_field'], request.form['medicine_field'], request.form['syndrom_field'], datetime.strptime(request.form['date_diagnosis'], '%Y-%m-%d'), datetime.strptime(request.form['date_begin'], '%Y-%m-%d'), datetime.strptime(request.form['date_end'], '%Y-%m-%d'))
                if res:
                    return render_template('history.html', data = data, form = form)
                else:
                    return render_template('history.html', data = data, form = form)




@app.route('/piechart', methods = ['GET', 'POST'])
@register_menu(app, '.piechart', 'Make prediction for you', order=6)
def vizualization():
    if not is_login():
        return redirect('/login')
    else:
        form = Cr1D()
        if request.method == 'GET':
            return render_template('vizualization.html', form=form)

        if request.method == 'POST':
            if not form.validate():
                return render_template('vizualization.html', form=form)
            else:
                res = User().stat_weaks_for_syndrom(request.form['data_field'])
                if res:
                    values = [v for k, v in res]
                    keys = [k for k, v in res]
                    name_of_max = keys[0]
                    return plot_png(values, keys, name_of_max)
                else:
                    return render_template('vizualization.html', form=form)


@app.route('/trends', methods = ['GET', 'POST'])
@register_menu(app, '.trends', 'Trends for weaknesses', order=7)
def trends():
    if not is_login():
        return redirect('/login')
    else:
        form = Cr1D()
        if request.method == 'GET':
            return render_template('trends.html', form=form)
        if request.method == 'POST':
            if not form.validate():
                return render_template('trends.html', form=form)
            else:
                #try:
                    res = User().stat_weak_by_date(request.form['data_field'])
                    if res:
                        values = [v for k, v in res if k is not None]
                        keys = [k for k, v in res if k is not None]
                        return plot_png_weaks(dates.date2num(keys), values, request.form['data_field'])
                    else:
                        return render_template('trends.html', form=form)
                #except Exception:
                #    return(render_template('trends.html', form=form))



def plot_png(xs, ys, name):
    fig = create_figure(xs, ys, name)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

def create_figure(xs, ys, name):
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    med = User().max_medicine_for_weakness(name)[0][0]
    fig.suptitle('Your diagnosis is   '+name+'    and your recommendation is to use   '+ med, fontsize = 10)
    axis.pie(xs, labels = ys)
    return fig

def plot_png_weaks(xs, ys, name):
    fig = create_figure_trends(xs, ys, name)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


def create_figure_trends(xs, ys, name):
    fig = Figure(figsize =[40, 10])
    axis = fig.add_subplot(1, 1, 1)
    fig.suptitle('Trend of beggining to be sick of '+name, fontsize = 10)
    axis.plot_date(xs, ys, 'r+')
    return fig


@app.route('/upd_mws')
@register_menu(app, '.upd_mws', 'Update names of medicines, weaknesses and syndromes', order = 8)
def upd_mws():
    if not is_login():
        return redirect('/login')
    else:
        form = upd_test()
        return render_template('update_mws.html',form=form)


@app.route('/upd_m', methods=['GET', 'POST'])
def upd_m():
    if not is_login():
        return redirect('/login')
    else:
        form = upd_test()
        if request.method == 'GET':
            return redirect('/upd_mws')
        if request.method == 'POST':
            if not form.validate():
                return redirect('/upd_mws')
            else:
                res = User().upd_med(request.form['data_old_field'], request.form['data_new_field'])
                if res:
                    return render_template('index.html')
                else:
                    return redirect('/upd_mws')


@app.route('/upd_w', methods=['GET', 'POST'])
def upd_w():
    if not is_login():
        return redirect('/login')
    else:
        form = upd_test()
        if request.method == 'GET':
            return redirect('/upd_mws')
        if request.method == 'POST':
            if not form.validate():
                return redirect('/upd_mws')
            else:
                res = User().upd_weak(request.form['data_old_field'], request.form['data_new_field'])
                if res:
                    return render_template('index.html')
                else:
                    return redirect('/upd_mws')


@app.route('/upd_s', methods=['GET', 'POST'])
def upd_s():
    if not is_login():
        return redirect('/login')
    else:
        form = upd_test()
        if request.method == 'GET':
            return redirect('/upd_mws')
        if request.method == 'POST':
            if not form.validate():
                return redirect('/upd_mws')
            else:
                res = User().upd_synd(request.form['data_old_field'], request.form['data_new_field'])
                if res:
                    return render_template('index.html')
                else:
                    return redirect('/upd_mws')



@app.route('/upd_diag_test', methods =['GET', 'POST'])
def updg():
    form = upd_test()
    if request.method == 'GET':
        return render_template('upd_diag_test.html', form=form)

    if request.method == 'POST':
        if not form.validate():
            return render_template('upd_diag_test.html', form=form)
        else:
            res = User().upd_diag(request.form['data_old_field'], request.form['data_new_field'])
            return render_template('upd_diag_test.html', form=form)

app.run(debug=True)



