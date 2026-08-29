from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def shop():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Apex Store | Premium Digital Assets</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-slate-50 font-sans antialiased text-slate-900">
        <!-- Navigation -->
        <nav class="bg-white border-b border-slate-200 sticky top-0 z-50">
            <div class="max-w-7xl mx-auto px-6 h-16 flex justify-between items-center">
                <span class="text-xl font-extrabold tracking-tight text-indigo-600">APEX<span class="text-slate-900">STORE</span></span>
                <div class="flex items-center space-x-6">
                    <a href="#" class="text-sm font-medium text-slate-600 hover:text-indigo-600">Catalog</a>
                    <a href="#" class="text-sm font-medium text-slate-600 hover:text-indigo-600">Features</a>
                    <button onclick="alert('Cart is empty')" class="bg-indigo-600 text-white px-4 py-2 rounded-lg text-sm font-medium hover:bg-indigo-700 transition shadow-sm">Cart (0)</button>
                </div>
            </div>
        </nav>

        <!-- Hero Section -->
        <section class="bg-gradient-to-b from-white to-slate-100 py-16 px-6 text-center border-b border-slate-200">
            <div class="max-w-3xl mx-auto">
                <span class="bg-indigo-50 text-indigo-600 text-xs font-semibold px-3 py-1 rounded-full uppercase tracking-wider">New Release</span>
                <h1 class="text-4xl md:text-5xl font-black text-slate-900 mt-4 tracking-tight">Scale Your Digital Workflow Instantly</h1>
                <p class="text-lg text-slate-600 mt-4">Professional-grade toolkits, assets, and applications built for modern creators and developers.</p>
                <div class="mt-8 flex justify-center gap-4">
                    <a href="#products" class="bg-indigo-600 text-white font-medium px-6 py-3 rounded-xl text-sm hover:bg-indigo-700 transition shadow-md">Browse Products</a>
                    <a href="#" class="bg-white border border-slate-300 text-slate-700 font-medium px-6 py-3 rounded-xl text-sm hover:bg-slate-50 transition">Learn More</a>
                </div>
            </div>
        </section>

        <!-- Product Catalog Grid -->
        <main id="products" class="max-w-7xl mx-auto px-6 py-16">
            <div class="flex justify-between items-center mb-8">
                <h2 class="text-2xl font-bold tracking-tight">Featured Products</h2>
                <span class="text-sm text-slate-500">Showing 4 items</span>
            </div>
            
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
                <!-- Product Card 1 -->
                <div class="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-sm hover:shadow-md transition group">
                    <div class="h-48 bg-indigo-50 flex items-center justify-center text-indigo-500 font-bold text-lg group-hover:bg-indigo-100 transition">Toolkit Pro</div>
                    <div class="p-5">
                        <span class="text-xs font-semibold text-indigo-600 uppercase">Software</span>
                        <h3 class="font-bold text-lg mt-1 text-slate-900">Automation Suite</h3>
                        <p class="text-sm text-slate-500 mt-1">Streamline tasks with advanced scripts.</p>
                        <div class="mt-5 flex items-center justify-between">
                            <span class="text-lg font-bold text-slate-900">$49.00</span>
                            <button onclick="alert('Toolkit Pro added to cart!')" class="bg-slate-900 text-white text-xs font-medium px-3.5 py-2 rounded-lg hover:bg-indigo-600 transition">Add to Cart</button>
                        </div>
                    </div>
                </div>

                <!-- Product Card 2 -->
                <div class="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-sm hover:shadow-md transition group">
                    <div class="h-48 bg-emerald-50 flex items-center justify-center text-emerald-600 font-bold text-lg group-hover:bg-emerald-100 transition">UI Kit</div>
                    <div class="p-5">
                        <span class="text-xs font-semibold text-emerald-600 uppercase">Design</span>
                        <h3 class="font-bold text-lg mt-1 text-slate-900">SaaS Tailwind UI</h3>
                        <p class="text-sm text-slate-500 mt-1">High-converting dashboard components.</p>
                        <div class="mt-5 flex items-center justify-between">
                            <span class="text-lg font-bold text-slate-900">$79.00</span>
                            <button onclick="alert('SaaS Tailwind UI added to cart!')" class="bg-slate-900 text-white text-xs font-medium px-3.5 py-2 rounded-lg hover:bg-emerald-600 transition">Add to Cart</button>
                        </div>
                    </div>
                </div>

                <!-- Product Card 3 -->
                <div class="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-sm hover:shadow-md transition group">
                    <div class="h-48 bg-amber-50 flex items-center justify-center text-amber-600 font-bold text-lg group-hover:bg-amber-100 transition">Analytics</div>
                    <div class="p-5">
                        <span class="text-xs font-semibold text-amber-600 uppercase">Data</span>
                        <h3 class="font-bold text-lg mt-1 text-slate-900">Traffic Tracker</h3>
                        <p class="text-sm text-slate-500 mt-1">Real-time visitor intelligence system.</p>
                        <div class="mt-5 flex items-center justify-between">
                            <span class="text-lg font-bold text-slate-900">$29.00</span>
                            <button onclick="alert('Traffic Tracker added to cart!')" class="bg-slate-900 text-white text-xs font-medium px-3.5 py-2 rounded-lg hover:bg-amber-600 transition">Add to Cart</button>
                        </div>
                    </div>
                </div>

                <!-- Product Card 4 -->
                <div class="bg-white rounded-2xl border border-slate-200 overflow-hidden shadow-sm hover:shadow-md transition group">
                    <div class="h-48 bg-purple-50 flex items-center justify-center text-purple-600 font-bold text-lg group-hover:bg-purple-100 transition">API Engine</div>
                    <div class="p-5">
                        <span class="text-xs font-semibold text-purple-600 uppercase">Backend</span>
                        <h3 class="font-bold text-lg mt-1 text-slate-900">Secure Auth Microservice</h3>
                        <p class="text-sm text-slate-500 mt-1">Plug-and-play authentication pipeline.</p>
                        <div class="mt-5 flex items-center justify-between">
                            <span class="text-lg font-bold text-slate-900">$99.00</span>
                            <button onclick="alert('Secure Auth Microservice added to cart!')" class="bg-slate-900 text-white text-xs font-medium px-3.5 py-2 rounded-lg hover:bg-purple-600 transition">Add to Cart</button>
                        </div>
                    </div>
                </div>
            </div>
        </main>

        <!-- Footer -->
        <footer class="bg-white border-t border-slate-200 py-8 text-center text-sm text-slate-500">
            <p>&copy; 2026 Apex Store. All rights reserved. Deployed on Render.</p>
        </footer>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run()
