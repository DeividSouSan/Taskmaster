
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
const floatingMenu = document.querySelector(".floating-menu-container");
const headerAfterAuth = document.querySelector(".header-after-auth");

accountButton.addEventListener('click', () => {
    if (floatingMenu.classList.contains("active")) {
        floatingMenu.style.display = "none";
    } else {
        floatingMenu.style.display = "block";
    }
    floatingMenu.classList.toggle("active");
});

/* Confimração de Excluir a Task (Task Delegation Technique)*/

/* 
Quando você adiciona um evento de clique ao documento, esse evento é acionado sempre que um clique é feito em qualquer lugar do documento. Isso é chamado de propagação de eventos, onde um evento começa no elemento mais interno (o alvo do evento) e então se propaga para cima na árvore do DOM.

Se você atribuir o evento de clique diretamente ao botão, o evento será perdido sempre que o botão for re-renderizado pelo HTMX, porque o HTMX substitui o elemento do botão no DOM, e o novo botão não terá o evento de clique anexado a ele.

Portanto, ao adicionar o evento de clique ao documento e verificar se o alvo do evento é um botão de exclusão, você garante que o evento de clique funcione corretamente, mesmo após re-renderizações do HTMX. Isso é conhecido como delegação de eventos.
*/

const taskWrapper = document.querySelector(".task-wrapper");
taskWrapper.addEventListener('click', event => {
    if (event.target.matches('.delete-task')) {
        const taskHeader = event.target.parentElement;
        const task = taskHeader.parentElement;

        const confirmationSection = task.querySelector(".delete-task-confirm");
        confirmationSection.style.display = "block";

        const cancelDeleteTaskButton = confirmationSection.querySelector(".cancel-delete-task-button");

        cancelDeleteTaskButton.addEventListener('click', () => {
            confirmationSection.style.display = "none";
        });
    }
});


