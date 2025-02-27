
let mode = "close";

function toggle(){
    const menu = document.getElementById("menu-bar")
    if(mode == "close"){
        
        mode="open"
        menu.style.display="block";
    }
    else{
        mode="close"
        menu.style.display="none";
    }
}