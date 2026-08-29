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
        <title>NEXUS-X // Quantum 3D Node</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
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
            .glow {{ box-shadow: 0 0 35px rgba(6, 182, 212, 0.3); }}
            .glow-text {{ text-shadow: 0 0 20px rgba(6, 182, 212, 0.6); }}
            #webgl-container {{ position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; pointer-events: none; z-index: 0; }}
        </style>
    </head>
    <body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col justify-between selection:bg-cyan-500 selection:text-black relative overflow-x-hidden">

        <!-- 3D Interactive WebGL Background -->
        <div id="webgl-container"></div>

        <!-- Top Telemetry Status -->
        <header class="border-b border-cyan-500/20 bg-slate-950/70 backdrop-blur-xl sticky top-0 z-50">
            <div class="max-w-7xl mx-auto px-6 h-16 flex justify-between items-center relative z-10">
                <div class="flex items-center space-x-3">
                    <div class="h-3 w-3 rounded-full bg-cyan-400 animate-ping"></div>
                    <span class="mono tracking-wider font-bold text-cyan-400 text-sm">NEXUS_3D // v5.0.0</span>
                </div>
                <div class="hidden sm:flex items-center space-x-6 text-xs mono text-slate-400">
                    <span>ENGINE: <span class="text-cyan-400">THREE.JS WebGL</span></span>
                    <span>ENCRYPTION: <span class="text-emerald-400">QUANTUM-AES</span></span>
                    <span>LATENCY: <span class="text-cyan-400">4ms</span></span>
                </div>
            </div>
        </header>

        <!-- Main Cyber Hero Section -->
        <main class="max-w-4xl mx-auto px-6 py-20 text-center relative z-10 my-auto">
            <div class="absolute inset-0 -z-10 bg-gradient-to-tr from-cyan-500/10 via-transparent to-purple-500/10 blur-3xl pointer-events-none"></div>
            
            <div class="inline-block mb-4 border border-cyan-500/30 bg-cyan-500/10 px-4 py-1.5 rounded-full text-cyan-400 text-xs mono uppercase tracking-widest glow">
                Next-Gen Spatial Gateway
            </div>
            
            <h1 class="text-4xl md:text-7xl font-bold tracking-tight text-white mt-2">
                Decentralized <span class="text-transparent bg-clip-text bg-gradient-to-r from-cyan-400 via-teal-300 to-indigo-500 glow-text">Quantum Core</span>
            </h1>
            
            <p class="text-slate-400 text-base md:text-lg mt-6 max-w-xl mx-auto">
                Interact with the multidimensional storage grid to extract high-security cryptographic operational keys instantly.
            </p>

            <!-- Interactive Terminal Dispatch Box -->
            <div class="mt-12 bg-slate-900/80 border border-cyan-500/30 rounded-2xl p-8 shadow-2xl glow relative backdrop-blur-xl transition-all duration-300 hover:border-cyan-400">
                <div class="absolute top-0 left-0 right-0 h-1 bg-gradient-to-r from-cyan-500 via-indigo-500 to-purple-500"></div>
                
                <form method="POST" class="space-y-6">
                    <input type="hidden" name="action" value="claim">
                    <div class="flex flex-col sm:flex-row items-center justify-center gap-4">
                        <div class="mono bg-slate-950/80 border border-slate-800 px-4 py-3 rounded-xl text-xs text-slate-400 w-full sm:w-auto text-left">
                            <span>TARGET: <span class="text-cyan-400">keys.txt [Matrix Sync]</span></span>
                        </div>
                        <button type="submit" class="w-full sm:w-auto bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-bold px-8 py-3.5 rounded-xl text-sm transition-all duration-300 tracking-wide uppercase mono shadow-lg shadow-cyan-500/30 flex items-center justify-center gap-2 transform hover:-translate-y-0.5">
                            <i class="fa-solid fa-cube"></i> Initialize Extraction
                        </button>
                    </div>
                </form>

                {f'''
                <div class="mt-8 p-6 bg-slate-950/90 border border-cyan-500/40 rounded-xl text-left animate-pulse">
                    <p class="text-xs mono text-cyan-400 uppercase tracking-widest mb-2"><i class="fa-solid fa-check-circle mr-1"></i> {status_message}</p>
                    <div class="flex flex-col sm:flex-row items-center justify-between bg-slate-900/80 p-4 rounded-lg border border-slate-800 gap-4">
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
        <footer class="border-t border-slate-900 bg-slate-950/80 py-6 text-center text-xs mono text-slate-500 relative z-10 backdrop-blur-md">
            <p>SYSTEM UPTIME: 99.99% // POWERED BY THREE.JS WEBGL RENDERER</p>
        </footer>

        <!-- Three.js 3D Background Animation Script -->
        <script>
            const container = document.getElementById('webgl-container');
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({{ alpha: true, antialias: true }});
            
            renderer.setSize(window.innerWidth, window.innerHeight);
            renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
            container.appendChild(renderer.domElement);

            // Create 3D Torus Knot Wireframe Core
            const geometry = new THREE.TorusKnotGeometry(10, 3, 100, 16);
            const material = new THREE.MeshBasicMaterial({{
                color: 0x06b6d4,
                wireframe: true,
                transparent: true,
                opacity: 0.18
            }});
            const torusKnot = new THREE.Mesh(geometry, material);
            scene.add(torusKnot);

            // Create 3D Floating Particle Field
            const particlesGeometry = new THREE.BufferGeometry();
            const particlesCount = 1200;
            const posArray = new Float32Array(particlesCount * 3);

            for(let i = 0; i < particlesCount * 3; i++) {{
                posArray[i] = (Math.random() - 0.5) * 80;
            }}

            particlesGeometry.setAttribute('position', new THREE.BufferAttribute(posArray, 3));
            const particlesMaterial = new THREE.PointsMaterial({{
                size: 0.15,
                color: 0x06b6d4,
                transparent: true,
                opacity: 0.7
            }});
            const particlesMesh = new THREE.Points(particlesGeometry, particlesMaterial);
            scene.add(particlesMesh);

            camera.position.z = 30;

            // Mouse Interaction Tracking
            let mouseX = 0;
            let mouseY = 0;
            let targetX = 0;
            let targetY = 0;

            document.addEventListener('mousemove', (event) => {{
                mouseX = (event.clientX - window.innerWidth / 2) * 0.001;
                mouseY = (event.clientY - window.innerHeight / 2) * 0.001;
            }});

            // Animation Loop
            const clock = new THREE.Clock();

            function animate() {{
                requestAnimationFrame(animate);

                targetX = mouseX * 2;
                targetY = mouseY * 2;

                torusKnot.rotation.x += 0.003 + (targetY - torusKnot.rotation.x) * 0.05;
                torusKnot.rotation.y += 0.005 + (targetX - torusKnot.rotation.y) * 0.05;

                particlesMesh.rotation.y = clock.getElapsedTime() * 0.03;

                renderer.render(scene, camera);
            }}

            animate();

            // Responsive Window Scaling
            window.addEventListener('resize', () => {{
                camera.aspect = window.innerWidth / window.innerHeight;
                camera.updateProjectionMatrix();
                renderer.setSize(window.innerWidth, window.innerHeight);
            }});
        </script>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run()
