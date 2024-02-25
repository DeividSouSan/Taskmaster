
const template = document.querySelector(".add-task-template");

const addTaskModal = template.content.cloneNode(true);



var addTaskButton = document.querySelector(".add-task-button");

addTaskButton.addEventListener('click', () => {
    document.body.appendChild(addTaskModal)
})