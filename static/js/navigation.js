function active() {
    pathname = window.location.pathname;
    pathname = pathname.replace("/","");
    if (pathname === "") {
        pathname = "index";
    }
    var a = document.getElementById(pathname);
    if (a.className === "menuitems") {
        a.className += " active";
    }
}
active();
function responsive() {
    var x = document.getElementById("Topnav");
    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
}

window.addEventListener("load", () => {
    if (!document.getElementById('progress')) {
        var progressBar = document.createElement('div');
        progressBar.id = 'progress';
        var bElement = document.createElement('b');
        var iElement = document.createElement('i');
        progressBar.appendChild(bElement);
        progressBar.appendChild(iElement);
        document.getElementById('loader').appendChild(progressBar);
        setTimeout(function() {
            progressBar.style.transition = 'width 3s 0s opacity 3s 3s';
            progressBar.style.width = '300%';
            progressBar.style.opacity = '0';
            setTimeout(function() {
                if (progressBar.parentNode) {
                    progressBar.parentNode.removeChild(progressBar);
                }
            }, 2000);
        }, 500);
    }
});