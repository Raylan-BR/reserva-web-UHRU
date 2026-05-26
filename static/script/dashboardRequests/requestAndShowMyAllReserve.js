import { requestServer } from '../utils/requestServer.js';
import { getDateReserve, getTimeReserve } from '../utils/formatDateTime.js';
import { notificationPopUp } from '../utils/notificationPopUp.js';

export async function requestAndShowMyAllReserve() {
    const myAllReserveJson = await requestServer('/api/getMyAllReserve');
    showItemHtml(myAllReserveJson);
}
async function showItemHtml(allReserve){
    const itemHtml = await requestServer('/myItem', true);

    const menuHtml = document.querySelector('main');

    // Limpar o conteúdo que já tinha
    menuHtml.innerHTML = '';

    showTitlePage('Suas Reservas', menuHtml);

    allReserve.forEach(reserve => {
        const reserveHtml = document.createElement('div');
        reserveHtml.classList.add('reserve_item');
        reserveHtml.innerHTML = itemHtml;
        reserveHtml.querySelector('#name_user_reserve').textContent = reserve.name;

        reserveHtml.querySelector('#date_user_reserve')
        .innerHTML = getDateReserve(reserve.dateTimeStart);

        const timeStart = getTimeReserve(reserve.dateTimeStart);
        const timeEnd = getTimeReserve(reserve.dateTimeEnd);

        reserveHtml.querySelector('#time_user_reserve')
        .innerHTML = `${timeStart} às ${timeEnd}`;

        reserveHtml.querySelector('.icon_delete')
        .dataset.id = reserve['_id']

        menuHtml.appendChild(reserveHtml);
    });
    document.querySelectorAll('.icon_delete').forEach(_delete => {
        _delete.addEventListener('click', requestDeleteMyReserve);
    });
}
async function requestDeleteMyReserve(event){
    const _id = event.currentTarget.dataset.id;
    const itemDeleted = event.currentTarget.parentElement.parentElement;
    const options = {
        method: 'DELETE'
    }
    
    const response = await requestServer(`/api/delete/${_id}`, false, options);

    if(response.sucess){
        console.log('Exterminado !');
        notificationPopUp('Exterminado !');
        itemDeleted.remove();
    } else {
        notificationPopUp('Não foi deletado !');
        console.log('Não foi possivel deletar');
    }
}

function showTitlePage(title, divMain){
    const titlePageHtml = document.createElement("h2");
    titlePageHtml.classList.add("page_title");
    titlePageHtml.textContent = title;
    divMain.appendChild(titlePageHtml);
}