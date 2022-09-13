const Texts = [
    'HTML', 'CSS', 'JAVASCRIPT',
    'AutoCAD', 'SolidWorks', 'Inventor',
    'Arduino', 'MATLAB',
    'C LANG','Microsoft Office','ERP systems','LabView'
];
    let y=0;
    var windowWidth = window.innerWidth;
    if(windowWidth > 1100){
        y = 350;
    }
    else if(850 < windowWidth && windowWidth <= 1100){
        y = 300;
    }
    else if(600 < windowWidth && windowWidth <= 850){
        y = 275;
    }
    else if(400 < windowWidth && windowWidth <= 600){
        y = 250;
    }
    else if(300 < windowWidth && windowWidth <= 400){
        y = 200;
    }
    else{
        y = 150;
    }

var tagCloud = TagCloud('.Sphere', Texts, {

    // Sphere radius in px
    radius:y,
    // animation speed
    // slow, normal, fast
    maxSpeed: 'fast',
    initSpeed: 'fast',

    // Rolling direction [0 (top) , 90 (left), 135 (right-bottom)] 
    direction: 135,

    // interaction with mouse or not [Default true (decelerate to rolling init speed, and keep rolling with mouse).]
    keep: true

});

// Giving color to each text in sphere
var color = '#FFF';
document.querySelector('.Sphere').style.color = color;