from flask import Flask, render_template_string, request

app = Flask(__name__)

PRODUCTS = [
    {
        "id": "predator-edge",
        "name": "PREDATOR EDGE.1 3D",
        "category": "Quantum Cleat Matrix",
        "price": "$280",
        "desc": "Engineered with biometric grip zones and a responsive holographic chassis for ultimate pitch mastery.",
        "geometry": "box"
    },
    {
        "id": "ultraboost-x",
        "name": "ULTRABOOST X-SPACE",
        "category": "Kinetic Runner",
        "price": "$220",
        "desc": "Zero-gravity fluid cushioning cells combined with a reactive neural-mesh knit upper.",
        "geometry": "sphere"
    },
    {
        "id": "nmd-quantum",
        "name": "NMD_R1 QUANTUM GRID",
        "category": "Urban Cyberwear",
        "price": "$170",
        "desc": "Futuristic lifestyle silhouette featuring floating plug mechanics and adaptive LED fiber-weaves.",
        "geometry": "torus"
    }
]

@app.route('/')
def adidas_showcase():
    html_content = """
    <!DOCTYPE html>
    <html lang="en" class="dark">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ADIDAS // QUANTUM MATRIX SHOWCASE</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
        <script>
            tailwind.config = {{
                darkMode: 'class',
                theme: {{
                    extend: {{
                        colors: {{
                            adidas: {{ 500: '#111111', 600: '#00ffcc', 950: '#050505' }}
                        }}
                    }}
                }}
            }}
        </script>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;500;700;900&family=JetBrains+Mono:wght@400;700&display=swap');
            body {{ font-family: 'Space Grotesk', sans-serif; }}
            .mono {{ font-family: 'JetBrains Mono', monospace; }}
            .glow {{ box-shadow: 0 0 40px rgba(0, 255, 204, 0.25); }}
            .glow-text {{ text-shadow: 0 0 20px rgba(0, 255, 204, 0.6); }}
            #webgl-container {{ position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; pointer-events: none; z-index: 0; }}
            .glass {{ background: rgba(10, 10, 10, 0.75); backdrop-filter: blur(20px); border: 1px solid rgba(0, 255, 204, 0.2); }}
        </style>
    </head>
    <body class="bg-black text-white min-h-screen flex flex-col justify-between selection:bg-[#00ffcc] selection:text-black relative overflow-x-hidden">

        <!-- 3D WebGL Live Particle & Shape Grid -->
        <div id="webgl-container"></div>

        <!-- Telemetry Header -->
        <header class="border-b border-[#00ffcc]/20 bg-black/60 backdrop-blur-xl sticky top-0 z-50">
            <div class="max-w-7xl mx-auto px-6 h-20 flex justify-between items-center relative z-10">
                <div class="flex items-center space-x-4">
                    <div class="text-2xl font-black tracking-tighter text-white flex items-center gap-1">
                        ADIDAS <span class="text-[#00ffcc] text-xs mono px-2 py-0.5 border border-[#00ffcc]/40 rounded">3D.X</span>
                    </div>
                </div>
                <div class="hidden md:flex items-center space-x-8 text-xs mono text-slate-400">
                    <span>MODE: <span class="text-[#00ffcc]">INTERACTIVE SPATIAL</span></span>
                    <span>ENGINE: <span class="text-emerald-400">THREE.JS r128</span></span>
                    <span>SYNC: <span class="text-[#00ffcc]">OPTIMIZED</span></span>
                </div>
            </div>
        </header>

        <!-- Main Hero Section -->
        <main class="max-w-7xl mx-auto px-6 py-16 relative z-10 my-auto w-full">
            <div class="text-center max-w-3xl mx-auto mb-16">
                <div class="inline-block mb-4 border border-[#00ffcc]/40 bg-[#00ffcc]/10 px-4 py-1.5 rounded-full text-[#00ffcc] text-xs mono uppercase tracking-widest glow">
                    Next-Gen Spatial Catalog
                </div>
                <h1 class="text-5xl md:text-8xl font-black tracking-tight mt-2 uppercase">
                    Future <span class="text-transparent bg-clip-text bg-gradient-to-r from-[#00ffcc] via-teal-300 to-cyan-500 glow-text">Footwear</span>
                </h1>
                <p class="text-slate-400 text-base md:text-lg mt-6 max-w-xl mx-auto font-light">
                    Interact with multidimensional product geometries in real-time. Rotate, inspect, and experience footwear engineered for the metaverse.
                </p>
            </div>

            <!-- Interactive Product Grid -->
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8 relative z-10">
                {% for p in products %}
                <div class="glass rounded-3xl p-8 flex flex-col justify-between transition-all duration-500 hover:border-[#00ffcc] hover:scale-105 hover:glow group cursor-pointer" onclick="changeModel('{{ p.geometry }}')">
                    <div>
                        <div class="flex justify-between items-start mb-6">
                            <span class="text-xs mono text-[#00ffcc] uppercase tracking-widest">{{ p.category }}</span>
                            <span class="text-lg font-bold mono text-white">{{ p.price }}</span>
                        </div>
                        <h3 class="text-2xl font-bold mb-3 group-hover:text-[#00ffcc] transition-colors">{{ p.name }}</h3>
                        <p class="text-slate-400 text-sm leading-relaxed mb-6">{{ p.desc }}</p>
                    </div>
                    <div class="pt-4 border-t border-slate-800 flex items-center justify-between">
                        <span class="text-xs mono text-slate-500 group-hover:text-[#00ffcc] transition-colors">CLICK TO MORPH 3D NODE</span>
                        <div class="h-8 w-8 rounded-full bg-[#00ffcc]/10 border border-[#00ffcc]/30 flex items-center justify-center text-[#00ffcc] group-hover:bg-[#00ffcc] group-hover:text-black transition-all">
                            <i class="fa-solid fa-arrow-right text-xs"></i>
                        </div>
                    </div>
                </div>
                {% endfor %}
            </div>
        </main>

        <!-- Footer -->
        <footer class="border-t border-slate-900 bg-black/80 py-8 text-center text-xs mono text-slate-500 relative z-10 backdrop-blur-md">
            <p>ADIDAS GLOBAL INNOVATION LAB // QUANTUM DIVISION</p>
        </footer>

        <!-- Three.js Interactive 3D Script -->
        <script>
            const container = document.getElementById('webgl-container');
            const scene = new THREE.Scene();
            const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
            const renderer = new THREE.WebGLRenderer({{ alpha: true, antialias: true }});
            
            renderer.setSize(window.innerWidth, window.innerHeight);
            renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
            container.appendChild(renderer.domElement);

            // Dynamic Active 3D Geometry Object
            let currentMesh;
            const material = new THREE.MeshBasicMaterial({{
                color: 0x00ffcc,
                wireframe: true,
                transparent: true,
                opacity: 0.25
            }});

            function createGeometry(type) {{
                if (currentMesh) scene.remove(currentMesh);
                let geom;
                if (type === 'box') {{
                    geom = new THREE.BoxGeometry(12, 12, 12, 6, 6, 6);
                }} else if (type === 'sphere') {{
                    geom = new THREE.IcosahedronGeometry(10, 2);
                }} else {{
                    geom = new THREE.TorusKnotGeometry(9, 3, 100, 16);
                }}
                currentMesh = new THREE.Mesh(geom, material);
                scene.add(currentMesh);
            }}

            createGeometry('torus');

            function changeModel(type) {{
                createGeometry(type);
            }}

            // Floating Particle Field
            const particlesGeometry = new THREE.BufferGeometry();
            const particlesCount = 800;
            const posArray = new Float32Array(particlesCount * 3);

            for(let i = 0; i < particlesCount * 3; i++) {{
                posArray[i] = (Math.random() - 0.5) * 70;
            }}

            particlesGeometry.setAttribute('position', new THREE.BufferAttribute(posArray, 3));
            const particlesMaterial = new THREE.PointsMaterial({{
                size: 0.12,
                color: 0x00ffcc,
                transparent: true,
                opacity: 0.6
            }});
            const particlesMesh = new THREE.Points(particlesGeometry, particlesMaterial);
            scene.add(particlesMesh);

            camera.position.z = 30;

            // Mouse Interaction
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

                targetX = mouseX * 3;
                targetY = mouseY * 3;

                if (currentMesh) {{
                    currentMesh.rotation.x += 0.004 + (targetY - currentMesh.rotation.x) * 0.05;
                    currentMesh.rotation.y += 0.006 + (targetX - currentMesh.rotation.y) * 0.05;
                }}

                particlesMesh.rotation.y = clock.getElapsedTime() * 0.02;

                renderer.render(scene, camera);
            }}

            animate();

            window.addEventListener('resize', () => {{
                camera.aspect = window.innerWidth / window.innerHeight;
                camera.updateProjectionMatrix();
                renderer.setSize(window.innerWidth, window.innerHeight);
            }});
        </script>
    </body>
    </html>
    """
    return render_template_string(html_content, products=PRODUCTS)

if __name__ == '__main__':
    app.run()
