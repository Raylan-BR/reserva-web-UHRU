import { requestAndShowAllReserve } from './dashboardRequests/requestAndShowAllReserve.js';
import { requestServer } from './utils/requestServer.js';
import { requestAndShowFormReserve } from './dashboardRequests/requestAndShowFormReserve.js';

DashboardLoaded();

async function DashboardLoaded() {
    const navHtml = await requestServer('/nav', true);
    document.querySelector('nav').innerHTML = navHtml;

    document.querySelector('.request_all_reserve')
    ?.addEventListener('click', requestAndShowAllReserve);

    document.querySelector('.request_reserve_form')
    ?.addEventListener('click', requestAndShowFormReserve);

    document.querySelector('.request_logout')
    ?.addEventListener('click', requestLogout);
}

requestAndShowAllReserve();

export function requestLogout(){
    localStorage.removeItem('token');
    window.location.href = '/';
}
