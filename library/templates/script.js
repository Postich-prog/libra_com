const form  = document.getElementsByTagName('form')[0];
                    
const email = document.getElementById('mail');
const name = document.getElementById('name');
const emailError = document.querySelector('#mail + span.error');
const nameError = document.querySelector('#name + span.error');

email.addEventListener('input', function (event) {
  // Each time the user types something, we check if the
  // form fields are valid.

  if (email.validity.valid) {
    // In case there is an error message visible, if the field
    // is valid, we remove the error message.
    emailError.innerHTML = ''; // Reset the content of the message
    emailError.className = 'error'; // Reset the visual state of the message
  } else {
    // If there is still an error, show the correct error
    showError();
  }
});

name.addEventListener('input', function (event) {
  // Each time the user types something, we check if the
  // form fields are valid.

  if (name.validity.valid) {
    // In case there is an error message visible, if the field
    // is valid, we remove the error message.
    nameError.innerHTML = ''; // Reset the content of the message
    nameError.className = 'error'; // Reset the visual state of the message
  } else {
    // If there is still an error, show the correct error
    showErrorName();
  }
});

form.addEventListener('submit', function (event) {
  // if the form contains valid data, we let it submit

  if(!email.validity.valid) {
    // If it isn't, we display an appropriate error message
    showError();
    // Then we prevent the form from being sent by canceling the event
    event.preventDefault();
  }
  if(!name.validity.valid) {
    // If it isn't, we display an appropriate error message
    showErrorName();
    // Then we prevent the form from being sent by canceling the event
    event.preventDefault();
  }
});

function showError() {
  if(email.validity.valueMissing) {
    // If the field is empty
    // display the following error message.
    emailError.textContent = 'Нужно ввести адрес электронной почты.';
  } else if(email.validity.typeMismatch) {
    // If the field doesn't contain an email address
    // display the following error message.
    emailError.textContent = 'Это не похоже на почту :(';
  } else if(email.validity.tooShort) {
    // If the data is too short
    // display the following error message.
    emailError.textContent = `Почта должна содержать минимум ${ email.minLength } символов; вы ввели ${ email.value.length }.`;
  }
  // Set the styling appropriately
  emailError.className = 'error active';
}

function showErrorName() {
    if(name.validity.valueMissing) {
        // If the field is empty
        // display the following error message.
        nameError.textContent = 'Нужно ввести имя.';
      } else if(name.validity.tooShort) {
        // If the data is too short
        // display the following error message.
        nameError.textContent = `Имя должно содержать минимум ${ name.minLength } символов; вы ввели ${ name.value.length }.`;
      } else if(!validateName(name)) {
        nameError.textContent = 'Неверный формат';
      }
      // Set the styling appropriately
      nameError.className = 'error active';
}

function validateName(name){
  var nameRegex = /^[А-Я][^А-Я]*$/;
  return nameRegex.test(String(name));
}