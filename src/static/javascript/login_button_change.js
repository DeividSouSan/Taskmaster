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