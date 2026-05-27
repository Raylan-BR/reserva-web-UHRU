export function openCloseMenu(close=false){
    const navBar = document.querySelector('nav');
    if(close){
        navBar.classList.remove('navBar');
    } else {
        navBar.classList.toggle('navBar');
    }
}