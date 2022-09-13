
var loader=document.querySelector(".start-loader");
var headeranimation=document.querySelector("header");

window.addEventListener("load",vanish);

    function vanish(){
        loader.classList.add("disappear");
        setTimeout(function() { headeranimation.classList.add("header-after-animation"); },650);
    }
    window.scrollTo(0,0);
