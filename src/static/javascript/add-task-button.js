var taskModalButton = document.querySelector(".task-modal-button");

const taskModalTemplate = document.querySelector(".task-modal-template");
const taskModal = taskModalTemplate.content.cloneNode(true);
const taskModalContainer = taskModal.querySelector(".task-modal-window");


// Botão do modal adiciona o formulário de tarefa
taskModalButton.addEventListener('click', () => {
    document.body.appendChild(taskModalContainer);
})

// Fecha o modal ao clicar fora do formulário
taskModalContainer.addEventListener("click", (ev) => {
    if (ev.target.classList.contains("task-modal-window")) {
        document.body.removeChild(taskModalContainer);
    }
})