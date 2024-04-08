const accountButton = document.querySelector(".account-button");
const floatingMenu = document.querySelector(".floating-menu-container");
const headerAfterAuth = document.querySelector(".header-after-auth");

accountButton.addEventListener('click', (ev) => {

    if (floatingMenu.classList.contains("active")) {
        floatingMenu.style.display = "none";
    } else {
        floatingMenu.style.display = "block";
    }

    floatingMenu.classList.toggle("active");
});

document.addEventListener('click', (ev) => {
    if (ev.target.classList.contains("floating-menu-container")) {
        console.log("Tá clicando no menu")
    }
});
