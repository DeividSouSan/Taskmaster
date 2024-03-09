
/* Botão de adicionar tarefa */

var addTaskButton = document.querySelector(".add-task-button");

const taskFormTemplate = document.querySelector(".add-task-template");
const taskFormModal = taskFormTemplate.content.cloneNode(true);
const taskFormContainer = taskFormModal.querySelector(".modal-container");

addTaskButton.addEventListener('click', () => {
    document.body.appendChild(taskFormContainer);
})

taskFormContainer.addEventListener("click", (ev) => {
    if (ev.target.classList.contains("modal-container")) {
        document.body.removeChild(taskFormContainer);
    }
})

/* Botão de opções do menu */

const accountButton = document.querySelector(".account-button");
const floatingMenu = document.querySelector(".floating-menu");
const headerAfterAuth = document.querySelector(".header-after-auth");
accountButton.addEventListener('click', () => {
    headerAfterAuth.appendChild(floatingMenu);
    floatingMenu.style.display = "block";
});

