document.addEventListener('DOMContentLoaded', () => {
    const input = document.getElementById('myInput');
    const clearBtn = document.getElementById('clearBtn');
    const sendBtn = document.getElementById('sendBtn');
    const orb1 = document.querySelector('.orb-1');
    const orb2 = document.querySelector('.orb-2');

    // Движение шаров за мышкой
    document.addEventListener('mousemove', (e) => {
        const x = e.clientX / window.innerWidth;
        const y = e.clientY / window.innerHeight;
        if (orb1) orb1.style.transform = translate(${x * 40}px, ${y * 40}px);
        if (orb2) orb2.style.transform = translate(${x * -60}px, ${y * -60}px);
    });

    // Функция искр
    function spawnParticles(x, y, color) {
        for (let i = 0; i < 10; i++) {
            const p = document.createElement('div');
            p.className = 'particle';
            p.style.left = x + 'px';
            p.style.top = y + 'px';
            p.style.width = p.style.height = Math.random() * 6 + 2 + 'px';
            p.style.background = color;
            document.body.appendChild(p);

            p.animate([
                { transform: 'translate(0,0)', opacity: 1 },
                { transform: translate(${(Math.random()-0.5)*200}px, ${(Math.random()-0.5)*200}px), opacity: 0 }
            ], { duration: 600 }).onfinish = () => p.remove();
        }
    }

    // Кнопка Clear
    clearBtn.addEventListener('click', (e) => {
        spawnParticles(e.clientX, e.clientY, '#ff4d4d');
        input.value = "";
    });

    // Кнопка Send
    sendBtn.addEventListener('click', (e) => {
        if (input.value.trim() === "") {
            input.classList.add('shake');
            setTimeout(() => input.classList.remove('shake'), 400);
        } else {
            spawnParticles(e.clientX, e.clientY, '#03dac6');
            console.log("Отправлено:", input.value);
            input.value = "";
        }
    });
});