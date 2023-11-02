const wrapper=document.querySelector('.wrapper');
const loginLink=document.querySelector('.login-link');
const registerLink=document.querySelector('.register-link');
const btn=document.querySelector('.btnlogin');
const iconClose=document.querySelector('.icon-close');

registerLink.addEventListener('click',()=>{
    //console.log(wrapper.classList);
    wrapper.classList.add('active')
})

loginLink.addEventListener('click',()=>{
    //console.log(wrapper.classList);
    wrapper.classList.remove('active');
})


btn.addEventListener('click',()=>{
    //console.log(wrapper.classList);
    wrapper.classList.add('active-popup');
})

iconClose.addEventListener('click',()=>{
    //console.log(wrapper.classList);
    wrapper.classList.remove('active');
})

