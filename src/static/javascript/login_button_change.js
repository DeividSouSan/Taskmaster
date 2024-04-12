const loginForm = document.querySelector(".login-form");
const loginUsernameInput = loginForm.querySelector("#username");
const loginPasswordInput = loginForm.querySelector("#password");
const loginSubmitButton = loginForm.querySelector("#submit");

loginUsernameInput.addEventListener('keyup', event => {
    const allFieldsFilled = loginUsernameInput.value.length > 0 && loginPasswordInput.value.length > 0;

    if (allFieldsFilled) {
        loginSubmitButton.disabled = false;

    } else {
        loginSubmitButton.disabled = true;

    }
});

loginPasswordInput.addEventListener('keyup', event => {
    const allFieldsFilled = loginUsernameInput.value.length > 0 && loginPasswordInput.value.length > 0

    if (allFieldsFilled) {
        loginSubmitButton.disabled = false;
    } else {
        loginSubmitButton.disabled = true;

    }
});
