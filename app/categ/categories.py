import os
import uuid
from flask import Blueprint, render_template
from flask_login import login_required
from app.models import Categories


categ_bp = Blueprint('categ', __name__, template_folder='templates', static_folder='static')

# Маршрут для отображения категорий
@categ_bp.route('/category', methods=['GET', 'POST'])
@login_required
def new_categ():
    categories = Categories.query.all()  # Получаем список категорий из базы данных
    return render_template('categ.categories_page.html', categories=categories)