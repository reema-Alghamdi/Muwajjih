
const API = 'http://127.0.0.1:5001';

document.getElementById('scoreBtn').addEventListener('click', async () => {
  const text = document.getElementById('cvText').value;
  const res = await fetch(`${API}/api/score_cv`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text })
  });
  const data = await res.json();
  document.getElementById('cvResult').innerHTML = `<b>Score:</b> ${data.score}/100<br><ul>${
    data.tips.map(t => `<li>${t}</li>`).join('')
  }</ul>`;
});

document.getElementById('recBtn').addEventListener('click', async () => {
  const skills = document.getElementById('skillsInput').value.split(',').map(s => s.trim()).filter(Boolean);
  const res = await fetch(`${API}/api/recommend_jobs`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ skills })
  });
  const data = await res.json();
  document.getElementById('jobsResult').innerHTML = data.jobs.map(j => `
    <div class="job">
      <b>${j.title}</b> – ${j.city} – قطاع ${j.sector} – <b>توافق ${j.match}%</b>
    </div>
  `).join('');
});

document.getElementById('insightsBtn').addEventListener('click', async () => {
  const res = await fetch(`${API}/api/insights`);
  const data = await res.json();
  document.getElementById('insights').textContent = JSON.stringify(data, null, 2);
});
