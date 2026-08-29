import secrets
import sqlite3
from flask import Flask, request, make_response, render_template_string

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE,
            auth_token TEXT
        )
    ''')
    cursor.execute("INSERT OR IGNORE INTO users (email) VALUES ('friend@example.com')")
    conn.commit()
    conn.close()

init_db()

# Route to generate a test link
@app.route('/generate-link', methods=['GET'])
def generate_link():
    email = request.args.get('email', 'friend@example.com')
    token = secrets.token_urlsafe(16)

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET auth_token = ? WHERE email = ?", (token, email))
    conn.commit()
    conn.close()

    link = f"https://messenger-autologin.onrender.com/autologin?token={token}"
    return f'<h1>Link for {email}:</h1><p><a href="{link}">{link}</a></p>'

# Auto-login route that sets cookie and directs to the dashboard
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

        # Set session cookie and redirect to the dashboard route
        response = make_response('', 302)
        response.set_cookie('session_user_id', str(user_id), httponly=True, secure=True)
        response.headers['Location'] = '/dashboard'
        return response

    conn.close()
    return 'Invalid or expired login link.', 401

# The Dashboard where the logged-in user can control chats or send messages
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    user_id = request.cookies.get('session_user_id')
    if not user_id:
        return 'Unauthorized. Please use your login link first.', 401

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT email FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()

    email = user[0] if user else 'Unknown'

    # Handle when they submit a chat message from the dashboard
    message_status = ""
    if request.method == 'POST':
        chat_message = request.form.get('message')
        # Here is where you would hook up Facebook's Messenger API to send the message
        message_status = f"Successfully sent chat message: '{chat_message}'"

    # HTML dashboard interface with a chat box
    dashboard_html = f"""
    <!DOCTYPE html>
    <html>
    <head><title>User Dashboard</title></head>
    <body style="font-family: Arial; padding: 20px;">
        <h2>Welcome to your Dashboard, {email}</h2>
        <p>You are successfully logged in via your auto-login link.</p>
        
        <hr style="margin: 20px 0;">
        
        <h3>Send a Chat / Control Message</h3>
        <form method="POST">
            <textarea name="message" rows="4" cols="50" placeholder="Type your message or auto-chat command here..."></textarea><br><br>
            <button type="submit" style="padding: 10px 20px;">Send Message</button>
        </form>
        
        <p style="color: green; font-weight: bold;">{message_status}</p>
    </body>
    </html>
    """
    return render_template_string(dashboard_html)

if __name__ == '__main__':
    app.run()
