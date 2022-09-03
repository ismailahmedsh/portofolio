
var loader=document.querySelector(".start-loader");


window.addEventListener("load",vanish)


    function vanish(){
        setTimeout(function() { loader.classList.add("disappear"); }, 500);
        window.scrollTo(0,0);
    }

