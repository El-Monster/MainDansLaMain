// Menu pour petit écran
const hamburger = document.querySelector("#toggle-btn");

hamburger.addEventListener("click", function (){
    document.querySelector("#sidebar").classList.toggle("expand");
    const right = document.querySelector('#right');
    right.classList.toggle('expand');
});

// Lorsqu'on clique sur les menus du sidebar
const sidebarLinks = document.querySelectorAll('a.sidebar-link');

sidebarLinks.forEach((sidebarLink) => {
    sidebarLink.addEventListener('click', function () {
        sidebarLinks.forEach((link) => {
            link.classList.remove('selected');
        });
        sidebarLink.classList.add('selected');
    });
});

// Pour afficher ou masquer le sidebar sur les petits écrans 
const btnToggleLeft = document.querySelector('#toggleLeft');

btnToggleLeft.addEventListener("click", function () {
    // les panels
    const left = document.querySelector('#left');
    const right = document.querySelector('#right');
    left.classList.toggle('affiche');
    left.classList.toggle('hidden');
    right.classList.toggle('affiche');
    // les boutons 
    const btnMenu = document.querySelector('.bi.bi-list');
    const btnClose = document.querySelector('.bi.bi-x-lg');
    btnMenu.classList.toggle('visually-hidden');
    btnClose.classList.toggle('visually-hidden');
});