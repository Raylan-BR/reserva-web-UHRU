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

    allReserve.forEach(reserve => {
        const reserveHtml = document.createElement("div");
        reserveHtml.classList.add("reserve_item");
        reserveHtml.innerHTML = itemHtml;
        reserveHtml.querySelector('#name_user_reserve').textContent = reserve.name;

        reserveHtml.querySelector('#date_user_reserve')
        .innerHTML = getDateReserve(reserve.dateTimeStart);

        const timeStart = getTimeReserve(reserve.dateTimeStart);
        const timeEnd = getTimeReserve(reserve.dateTimeEnd);

        reserveHtml.querySelector('#time_user_reserve')
        .innerHTML = `${timeStart} às ${timeEnd}`;

        menuHtml.appendChild(reserveHtml);
    });
}
function showTitlePage(title, divMain){
    const titlePageHtml = document.createElement("h2");
    titlePageHtml.classList.add("page_title");
    titlePageHtml.textContent = title;
    divMain.appendChild(titlePageHtml);
}