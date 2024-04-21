var addTaskButton = document.querySelector(".add-task-button");

const taskModalWindow = document.querySelector(".task-modal-window");
const taskForm = document.querySelector("#add-form")

// Botão do modal adiciona o formulário de tarefa
addTaskButton.addEventListener('click', () => {
    taskForm.reset()
    taskModalWindow.style.display = "block";
})

// Fecha o modal ao clicar fora do formulário
taskModalWindow.addEventListener("click", (ev) => {
    if (ev.target.classList.contains("task-modal-window")) {
        taskModalWindow.style.display = "none";
    }
})

const addSubmitBtn = document.querySelector(".add-task-submit");

addSubmitBtn.addEventListener("click", () => {
    taskModalWindow.style.display = "none";
});
