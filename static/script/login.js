import { notificationPopUp } from './utils/notificationPopUp.js';
import { messageRequest } from './utils/messageRequest.js';

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
            if (data.token){
                localStorage.setItem('token', data.token);
                window.location.href = '/';
            } else {
                notificationPopUp(messageRequest[data.message]);
            }
        });
    
    } catch (error) {
        notificationPopUp('Problema no servidor');
    }
});