import { requestServer } from "../utils/requestServer.js";


export async function requestAndShowFormReserve(){
    const formReserveHtml = await requestServer('/form', true);

    const menuHtml = document.querySelector('main');

    // Limpar o conteúdo que já tinha
    menuHtml.innerHTML = '';

    menuHtml.innerHTML = formReserveHtml;
}