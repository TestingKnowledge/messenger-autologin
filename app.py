from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def flappy_game():
    html_content = """
    <!DOCTYPE html>
    <html lang="en" class="dark">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>CYBER_FLAP // Quantum Node Runner</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
        <script>
            tailwind.config = {
                darkMode: 'class',
                theme: {
                    extend: {
                        colors: {
                            cyber: { 500: '#06b6d4', 600: '#0891b2', 950: '#030712' }
                        }
                    }
                }
            }
        </script>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;500;700&family=JetBrains+Mono:wght@400;700&display=swap');
            body { font-family: 'Space Grotesk', sans-serif; }
            .mono { font-family: 'JetBrains Mono', monospace; }
            .glow { box-shadow: 0 0 30px rgba(6, 182, 212, 0.3); }
            .glow-text { text-shadow: 0 0 15px rgba(6, 182, 212, 0.6); }
        </style>
    </head>
    <body class="bg-slate-950 text-slate-100 min-h-screen flex flex-col items-center justify-between selection:bg-cyan-500 selection:text-black overflow-hidden">

        <header class="w-full border-b border-cyan-500/20 bg-slate-950/80 backdrop-blur-md py-4 text-center">
            <h1 class="text-xl font-bold mono text-cyan-400 tracking-wider glow-text">CYBER_FLAP // v1.0.0</h1>
        </header>

        <main class="flex flex-col items-center justify-center my-auto relative">
            <div class="relative bg-slate-900 border border-cyan-500/30 rounded-2xl p-4 shadow-2xl glow backdrop-blur-md">
                <canvas id="gameCanvas" width="400" height="600" class="rounded-xl bg-slate-950 border border-slate-800 block cursor-pointer"></canvas>
                <div id="overlay" class="absolute inset-0 flex flex-col items-center justify-center bg-slate-950/80 backdrop-blur-sm rounded-xl transition-opacity">
                    <div class="text-center p-6">
                        <h2 class="text-3xl font-black text-white mb-2 uppercase tracking-wide">Cyber <span class="text-cyan-400">Flight</span></h2>
                        <p class="text-xs mono text-slate-400 mb-6">Press SPACE or CLICK to navigate the quantum grid.</p>
                        <button onclick="startGame()" class="bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-bold px-8 py-3 rounded-xl text-sm transition tracking-wide uppercase mono shadow-lg shadow-cyan-500/20">
                            Initialize Flight
                        </button>
                    </div>
                </div>
            </div>
        </main>

        <footer class="w-full border-t border-slate-900 bg-slate-950 py-4 text-center text-xs mono text-slate-500">
            <p>CONTROL: CLICK / SPACEBAR TO JUMP</p>
        </footer>

        <script>
            const canvas = document.getElementById('gameCanvas');
            const ctx = canvas.getContext('2d');
            const overlay = document.getElementById('overlay');

            let gameStarted = false;
            let gameOver = false;
            let score = 0;
            let highscore = 0;

            let bird = {
                x: 80,
                y: 300,
                radius: 12,
                gravity: 0.45,
                lift: -8,
                velocity: 0
            };

            let pipes = [];
            let pipeWidth = 60;
            let pipeGap = 160;
            let pipeSpeed = 3;
            let frameCount = 0;

            function resetGame() {
                bird.y = 300;
                bird.velocity = 0;
                pipes = [];
                score = 0;
                frameCount = 0;
                gameOver = false;
                overlay.style.display = 'none';
                loop();
            }

            function startGame() {
                gameStarted = true;
                resetGame();
            }

            function jump() {
                if (!gameStarted || gameOver) return;
                bird.velocity = bird.lift;
            }

            window.addEventListener('keydown', (e) => {
                if (e.code === 'Space') {
                    e.preventDefault();
                    if (!gameStarted || gameOver) {
                        startGame();
                    } else {
                        jump();
                    }
                }
            });

            canvas.addEventListener('click', () => {
                if (!gameStarted || gameOver) {
                    startGame();
                } else {
                    jump();
                }
            });

            function spawnPipe() {
                let minHeight = 50;
                let maxHeight = canvas.height - pipeGap - 50;
                let height = Math.floor(Math.random() * (maxHeight - minHeight + 1)) + minHeight;
                pipes.push({
                    x: canvas.width,
                    top: height,
                    bottom: canvas.height - height - pipeGap,
                    passed: false
                });
            }

            function update() {
                if (gameOver) return;

                bird.velocity += bird.gravity;
                bird.y += bird.velocity;

                if (bird.y + bird.radius >= canvas.height || bird.y - bird.radius <= 0) {
                    endGame();
                }

                if (frameCount % 100 === 0) {
                    spawnPipe();
                }

                for (let i = pipes.length - 1; i >= 0; i--) {
                    pipes[i].x -= pipeSpeed;

                    if (
                        bird.x + bird.radius > pipes[i].x &&
                        bird.x - bird.radius < pipes[i].x + pipeWidth &&
                        (bird.y - bird.radius < pipes[i].top || bird.y + bird.radius > canvas.height - pipes[i].bottom)
                    ) {
                        endGame();
                    }

                    if (!pipes[i].passed && pipes[i].x + pipeWidth < bird.x) {
                        score++;
                        pipes[i].passed = true;
                    }

                    if (pipes[i].x + pipeWidth < 0) {
                        pipes.splice(i, 1);
                    }
                }

                frameCount++;
            }

            function draw() {
                ctx.clearRect(0, 0, canvas.width, canvas.height);

                ctx.strokeStyle = 'rgba(6, 182, 212, 0.05)';
                ctx.lineWidth = 1;
                for (let i = 0; i < canvas.width; i += 30) {
                    ctx.beginPath();
                    ctx.moveTo(i, 0);
                    ctx.lineTo(i, canvas.height);
                    ctx.stroke();
                }

                pipes.forEach(pipe => {
                    ctx.fillStyle = '#06b6d4';
                    ctx.shadowColor = '#06b6d4';
                    ctx.shadowBlur = 10;
                    ctx.fillRect(pipe.x, 0, pipeWidth, pipe.top);
                    ctx.fillRect(pipe.x, canvas.height - pipe.bottom, pipeWidth, pipe.bottom);
                    ctx.shadowBlur = 0;
                });

                ctx.fillStyle = '#22d3ee';
                ctx.shadowColor = '#22d3ee';
                ctx.shadowBlur = 15;
                ctx.beginPath();
                ctx.arc(bird.x, bird.y, bird.radius, 0, Math.PI * 2);
                ctx.fill();
                ctx.shadowBlur = 0;

                ctx.fillStyle = '#ffffff';
                ctx.font = 'bold 24px "JetBrains Mono", monospace';
                ctx.textAlign = 'center';
                ctx.fillText(score, canvas.width / 2, 50);
            }

            function endGame() {
                gameOver = true;
                if (score > highscore) highscore = score;
                overlay.style.display = 'flex';
                overlay.querySelector('h2').textContent = 'System Crash';
                overlay.querySelector('p').innerHTML = `Score: <span class="text-cyan-400 font-bold">${score}</span> | High Score: <span class="text-emerald-400 font-bold">${highscore}</span>`;
                overlay.querySelector('button').textContent = 'Reboot Node';
            }

            function loop() {
                if (!gameOver) {
                    update();
                    draw();
                    requestAnimationFrame(loop);
                }
            }

            draw();
        </script>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run()
