
var button = document.querySelector(".add-task-button");

const template = document.querySelector(".add-task-template");

const modal = template.content.cloneNode(true);
const container = modal.querySelector(".modal-container");

button.addEventListener('click', () => {
    document.body.appendChild(container);
})

container.addEventListener("click", (ev) => {
    if (ev.target.classList.contains("modal-container")) {
        document.body.removeChild(container);
    }
})
