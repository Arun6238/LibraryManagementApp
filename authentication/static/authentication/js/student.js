function showTable(){
    document.getElementById("requested-books-table").style.display = "table"
    document.getElementById("open").style.display = "none"
    document.getElementById("close").style.display = "inline"

}

function closeTable(){
    document.getElementById("requested-books-table").style.display = "none"
    document.getElementById("close").style.display = "none"
    document.getElementById("open").style.display = "inline"
}

function showViewTable(){
    document.getElementById("issued-book-table").style.display = "table"
    document.getElementById("open-issued-book").style.display = "none"
    document.getElementById("close-issued-book").style.display = "inline"
}
function closeViewTable(){
    document.getElementById("issued-book-table").style.display = "none"
    document.getElementById("open-issued-book").style.display = "inline"
    document.getElementById("close-issued-book").style.display = "none"
}
function closePasswordMessage(){
    console.log("clicked")
    document.getElementById("Msg").style.display = "none"
    document.getElementById("msgp").style.display = "none"
}
function closePasswordMessage2(){
    console.log("clicked")
    document.getElementById("Msg2").style.display = "none"
    document.getElementById("msgp2").style.display = "none"
}
function closeValidateMsg(){
    document.getElementById("validateMessage").style.display = "none"
}
function validateChangePassoword(){
    let passw = document.getElementById("new_pass").value
    let confPassw = document.getElementById("conf_new_pass").value

    let validatePass = false
    if (passw.length>=8)
    {
        if(passw == confPassw){
            document.forms["changePasswordForm"].submit();
        }
        else{
            document.getElementById("validateMessage").style.display = "flex"
            document.getElementById("conf_new_pass").style.borderColor = "red"
            document.getElementById("conf_new_pass").style.backgroundColor = "#ffc4c4"
            document.getElementById("msg2").innerHTML = "Please enter the same password"
        }
    }
    else{
        document.getElementById("validateMessage").style.display = "flex"
        document.getElementById("msg2").innerHTML = "Password must contain minimum 8 charecters"
        document.getElementById("conf_new_pass").style.borderColor = "red"
        document.getElementById("conf_new_pass").style.backgroundColor = "#ffc4c4"
        document.getElementById("new_pass").style.borderColor = "red"
        document.getElementById("new_pass").style.backgroundColor = "#ffc4c4"
    }
}