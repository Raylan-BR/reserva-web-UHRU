document.querySelector('form').addEventListener('submit', (e) =>{
    e.preventDefault();

    const email = document.querySelector('#login_email').value;

    try {
        fetch('/api/getTokenLogin',{
            headers: {'Content-Type': 'application/json'},
            method: 'POST',
            body: JSON.stringify({'email': email}),
        })
        .then(response => response.json())
        .then(data => {
            console.log(`data: ${data}`)
            if (data.token){
                localStorage.setItem('token', data.token);
                window.location.href = '/';
            } else {
                console.log('Não encontramos seu email !');
            }
        });
    
    } catch (error) {
        console.error('Erro de requisição:', error);
    }
});