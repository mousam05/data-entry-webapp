from flask import request, render_template, Blueprint, redirect, url_for
from src.Login.Application.User import User
from src.Login.Domain.Login_form import Login_form

login_blueprint = Blueprint('login', __name__)


@login_blueprint.route('/', methods=['GET', 'POST'])
def login():
    form = Login_form(request.form)
    if request.method == 'POST' and form.validate():
        try:
            user_instance = User()
            user_instance.create_user(form)
            #return redirect('/')
        except Exception as e:
            print(f"Error creating user: {str(e)}")
    return render_template('login.html', form=form)
