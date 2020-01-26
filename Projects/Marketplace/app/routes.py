from app import app, db
from app import models,forms
import flask, flask_login
from flask import Flask, render_template, flash, redirect, url_for, request
from app.forms import SignupForm
from app.models import Customer, Item 
from flask_login import logout_user

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()  # Load signup the form

    if form.validate_on_submit():

        customer = Customer(customer_name=form.customer_name.data,customer_password=form.customer_password.data,status="active")

        db.session.add(customer)
        db.session.commit()

        flask_login.login_user(customer)

        return flask.redirect(url_for('homepage'))

    return flask.render_template('signup.html', title='Sign UP', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask_login.current_user.is_authenticated:
        return flask.redirect(url_for('homepage'))

    form = forms.LoginForm()  # Load the form

    if form.validate_on_submit():
        customer = models.Customer.query.filter_by(customer_name=form.customer_name.data).first()

        if customer is None or not customer.customer_password == form.customer_password.data:
            flask.flash('Invalid customer Name or password')
            return flask.redirect(url_for('login'))

        # Log the user in
        flask_login.login_user(customer, remember=form.remember_me.data)
        return flask.redirect(url_for('homepage'))

    return flask.render_template('login.html', title='Sign In', form=form)  # Render the form

@app.route('/logout')
@flask_login.login_required
def logout():
    logout_user()
    return redirect(url_for('homepage'))

@app.route('/')
def homepage():
    products = models.Item.query.all()
    return render_template('homepage.html', products=products)

@app.route('/add-to-cart/<int:item_id>')
@flask_login.login_required
def add_to_cart(item_id):
    item = Item.get_by_id(item_id)
    if not item:
        return flask.redirect(flask.url_for('homepage'))

    user = flask_login.current_user
    user.basket.append(item)

    db.session.commit()
    flask.flash("Added {} to the cart".format(item.item_name))
    return flask.redirect(flask.url_for('homepage'))

@app.route('/remove-from-cart/<int:item_id>')
@flask_login.login_required
def remove_from_cart(item_id):
    item = Item.get_by_id(item_id)
    if not item:
        return flask.redirect(flask.url_for('homepage'))

    user = flask_login.current_user
    user.basket.remove(item)

    db.session.commit()
    flask.flash("Removed {} from the cart".format(item.item_name))
    return flask.redirect(flask.url_for('user_cart'))

@app.route('/cart')
def user_cart():
    return flask.render_template('user_cart.jin')

# API funcs
@app.route('/api/add-to-cart/<int:item_id>')
@flask_login.login_required
def api_add_to_cart(item_id):
    item = Item.get_by_id(item_id)
    if not item:
        return flask.jsonify(False)

    user = flask_login.current_user
    user.basket.append(item)

    db.session.commit()
    return flask.jsonify(True)

