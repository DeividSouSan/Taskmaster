const loginForm = document.querySelector(".login-form");

const loginUsernameInput = loginForm.querySelector("#username");
const loginPasswordInput = loginForm.querySelector("#password");

const loginSubmitButton = loginForm.querySelector("#submit");

const checkIsFilled = (input) => {
    if (input.value.length > 0) {
        return true;
    } else {
        return false;
    }
}

const fields = [loginUsernameInput, loginPasswordInput];

loginForm.addEventListener('keyup', event => {
    const allFieldsFilled = fields.every(checkIsFilled);

    if (allFieldsFilled) {
        loginSubmitButton.disabled = false;
    } else {
        loginSubmitButton.disabled = true;
    }
});

<<<<<<< HEAD
loginPasswordInput.addEventListener('keyup', event => {
    const allFieldsFilled = loginUsernameInput.value.length > 0 && loginPasswordInput.value.length > 0

    if (allFieldsFilled) {
        loginSubmitButton.disabled = false;
    } else {
        loginSubmitButton.disabled = true;

    }
});
=======
>>>>>>> d306b2048c9997f3e9c6138c6940b73145bdfa1a
