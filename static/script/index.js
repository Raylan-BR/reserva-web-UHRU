// Mostrar tela do usuário autenticado ou não
document.addEventListener('DOMContentLoaded', () => {
    const token = localStorage.getItem('token');
    fetch('/nav',{
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${token}`,
        },
        method: 'GET',
    })
    .then(response => response.text())
    .then(html => {
        document.querySelector('nav').innerHTML = html;
    });
});