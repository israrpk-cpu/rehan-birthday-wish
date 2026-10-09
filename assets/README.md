const canvas = document.getElementById('fireworks');
const ctx = canvas.getContext('2d');
const button = document.getElementById('celebrateButton');

let particles = [];
let animationId;

function resizeCanvas() {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
}

window.addEventListener('resize', resizeCanvas);
resizeCanvas();

function createBurst(x, y, color) {
  const count = 40;
  for (let i = 0; i < count; i++) {
    const angle = (Math.PI * 2 * i) / count;
    const speed = 1.5 + Math.random() * 4.5;
    particles.push({
      x,
      y,
      vx: Math.cos(angle) * speed,
      vy: Math.sin(angle) * speed,
      life: 70 + Math.random() * 30,
      maxLife: 70 + Math.random() * 30,
      size: 2 + Math.random() * 3,
      color
    });
  }
}

function animate() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  for (let i = particles.length - 1; i >= 0; i--) {
    const p = particles[i];
    p.x += p.vx;
    p.y += p.vy;
    p.vy += 0.04;
    p.life -= 1;

    if (p.life <= 0) {
      particles.splice(i, 1);
      continue;
    }

    const alpha = p.life / p.maxLife;
    ctx.beginPath();
    ctx.fillStyle = p.color.replace(')', `, ${alpha})`).replace('rgb', 'rgba');
    ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
    ctx.fill();
  }

  animationId = requestAnimationFrame(animate);
}

function burstOnButton() {
  const colors = ['#ff4d8d', '#ffd166', '#56ccf2', '#7ae582', '#a78bfa'];
  for (let i = 0; i < 3; i++) {
    const x = Math.random() * window.innerWidth;
    const y = Math.random() * window.innerHeight * 0.58;
    createBurst(x, y, colors[Math.floor(Math.random() * colors.length)]);
  }
}

button.addEventListener('click', () => {
  button.textContent = 'Wishing You Joy! ✨';
  burstOnButton();
  setTimeout(() => {
    button.textContent = 'Celebrate Rehan 🎉';
  }, 1200);
});

setInterval(() => {
  const colors = ['#ff4d8d', '#ffd166', '#56ccf2', '#7ae582', '#a78bfa'];
  const x = Math.random() * window.innerWidth;
  const y = Math.random() * window.innerHeight * 0.7;
  createBurst(x, y, colors[Math.floor(Math.random() * colors.length)]);
}, 1400);

animate();
