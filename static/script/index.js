import { requestAndShowAllReserve } from './dashboardRequests/requestAndShowAllReserve.js';
import { requestServer } from './utils/requestServer.js';
import { requestAndShowFormReserve } from './dashboardRequests/requestAndShowFormReserve.js';
import { requestAndShowMyAllReserve } from './dashboardRequests/requestAndShowMyAllReserve.js';

DashboardLoaded();

async function DashboardLoaded() {
    const navHtml = await requestServer('/nav', true);
    document.querySelector('nav').innerHTML = navHtml;

    document.querySelector('.request_all_reserve')
    ?.addEventListener('click', requestAndShowAllReserve);

    document.querySelector('.request_reserve_form')
    ?.addEventListener('click', requestAndShowFormReserve);

    document.querySelector('.request_my_reserve')
    ?.addEventListener('click', requestAndShowMyAllReserve);

    document.querySelector('.request_logout')
    ?.addEventListener('click', requestLogout);

    document.querySelector('.icon_hamburguer')
    ?.addEventListener('click', ()=>{
        openCloseMenu();
    });

    document.querySelectorAll('.option_nav').forEach(option=>{
        option.addEventListener('click', ()=>{
            openCloseMenu(true);
        });
    });
}

requestAndShowAllReserve();

export function requestLogout(){
    localStorage.removeItem('token');
    window.location.href = '/';
}
function openCloseMenu(close=false){
    const navBar = document.querySelector('nav');
    if(close){
        navBar.classList.remove('navBar');
    } else {
        navBar.classList.toggle('navBar');
    }
}