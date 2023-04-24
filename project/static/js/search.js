function check(form){
    if(form.name.value == "osama"){
        press();
    }
    else{
       
        alert("invalid input.");
    }
}
function press(){
    document.getElementById('p').style.display = "block";
}