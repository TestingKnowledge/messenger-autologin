from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Professional Dashboard</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-gray-50 font-sans antialiased">
        <div class="min-h-screen flex flex-col">
            <!-- Navigation -->
            <nav class="bg-white border-b border-gray-200 px-6 py-4 flex justify-between items-center shadow-sm">
                <h1 class="text-xl font-bold text-gray-800">Enterprise Portal</h1>
                <span class="text-sm text-green-600 bg-green-50 px-3 py-1 rounded-full font-medium">● System Online</span>
            </nav>

            <!-- Main Content Area -->
            <main class="flex-grow max-w-5xl w-full mx-auto p-6 md:p-10">
                <div class="bg-white rounded-2xl shadow-sm border border-gray-200 p-8">
                    <h2 class="text-2xl font-bold text-gray-900 mb-2">Welcome Back</h2>
                    <p class="text-gray-600 mb-6">Manage your services, track deployments, and interact with live modules below.</p>
                    
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
                        <div class="bg-blue-50 border border-blue-100 rounded-xl p-5">
                            <h3 class="text-blue-900 font-semibold text-sm">Active Sessions</h3>
                            <p class="text-2xl font-bold text-blue-600 mt-1">1,248</p>
                        </div>
                        <div class="bg-green-50 border border-green-100 rounded-xl p-5">
                            <h3 class="text-green-900 font-semibold text-sm">Server Uptime</h3>
                            <p class="text-2xl font-bold text-green-600 mt-1">99.98%</p>
                        </div>
                        <div class="bg-purple-50 border border-purple-100 rounded-xl p-5">
                            <h3 class="text-purple-900 font-semibold text-sm">Response Time</h3>
                            <p class="text-2xl font-bold text-purple-600 mt-1">24ms</p>
                        </div>
                    </div>

                    <!-- Interactive Control Panel -->
                    <div class="border-t border-gray-100 pt-6">
                        <h3 class="text-lg font-semibold text-gray-800 mb-4">Interactive Command Terminal</h3>
                        <div class="space-y-4">
                            <textarea rows="3" class="w-full border border-gray-300 rounded-lg p-3 text-sm focus:ring-2 focus:ring-blue-500 focus:outline-none" placeholder="Enter system instruction or script payload..."></textarea>
                            <button onclick="alert('Command executed successfully!')" class="bg-blue-600 text-white font-medium px-5 py-2.5 rounded-lg text-sm hover:bg-blue-700 transition shadow-sm">Execute Action</button>
                        </div>
                    </div>
                </div>
            </main>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run()
