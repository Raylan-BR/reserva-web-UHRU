import { requestServer } from "../utils/requestServer.js";
import { getDateReserve, getTimeReserve } from "../utils/formatDateTime.js";


export async function requestAndShowAllReserve() {
    const allReserveJson = await requestServer('/api/getAllReserve');
    showItemHtml(allReserveJson);
}
async function showItemHtml(allReserve){
    const itemHtml = await requestServer('/item', true);

    const menuHtml = document.querySelector('main');

    // Limpar o conteúdo que já tinha
    menuHtml.innerHTML = '';
    showTitlePage('Todas as Reservas', menuHtml);

    // Mostrar reserva em processo
    const reserveCurrent = getReserveCurrentJSON(allReserve);
    if(reserveCurrent){
        const reserveCurrentHtml = buildItemPage(reserveCurrent, itemHtml);
        reserveCurrentHtml.classList.add('reserveCurrent');
        menuHtml.appendChild(reserveCurrentHtml);
    }

    allReserve.forEach(reserve => {
        const reserveHtml = buildItemPage(reserve, itemHtml);
        menuHtml.appendChild(reserveHtml);
    });
}
function showTitlePage(title, divMain){
    const titlePageHtml = document.createElement("h2");
    titlePageHtml.classList.add("page_title");
    titlePageHtml.textContent = title;
    divMain.appendChild(titlePageHtml);
}
function buildItemPage(itemJson, itemHtml){

    const reserveHtml = document.createElement("div");
    reserveHtml.classList.add("reserve_item");
    reserveHtml.innerHTML = itemHtml;
    reserveHtml.querySelector('#name_user_reserve').textContent = itemJson.name;

    reserveHtml.querySelector('#date_user_reserve')
    .innerHTML = getDateReserve(itemJson.dateTimeStart);

    const timeStart = getTimeReserve(itemJson.dateTimeStart);
    const timeEnd = getTimeReserve(itemJson.dateTimeEnd);

    reserveHtml.querySelector('#time_user_reserve')
    .innerHTML = `${timeStart} às ${timeEnd}`;

    return reserveHtml;
}
function getReserveCurrentJSON(allReserve){

    const timeNow = new Date();

    const reservaAtual = allReserve.find(reserva => {
        const timeStart = new Date(reserva.dateTimeStart);
        const timeEnd = new Date(reserva.dateTimeEnd);
        return timeNow >= timeStart && timeNow <= timeEnd;
    });

    return reservaAtual;
}