var addTaskButton = document.querySelector(".add-task-button");

const addModalWindow = document.querySelector(".add-modal-window");
const taskForm = document.querySelector("#add-form")

// Botão do modal adiciona o formulário de tarefa
addTaskButton.addEventListener('click', () => {
    taskForm.reset()
    addModalWindow.style.display = "block";
})

// Fecha o modal ao clicar fora do formulário
addModalWindow.addEventListener("click", (ev) => {
    if (ev.target.classList.contains("add-modal-window")) {
        addModalWindow.style.display = "none";
    }
})

const addSubmitBtn = document.querySelector(".add-task-submit");

addSubmitBtn.addEventListener("click", () => {
    addModalWindow.style.display = "none";
});
