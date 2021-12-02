function GetPasswordFromDatabase(inputLogin) {
    //Давай сделаем вид, что это реальный запрос в базу данных, а не работа со спискои JSON'ов
    database = [{login: "login", password: "password"},
            {login: "login1", password: "password2"}]
    for (indexOfUser = 0; indexOfUser < database.length; indexOfUser++){
        if (database[indexOfUser].login === inputLogin){
            return database[indexOfUser].password;
        }
    }
    throw "NotFound";
}

function ClearInputFields(){
    document.getElementById("login-form").reset();}



function isRightData(login, password) {
    try{
        return (password === GetPasswordFromDatabase(login));
    }
    catch(exception) {
        return false;
    }
}

function CheckForCorrectData(){
    loginInputData = document.getElementById('login-input').value;
    passwordInputData = document.getElementById('password-input').value;
    if (isRightData(loginInputData, passwordInputData)) {
        window.location.href = "./../main-content-page/landing.html";
    }else{
        ClearInputFields();
        alert(document.getElementById("login-input").value + " is not a valid login")

    }
    
}  