from app import app, db
from app.controller import user_controller, login_controller
from flask import json, request, jsonify, redirect, url_for
from flask_login import login_user
from app.model.user import User


# Buat instance dari UserController
usercontroller = user_controller.UserController()
# logincontroller = login_controller.validate_login()


@app.route('/')
def index():
    return "hello flask"

@app.route('/login')
def login():
    return "Login Page"

# Route untuk membuat user baru
@app.route('/Crusers', methods=['POST'])
def create_user():
    """Create a new user."""

    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not (username and email and password):
        return jsonify({'error': 'Bad request'}), 400

    user = usercontroller.create_user(username, email, password)

    return jsonify({'user': user.to_dict()}), 201

# Route untuk mendapatkan user oleh ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_users(user_id):
    """
    Mendapatkan user berdasarkan ID.

    Request ini akan mengembalikan data user berdasarkan ID yang dikirimkan.
    Jika user tidak ditemukan, maka akan mengembalikan error 404.
    """
    try:
        # Mendapatkan user dari database berdasarkan ID
        user = usercontroller.get_user(user_id)

        # Jika user ditemukan, maka mengembalikan data user
        if user:
            return jsonify({'user': user.to_dict()}), 200
        else:
            # Jika user tidak ditemukan, maka mengembalikan error 404
            return jsonify({'error': 'User tidak ditemukan'}), 404
    except Exception as e:
        # Menangani exception yang tidak terduga
        return jsonify({'error': 'Terjadi kesalahan pada server'}), 500


# Route untuk mengupdate user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    username = data['username']
    email = data['email']
    password = data['password']
    user = user_controller.update_user(user_id, username, email, password)
    if user:
        return jsonify({'user': user.to_dict()}), 200
    else:
        return jsonify({'error': 'User tidak ditemukan'}), 404

# Route untuk menghapus user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_controller.delete_user(user_id):
        return jsonify({'message': 'User berhasil dihapus'}), 200
    else:
        return jsonify({'error': 'User tidak ditemukan'}), 404
    
@app.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if not email or not password:
        return jsonify({'error': 'Email atau password tidak boleh kosong'}), 400

    if user is None or not user.check_password(password):
        return jsonify({'error': 'Email atau password salah'}), 401
    # If the user is not active, return a 401 error
    if not user.is_active:
        return jsonify({'error': 'Akun anda belum aktif'}), 401


    try:
        login_user(user)
    except Exception as e:
        return jsonify({'error': 'Terjadi kesalahan saat login'}), 500

    return redirect(url_for('main.dash'))




if __name__ == '__main__':
    app.run(debug=True)