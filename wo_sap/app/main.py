from app import app
from flask_login import login_required

@app.route('/dashboard')
@login_required
def dash():
    return "selamat datang"