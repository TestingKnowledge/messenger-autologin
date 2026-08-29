from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def shop_extended():
    html_content = """
    <!DOCTYPE html>
    <html lang="en" class="scroll-smooth">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ApexHub | Professional Creator Ecosystem</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    </head>
    <body class="bg-slate-900 text-slate-100 font-sans antialiased selection:bg-indigo-500 selection:text-white">
        
        <!-- Top Announcement Bar -->
        <div class="bg-gradient-to-r from-indigo-600 to-violet-600 text-xs font-semibold py-2 px-4 text-center text-white tracking-wide">
            🚀 Season Launch Sale: Use code <span class="underline font-bold">APEX2026</span> for 25% off all master packages!
        </div>

        <!-- Navigation Header -->
        <nav class="bg-slate-900/80 backdrop-blur-md border-b border-slate-800 sticky top-0 z-50">
            <div class="max-w-7xl mx-auto px-6 h-20 flex justify-between items-center">
                <div class="flex items-center space-x-3">
                    <div class="h-10 w-10 rounded-xl bg-indigo-600 flex items-center justify-center font-black text-xl text-white shadow-lg shadow-indigo-500/30">A</div>
                    <span class="text-xl font-black tracking-tight text-white">APEX<span class="text-indigo-500">HUB</span></span>
                </div>
                
                <div class="hidden md:flex items-center space-x-8 text-sm font-medium text-slate-300">
                    <a href="#catalog" class="hover:text-indigo-400 transition">Catalog</a>
                    <a href="#features" class="hover:text-indigo-400 transition">Ecosystem</a>
                    <a href="#testimonials" class="hover:text-indigo-400 transition">Community</a>
                    <a href="#contact" class="hover:text-indigo-400 transition">Support</a>
                </div>

                <div class="flex items-center space-x-4">
                    <div class="hidden sm:flex items-center space-x-3 text-slate-400 text-lg">
                        <a href="https://twitter.com" target="_blank" class="hover:text-indigo-400 transition"><i class="fa-brands fa-x-twitter"></i></a>
                        <a href="https://instagram.com" target="_blank" class="hover:text-pink-400 transition"><i class="fa-brands fa-instagram"></i></a>
                        <a href="https://discord.com" target="_blank" class="hover:text-indigo-500 transition"><i class="fa-brands fa-discord"></i></a>
                        <a href="https://github.com" target="_blank" class="hover:text-white transition"><i class="fa-brands fa-github"></i></a>
                    </div>
                    <button onclick="alert('Cart is currently empty.')" class="bg-indigo-600 hover:bg-indigo-500 text-white px-5 py-2.5 rounded-xl text-sm font-semibold transition shadow-md shadow-indigo-600/20 flex items-center gap-2">
                        <i class="fa-solid fa-cart-shopping"></i> Cart (0)
                    </button>
                </div>
            </div>
        </nav>

        <!-- Hero Section -->
        <header class="relative overflow-hidden py-24 px-6 border-b border-slate-800 bg-gradient-to-b from-slate-900 via-slate-950 to-slate-900">
            <div class="max-w-4xl mx-auto text-center relative z-10">
                <span class="inline-flex items-center gap-1.5 bg-indigo-500/10 border border-indigo-500/20 text-indigo-400 text-xs font-semibold px-3.5 py-1 rounded-full uppercase tracking-wider mb-6">
                    <i class="fa-solid fa-bolt text-indigo-400"></i> Next-Gen Developer Tooling
                </span>
                <h1 class="text-4xl md:text-7xl font-black text-white tracking-tight leading-none">
                    Engineered for <span class="bg-gradient-to-r from-indigo-400 via-purple-400 to-pink-400 bg-clip-text text-transparent">Maximum Scale</span>
                </h1>
                <p class="text-lg md:text-xl text-slate-400 mt-6 max-w-2xl mx-auto leading-relaxed">
                    Deploy production-ready architectures, secure microservices, and design systems built to elevate your tech stack instantly.
                </p>
                <div class="mt-10 flex flex-col sm:flex-row justify-center gap-4">
                    <a href="#catalog" class="bg-indigo-600 hover:bg-indigo-500 text-white font-semibold px-8 py-4 rounded-xl text-sm transition shadow-lg shadow-indigo-600/30 flex items-center justify-center gap-2">
                        Explore Marketplace <i class="fa-solid fa-arrow-right"></i>
                    </a>
                    <a href="#features" class="bg-slate-800 hover:bg-slate-700 text-slate-300 font-semibold px-8 py-4 rounded-xl text-sm transition border border-slate-700 flex items-center justify-center">
                        View Documentation
                    </a>
                </div>
            </div>
        </header>

        <!-- Catalog Section -->
        <main id="catalog" class="max-w-7xl mx-auto px-6 py-24">
            <div class="flex flex-col md:flex-row justify-between items-start md:items-end mb-12">
                <div>
                    <h2 class="text-3xl font-black tracking-tight text-white">Featured Digital Assets</h2>
                    <p class="text-slate-400 mt-1">Handcrafted templates and secure automation modules.</p>
                </div>
                <div class="mt-4 md:mt-0 flex gap-2">
                    <button class="bg-indigo-600 text-white px-4 py-2 rounded-lg text-xs font-semibold">All Products</button>
                    <button class="bg-slate-800 hover:bg-slate-700 text-slate-300 px-4 py-2 rounded-lg text-xs font-semibold transition">Software</button>
                    <button class="bg-slate-800 hover:bg-slate-700 text-slate-300 px-4 py-2 rounded-lg text-xs font-semibold transition">UI Kits</button>
                </div>
            </div>
            
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
                
                <!-- Product 1 -->
                <div class="bg-slate-800/50 rounded-2xl border border-slate-700/60 overflow-hidden hover:border-indigo-500/50 transition group flex flex-col justify-between shadow-xl">
                    <div>
                        <div class="h-52 bg-gradient-to-br from-indigo-900 to-slate-900 relative flex items-center justify-center overflow-hidden">
                            <div class="absolute inset-0 bg-[radial-gradient(#4f46e5_1px,transparent_1px)] [background-size:16px_16px] opacity-20"></div>
                            <i class="fa-solid fa-terminal text-5xl text-indigo-400 group-hover:scale-110 transition duration-300"></i>
                            <span class="absolute top-4 right-4 bg-indigo-500/20 border border-indigo-500/30 text-indigo-300 text-xs font-bold px-2.5 py-1 rounded-lg">Bestseller</span>
                        </div>
                        <div class="p-6">
                            <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider">Automation Engine</span>
                            <h3 class="font-bold text-xl mt-1 text-white">Nexus CLI Core</h3>
                            <p class="text-sm text-slate-400 mt-2 leading-relaxed">Advanced command-line execution pipeline with built-in telemetry and zero-config deployment options.</p>
                        </div>
                    </div>
                    <div class="p-6 pt-0 flex items-center justify-between border-t border-slate-700/40 mt-6 pt-4">
                        <div>
                            <span class="text-xs text-slate-500 block">Regular Price</span>
                            <span class="text-xl font-black text-white">$49.00</span>
                        </div>
                        <button onclick="alert('Nexus CLI Core added to cart!')" class="bg-indigo-600 hover:bg-indigo-500 text-white font-semibold px-4 py-2.5 rounded-xl text-xs transition shadow-md shadow-indigo-600/20">
                            Add to Cart
                        </button>
                    </div>
                </div>

                <!-- Product 2 -->
                <div class="bg-slate-800/50 rounded-2xl border border-slate-700/60 overflow-hidden hover:border-emerald-500/50 transition group flex flex-col justify-between shadow-xl">
                    <div>
                        <div class="h-52 bg-gradient-to-br from-emerald-950 to-slate-900 relative flex items-center justify-center overflow-hidden">
                            <div class="absolute inset-0 bg-[radial-gradient(#10b981_1px,transparent_1px)] [background-size:16px_16px] opacity-20"></div>
                            <i class="fa-solid fa-layer-group text-5xl text-emerald-400 group-hover:scale-110 transition duration-300"></i>
                            <span class="absolute top-4 right-4 bg-emerald-500/20 border border-emerald-500/30 text-emerald-300 text-xs font-bold px-2.5 py-1 rounded-lg">Popular</span>
                        </div>
                        <div class="p-6">
                            <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider">Design System</span>
                            <h3 class="font-bold text-xl mt-1 text-white">SaaS UI Master</h3>
                            <p class="text-sm text-slate-400 mt-2 leading-relaxed">Over 120+ responsive Tailwind components equipped with light/dark modes and accessible state toggles.</p>
                        </div>
                    </div>
                    <div class="p-6 pt-0 flex items-center justify-between border-t border-slate-700/40 mt-6 pt-4">
                        <div>
                            <span class="text-xs text-slate-500 block">Regular Price</span>
                            <span class="text-xl font-black text-white">$79.00</span>
                        </div>
                        <button onclick="alert('SaaS UI Master added to cart!')" class="bg-emerald-600 hover:bg-emerald-500 text-white font-semibold px-4 py-2.5 rounded-xl text-xs transition shadow-md shadow-emerald-600/20">
                            Add to Cart
                        </button>
                    </div>
                </div>

                <!-- Product 3 -->
                <div class="bg-slate-800/50 rounded-2xl border border-slate-700/60 overflow-hidden hover:border-amber-500/50 transition group flex flex-col justify-between shadow-xl">
                    <div>
                        <div class="h-52 bg-gradient-to-br from-amber-950 to-slate-900 relative flex items-center justify-center overflow-hidden">
                            <div class="absolute inset-0 bg-[radial-gradient(#f59e0b_1px,transparent_1px)] [background-size:16px_16px] opacity-20"></div>
                            <i class="fa-solid fa-shield-halved text-5xl text-amber-400 group-hover:scale-110 transition duration-300"></i>
                            <span class="absolute top-4 right-4 bg-amber-500/20 border border-amber-500/30 text-amber-300 text-xs font-bold px-2.5 py-1 rounded-lg">Secure</span>
                        </div>
                        <div class="p-6">
                            <span class="text-xs font-bold text-amber-400 uppercase tracking-wider">Microservice</span>
                            <h3 class="font-bold text-xl mt-1 text-white">Auth Vault API</h3>
                            <p class="text-sm text-slate-400 mt-2 leading-relaxed">Enterprise-grade authentication pipe supporting token rotation, session tracking, and rate limiting.</p>
                        </div>
                    </div>
                    <div class="p-6 pt-0 flex items-center justify-between border-t border-slate-700/40 mt-6 pt-4">
                        <div>
                            <span class="text-xs text-slate-500 block">Regular Price</span>
                            <span class="text-xl font-black text-white">$99.00</span>
                        </div>
                        <button onclick="alert('Auth Vault API added to cart!')" class="bg-amber-600 hover:bg-amber-500 text-white font-semibold px-4 py-2.5 rounded-xl text-xs transition shadow-md shadow-amber-600/20">
                            Add to Cart
                        </button>
                    </div>
                </div>

            </div>
        </main>

        <!-- Newsletter / Footer Callout -->
        <section id="contact" class="border-t border-slate-800 bg-slate-950/60 py-20 px-6">
            <div class="max-w-3xl mx-auto text-center">
                <h3 class="text-2xl font-black text-white">Subscribe to the Developer Digest</h3>
                <p class="text-slate-400 mt-2 text-sm">Get exclusive assets, weekly patch updates, and early discounts delivered straight to your inbox.</p>
                <div class="mt-6 flex flex-col sm:flex-row gap-3 justify-center">
                    <input type="email" placeholder="Enter your email address..." class="bg-slate-900 border border-slate-700 px-4 py-3 rounded-xl text-sm text-white placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 sm:w-80">
                    <button onclick="alert('Successfully subscribed to newsletter!')" class="bg-indigo-600 hover:bg-indigo-500 text-white font-semibold px-6 py-3 rounded-xl text-sm transition">Join Community</button>
                </div>
            </div>
        </section>

        <!-- Footer -->
        <footer class="bg-slate-950 border-t border-slate-800/80 py-12 px-6 text-sm text-slate-500">
            <div class="max-w-7xl mx-auto flex flex-col md:flex-row justify-between items-center gap-6">
                <div class="flex items-center space-x-2">
                    <span class="font-bold text-white">ApexHub Ecosystem</span>
                    <span>&copy; 2026. All rights reserved.</span>
                </div>
                <div class="flex space-x-6 text-lg">
                    <a href="https://twitter.com" target="_blank" class="hover:text-indigo-400 transition"><i class="fa-brands fa-x-twitter"></i></a>
                    <a href="https://instagram.com" target="_blank" class="hover:text-pink-400 transition"><i class="fa-brands fa-instagram"></i></a>
                    <a href="https://discord.com" target="_blank" class="hover:text-indigo-500 transition"><i class="fa-brands fa-discord"></i></a>
                    <a href="https://github.com" target="_blank" class="hover:text-white transition"><i class="fa-brands fa-github"></i></a>
                </div>
            </div>
        </footer>

    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run()
