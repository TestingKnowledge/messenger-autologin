import sqlite3
from flask import Flask, request, make_response

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT,
            auth_token TEXT
        )
    ''')
    cursor.execute("SELECT * FROM users WHERE email='friend@example.com'")
    if not cursor.fetchone():
        cursor.execute("INSERT INTO users (email, auth_token) VALUES ('friend@example.com', 'unique_token_xyz789')")
    conn.commit()
    conn.close()

init_db()

@app.route('/autologin', methods=['GET'])
def autologin():
    incoming_token = request.args.get('token')
    user_agent = request.headers.get('User-Agent', '')

    if 'facebookexternalhit' in user_agent or 'Facebot' in user_agent:
        return '<html><head><title>Dashboard Login</title></head><body>Loading...</body></html>'

    if not incoming_token:
        return 'Missing token.', 400

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, email FROM users WHERE auth_token = ?", (incoming_token,))
    user = cursor.fetchone()

    if user:
        user_id, email = user
        cursor.execute("UPDATE users SET auth_token = NULL WHERE id = ?", (user_id,))
        conn.commit()
        conn.close()

        response = make_response(f'<h1>Success! You are logged in as {email}.</h1>')
        response.set_cookie('session_user_id', str(user_id), httponly=True, secure=True)
        return response

    conn.close()
    return 'Invalid or expired login link.', 401

if __name__ == '__main__':
    app.run()
