import { requestServer } from "../utils/requestServer.js";
import { validateDateTime } from "../utils/formatDateTime.js";
import { notificationPopUp } from '../utils/notificationPopUp.js'; 
import { messageRequest } from "../utils/messageRequest.js";
import { openCloseMenu } from "../utils/menuMobile.js";
import { getTimeReserve } from "../utils/formatDateTime.js";

export async function requestAndShowFormReserve(){
    const formReserveHtml = await requestServer('/form', true);

    const menuHtml = document.querySelector('main');

    // Limpar o conteúdo que já tinha
    menuHtml.innerHTML = '';

    menuHtml.innerHTML = formReserveHtml;

    openCloseMenu(true);

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

        if(response.sucess){
            notificationPopUp(messageRequest[response.message]);
            setTimeout(() => {
                window.location.href = '/';
            }, 2000);
        } else {
            if (response.message == 'ERROR_TIME_EXIST') {
                let timeExistStart = response.reserve.dateTimeStart;
                timeExistStart = getTimeReserve(timeExistStart);

                let timeExistEnd = response.reserve.dateTimeEnd;
                timeExistEnd = getTimeReserve(timeExistEnd);

                notificationPopUp(`Já existe entre ${timeExistStart}h e ${timeExistEnd}h`);
            }  else {
                notificationPopUp(messageRequest[response.message]);
            } 
        }

    } catch(err) {

        console.error(err);

    }
}