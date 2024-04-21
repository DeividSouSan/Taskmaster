/* Confimração de Excluir a Task (Task Delegation Technique)

Quando você adiciona um evento de clique ao documento, esse evento é acionado sempre que um clique é feito em qualquer lugar do documento. Isso é chamado de propagação de eventos, onde um evento começa no elemento mais interno (o alvo do evento) e então se propaga para cima na árvore do DOM.

Se você atribuir o evento de clique diretamente ao botão, o evento será perdido sempre que o botão for re-renderizado pelo HTMX, porque o HTMX substitui o elemento do botão no DOM, e o novo botão não terá o evento de clique anexado a ele.

Portanto, ao adicionar o evento de clique ao documento e verificar se o alvo do evento é um botão de exclusão, você garante que o evento de clique funcione corretamente, mesmo após re-renderizações do HTMX. Isso é conhecido como delegação de eventos.
*/


const taskWrapper = document.querySelector(".task-wrapper");
taskWrapper.addEventListener('click', event => {
    if (event.target.matches('.task-config-btn')) {

        const taskHeader = event.target.parentElement;
        const task = taskHeader.parentElement;

        const configSection = task.querySelector(".task-config");
        configSection.style.display = "block";

        const cancelActionBtn = configSection.querySelector(".cancel-action-btn");
        cancelActionBtn.addEventListener('click', () => {
            configSection.style.display = "none";
        });

        const editModalWindow = document.querySelector(".edit-modal-window");

        const editTaskBtn = configSection.querySelector('.edit-task-btn');
        editTaskBtn.addEventListener('click', () => {
            editModalWindow.style.display = "block";
        });
    }
});

document.addEventListener('click', event => {
    if (event.target.classList.contains("edit-modal-window")) {
        editModalWindow.style.display = "none";
    }

    if (event.target.classList.contains("update-task-submit")) {
        editModalWindow.style.display = "none";
    }
});
