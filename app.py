import os
from flask import Flask, render_template_string, request

app = Flask(__name__)

KEYS_FILE = 'keys.txt'

def get_next_key():
    if not os.path.exists(KEYS_FILE):
        return None
    
    with open(KEYS_FILE, 'r') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    
    if not lines:
        return None
    
    # Take the first key
    assigned_key = lines[0]
    
    # Save remaining keys back to the file
    with open(KEYS_FILE, 'w') as f:
        f.write('\n'.join(lines[1:]) + '\n')
        
    return assigned_key

@app.route('/', methods=['GET', 'POST'])
def store():
    status_message = ""
    assigned_key = ""
    
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'purchase':
            key = get_next_key()
            if key:
                assigned_key = key
                status_message = "Success! Your license key has been generated."
            else:
                status_message = "Error: All keys are currently out of stock."

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ApexHub Instant Key Delivery</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    </head>
    <body class="bg-slate-900 text-slate-100 font-sans antialiased">
        <div class="max-w-3xl mx-auto px-6 py-16">
            <div class="bg-slate-800 border border-slate-700 rounded-2xl p-8 shadow-xl text-center">
                <h1 class="text-3xl font-black text-white">Instant Key Dispatch System</h1>
                <p class="text-slate-400 mt-2 text-sm">Click below to simulate a purchase and claim an automated license key from your GitHub store inventory.</p>
                
                <form method="POST" class="mt-8">
                    <input type="hidden" name="action" value="purchase">
                    <button type="submit" class="bg-indigo-600 hover:bg-indigo-500 text-white font-semibold px-8 py-3.5 rounded-xl text-sm transition shadow-lg shadow-indigo-600/30">
                        <i class="fa-solid fa-key mr-2"></i> Claim License Key
                    </button>
                </form>

                {f'''
                <div class="mt-8 p-6 bg-slate-900 border border-slate-700 rounded-xl text-left">
                    <p class="text-xs font-semibold text-emerald-400 uppercase tracking-wider">{status_message}</p>
                    <div class="mt-2 flex items-center justify-between bg-slate-950 p-4 rounded-lg border border-slate-800">
                        <code class="text-indigo-400 font-mono text-lg font-bold">{assigned_key}</code>
                        <span class="text-xs text-slate-500">One-time use</span>
                    </div>
                </div>
                ''' if assigned_key else f'''
                <div class="mt-6 text-sm text-amber-400 font-medium">
                    {status_message}
                </div>
                ''' if status_message else ""}
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run()
