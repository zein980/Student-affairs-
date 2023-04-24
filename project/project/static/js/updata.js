function checkForm(form)
{
    var letters = /^[A-Za-z ]+$/;
    if( form.name.value == "")
    {
        alert("Name is required.");
        form.name.focus();
        return false;
    }
    else if (!(form.name.value.match(letters))) {
        alert("Invalid Name.");
        form.name.focus();
        return false;
    }

    

    if(form.email.value == "")
    {
        alert("Email is required.");
        form.email.focus();
        return false;
    }


    var phoneno = /^\d{10}$/;
    if(form.phone.value == "")
    {
            alert("Phone is required.");
            form.phone.focus();
            return false; 
    }
    else if (!(form.phone.value.match(phoneno))) {
        alert("Invalid Phone.. number of digits must be 10.");
        form.phone.focus();
        return false;        
    }

    if( form.id.value == "")
    {
        alert("ID is required");
        form.id.focus();
        return false;
    }
    else if (!(form.id.value.match(/^\d+/))) {
        alert("Invalid ID.");
        form.id.focus();
        return false;       
    }


    if(form.level.value == "")
    {
        alert("Please, select level.");
        form.level.focus();
        return false;
    }

    if(form.gpa.value == "")
    {
        alert("GPA is required.");
        form.gpa.focus();
        return false;
    }

    if(form.date.value == "")
    {
        alert("Date is required.");
        form.date.focus();
        return false;
    }
    
    var option=document.getElementsByName('gender');
     
    if (!(option[0].checked || option[1].checked)) {
        alert("Please, Select student Gender.");
        return false;
    }

    var option=document.getElementsByName('Status');
     
    if (!(option[0].checked || option[1].checked)) {
        alert("Please, Select student Status.");
        return false;
    }
    else{
        alert("Update is done");
        return true;
    }
}