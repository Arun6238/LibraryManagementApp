function showPassword(){
    let inp = document.querySelector("#password")
    if(inp.type =="password"){
        inp.type = "text";
        console.log(inp.type)
    }
    else{
        inp.type = "password"
        console.log(inp.type)
    }
}
function registervalidation(){
    let inpPass = document.querySelector('#regPass')
    let inpConfPass = document.querySelector('#regConfPass')
    let msg = document.querySelector(".message")
    if (inpPass.value == inpConfPass.value){
        return true
    }
    else {
        msg.classList.remove("hide")
        inpPass.style.backgroundColor = "rgb(255, 157, 157)"
        inpPass.style.borderColor = "crimson"
        inpConfPass.style.backgroundColor = "rgb(255, 157, 157)"
        inpConfPass.style.borderColor = "crimson"
        msg.innerText = "The password  does not match."
        return false
    }
}

window.addEventListener('load',function(){
    let inp = document.querySelector("#regUsername")
    let msg = document.querySelector(".message")
    if(msg.innerText== "username name is already taken.."){
        inp.style.backgroundColor = "rgb(255, 157, 157)"
        inp.style.borderColor = "crimson"
    }
})
