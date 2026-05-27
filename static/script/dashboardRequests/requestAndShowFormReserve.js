import { requestServer } from "../utils/requestServer.js";
import { validateDateTime } from "../utils/formatDateTime.js";
import { notificationPopUp } from '../utils/notificationPopUp.js'; 
import { messageRequest } from "../utils/messageRequest.js";

export async function requestAndShowFormReserve(){
    const formReserveHtml = await requestServer('/form', true);

    const menuHtml = document.querySelector('main');

    // Limpar o conteúdo que já tinha
    menuHtml.innerHTML = '';

    menuHtml.innerHTML = formReserveHtml;

    document.querySelector('.reserve_home_now')
    .addEventListener('submit', requestSetMyReserve);
}

async function requestSetMyReserve(event){

    try {

        event.preventDefault();

        const dateInput = document.querySelector('#date').value;
        const timeStart = document.querySelector('#timeStart').value;
        const timeEnd = document.querySelector('#timeEnd').value;

        const dateTime = validateDateTime(dateInput, timeStart, timeEnd);
        const options = {
            method : 'POST',
            body: JSON.stringify(dateTime),
        }

        const response = await requestServer('/api/setMyReserve', false, options);
        
        notificationPopUp(messageRequest[response.message]);

    } catch(err) {

        console.error(err);

    }
}