const sbtn = document.getElementById('start-btn');
const tmr = document.getElementById('timer');
let startTime;
let timerInterval;

sbtn.addEventListener('click', function() {
    document.getElementById('status').textContent = 'Duel started!';
    startTime = Date.now();
    sbtn.disabled = true;
    timerInterval = setInterval(() => {
      const alr = Date.now() - startTime;
      const scsPassed = Math.floor(alr / 1000);
      tmr.textContent = `Time: ${scsPassed} secs.`;
    }, 1000);
});