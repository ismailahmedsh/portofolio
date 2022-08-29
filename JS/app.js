//function for Media Query menu animation
const navSlide=()=>{
    const burger= document.querySelector('.burger');
    const nav= document.querySelector('.nav-links');
    const navLinks= document.querySelectorAll('.nav-links').forEach(n => n.addEventListener('click',()=>{
        burger.classList.remove('active');
        nav.classList.remove('active');
    }));
    //toggle nav
    burger.addEventListener('click',()=>{
        burger.classList.toggle('active');
        nav.classList.toggle('active');
    });
}
navSlide();

