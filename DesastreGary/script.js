if('serviceWorker' in navigator){
    navigator.serviceWorker.register('./sw.js')
    .then(reg => console.log('Registro exitoso', reg))
    .catch(err => console.warn('Error de registro', err))
}

const nav = document.getElementById('navlist');
function toggleNav () {       

    if ( nav.style.display === "" )
    nav.style.display = "block";
    else
    nav.style.display = "";
}


function windowResizeHandler () {
    if ( screen.width > 800 )
    nav.style.display = "";
}

window.addEventListener("resize", windowResizeHandler);
