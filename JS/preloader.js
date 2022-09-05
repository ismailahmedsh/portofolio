
var loader=document.querySelector(".start-loader");
var headeranimation=document.querySelector("header");
loader.classList.add("disappear");
window.addEventListener("load",vanish)

    function vanish(){
        
        setTimeout(function() { headeranimation.classList.add("header-after-animation"); },1600);
        window.scrollTo(0,0);
    }

