const registerForm = document.querySelector(".register-form");

const registerUsernameInput = registerForm.querySelector("#username");
const registerPasswordInput = registerForm.querySelector("#password");
const registerFullnameInput = registerForm.querySelector("#fullname");
const registerEmailInput = registerForm.querySelector("#email");

const registerSubmitButton = registerForm.querySelector("#submit");

const checkIsFilled = (input) => {
    if (input.value.length > 0) {
        return true;
    } else {
        return false;
    }
}

const fields = [registerUsernameInput, registerPasswordInput, registerFullnameInput, registerEmailInput];

registerForm.addEventListener('keyup', event => {
    const allFieldsFilled = fields.every(checkIsFilled);

    if (allFieldsFilled) {
        registerSubmitButton.disabled = false;
    } else {
        registerSubmitButton.disabled = true;

    }
});