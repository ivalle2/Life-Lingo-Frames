const wrapper = document.querySelector('.wrapper');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');
const btnPopup = document.querySelector('.try-but');
const iconClose = document.querySelector('.icon-close');

document.getElementById('try-now').addEventListener('click', function() {
    window.location.href = 'try-now.html';
});

document.getElementById('try-now2').addEventListener('click', function() {
    window.location.href = 'try-now.html';
});

registerLink.addEventListener('click', ()=> {
    wrapper.classList.add('active');
});

loginLink.addEventListener('click', ()=> {
    wrapper.classList.remove('active');
});

btnPopup.addEventListener('click', ()=> {
    wrapper.classList.add('active-popup');
});

iconClose.addEventListener('click', ()=> {
    wrapper.classList.remove('active-popup');
});