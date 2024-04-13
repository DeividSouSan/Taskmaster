const menuBtn = document.querySelector(".account-button");
const menu = document.querySelector(".floating-menu-container");

menuBtn.addEventListener('click', (ev) => {
    menu.classList.remove("hide");
});

document.addEventListener('click', (ev) => {
    console.log("Chamou o evento do documento.");
    if (!menu.contains(ev.target) && !menuBtn.contains(ev.target)) {
        menu.classList.add("hide");
    }
});
