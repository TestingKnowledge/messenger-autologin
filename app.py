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
    
    assigned_key = lines[0]
    with open(KEYS_FILE, 'w') as f:
        f.write('\n'.join(lines[1:]) + '\n')
        
    return assigned_key

@app.route('/', methods=['GET', 'POST'])
def futuristic_store():
    status_message = ""
    assigned_key = ""
    
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'claim':
            key = get_next_key()
            if key:
                assigned_key = key
                status_message = "Neural link established. Key encrypted & delivered."
            else:
                status_message = "Warning: Node depletion. All secure keys claimed."

    html_content = f"""
    <!DOCTYPE html>
    <html lang="en" class="dark">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>NEXUS-X // Quantum Key Node</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
        <script>
            tailwind.config = {{
                darkMode: 'class',
                theme: {{
                    extend: {{
                        colors: {{
                            cyber: {{ 500: '#06b6d4', 600: '#0891b2', 950: '#030712' }}
                        }}
                    }}
                }}
            }}
        </script>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;500;700&family=JetBrains+Mono:wght@400;700&display=swap');
            body {{ font-family: 'Space Grotesk', sans-serif; }}
            .mono {{ font-family: 'JetBrains Mono', monospace; }}
            .glow {{ box-shadow: 0 0 25px rgba(6, 182, 212, 0.25); }}
            .glow-text {{ text-shadow: 0 0 15px rgba(6, 182, 212, 0.5); }}
            canvas {{ position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: 0; }}
        </style>
    </head>
    <body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col justify-between selection:bg-cyan-500 selection:text-black relative overflow-x-hidden">

        <!-- Live Particle Background Canvas -->
        <canvas id="particleCanvas"></canvas>

        <!-- Top Telemetry Status -->
        <header class="border-b border-cyan-500/20 bg-slate-950/80 backdrop-blur-md sticky top-0 z-50">
            <div class="max-w-7xl mx-auto px-6 h-16 flex justify-between items-center relative z-10">
                <div class="flex items-center space-x-3">
                    <div class="h-3 w-3 rounded-full bg-cyan-400 animate-ping"></div>
                    <span class="mono tracking-wider font-bold text-cyan-400 text-sm">NEXUS_CORE // v4.1.0</span>
                </div>
                <div class="hidden sm:flex items-center space-x-6 text-xs mono text-slate-400">
                    <span>NODE: <span class="text-cyan-400">ONLINE</span></span>
                    <span>ENCRYPTION: <span class="text-emerald-400">AES-256</span></span>
                    <span>LATENCY: <span class="text-cyan-400">12ms</span></span>
                </div>
            </div>
        </header>

        <!-- Main Cyber Hero Section -->
        <main class="max-w-4xl mx-auto px-6 py-20 text-center relative z-10 my-auto">
            <div class="absolute inset-0 -z-10 bg-gradient-to-tr from-cyan-500/10 via-transparent to-purple-500/10 blur-3xl pointer-events-none"></div>
            
            <div class="inline-block mb-4 border border-cyan-500/30 bg-cyan-500/10 px-4 py-1.5 rounded-full text-cyan-400 text-xs mono uppercase tracking-widest glow">
                Automated License Gateway
            </div>
            
            <h1 class="text-4xl md:text-7xl font-bold tracking-tight text-white mt-2">
                Decentralized <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 to-indigo-500 glow-text">Key Dispatch</span>
            </h1>
            
            <p class="text-slate-400 text-base md:text-lg mt-6 max-w-xl mx-auto">
                Securely interface with repository storage structures to claim cryptographic operational keys instantly.
            </p>

            <!-- Interactive Terminal Dispatch Box -->
            <div class="mt-12 bg-slate-900/90 border border-cyan-500/30 rounded-2xl p-8 shadow-2xl glow relative backdrop-blur-md">
                <div class="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-cyan-500 via-indigo-500 to-purple-500"></div>
                
                <form method="POST" class="space-y-6">
                    <input type="hidden" name="action" value="claim">
                    <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
                        <div class="mono bg-slate-950 border border-slate-800 px-4 py-3 rounded-xl text-xs text-slate-400 w-full sm:w-auto text-left">
                            <span>TARGET: <span class="text-cyan-400">keys.txt [GitHub]</span></span>
                        </div>
                        <button type="submit" class="w-full sm:w-auto bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-bold px-8 py-3.5 rounded-xl text-sm transition tracking-wide uppercase mono shadow-lg shadow-cyan-500/20 flex items-center justify-center gap-2">
                            <i class="fa-solid fa-terminal"></i> Execute Dispatch
                        </button>
                    </div>
                </form>

                {f'''
                <div class="mt-8 p-6 bg-slate-950 border border-cyan-500/40 rounded-xl text-left animate-pulse">
                    <p class="text-xs mono text-cyan-400 uppercase tracking-widest mb-2"><i class="fa-solid fa-check-circle mr-1"></i> {status_message}</p>
                    <div class="flex flex-col sm:flex-row items-center justify-between bg-slate-900 p-4 rounded-lg border border-slate-800 gap-4">
                        <code class="mono text-cyan-300 text-lg font-bold tracking-wider">{assigned_key}</code>
                        <button onclick="navigator.clipboard.writeText('{assigned_key}'); alert('Key copied to clipboard!');" class="bg-slate-800 hover:bg-slate-700 text-cyan-400 mono text-xs px-4 py-2 rounded-lg border border-slate-700 transition">
                            <i class="fa-solid fa-copy mr-1"></i> Copy Key
                        </button>
                    </div>
                </div>
                ''' if assigned_key else f'''
                <div class="mt-6 text-xs mono text-amber-400">
                    {status_message}
                </div>
                ''' if status_message else ""}
            </div>
        </main>

        <!-- Cyber Footer -->
        <footer class="border-t border-slate-900 bg-slate-950 py-6 text-center text-xs mono text-slate-500 relative z-10">
            <p>SYSTEM UPTIME: 99.99% // SECURED VIA RENDER & GITHUB SYNC</p>
        </footer>

        <!-- Particle Animation Script -->
        <script>
            const canvas = document.getElementById('particleCanvas');
            const ctx = canvas.getContext('2d');
            let particlesArray;

            function resizeCanvas() {{
                canvas.width = window.innerWidth;
                canvas.height = window.innerHeight;
            }}
            window.addEventListener('resize', resizeCanvas);
            resizeCanvas();

            class Particle {{
                constructor() {{
                    this.x = Math.random() * canvas.width;
                    this.y = Math.random() * canvas.height;
                    this.size = Math.random() * 2 + 1;
                    this.speedX = (Math.random() - 0.5) * 0.8;
                    this.speedY = (Math.random() - 0.5) * 0.8;
                }}
                update() {{
                    this.x += this.speedX;
                    this.y += this.speedY;
                    if (this.x > canvas.width) this.x = 0;
                    else if (this.x < 0) this.x = canvas.width;
                    if (this.y > canvas.height) this.y = 0;
                    else if (this.y < 0) this.y = canvas.height;
                }}
                draw() {{
                    ctx.fillStyle = 'rgba(6, 182, 212, 0.6)';
                    ctx.beginPath();
                    ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
                    ctx.fill();
                }}
            }}

            function initParticles() {{
                particlesArray = [];
                let numberOfParticles = (canvas.width * canvas.height) / 12000;
                for (let i = 0; i < numberOfParticles; i++) {{
                    particlesArray.push(new Particle());
                }}
            }}

            function animateParticles() {{
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                for (let i = 0; i < particlesArray.length; i++) {{
                    particlesArray[i].update();
                    particlesArray[i].draw();
                    
                    for (let j = i; j < particlesArray.length; j++) {{
                        let dx = particlesArray[i].x - particlesArray[j].x;
                        let dy = particlesArray[i].y - particlesArray[j].y;
                        let distance = Math.sqrt(dx * dx + dy * dy);
                        if (distance < 100) {{
                            ctx.strokeStyle = `rgba(6, 182, 212, ${{0.15 - distance/700}})`;
                            ctx.lineWidth = 0.5;
                            ctx.beginPath();
                            ctx.moveTo(particlesArray[i].x, particlesArray[i].y);
                            ctx.lineTo(particlesArray[j].x, particlesArray[j].y);
                            ctx.stroke();
                        }}
                    }}
                }}
                requestAnimationFrame(animateParticles);
            }}

            initParticles();
            animateParticles();
        </script>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run()
