function checkForm(form)
{
    var letters = /^[A-Za-z- ]+$/;
    if(!(form.name.value.match(letters)))
    {
        alert("Name is required, Invalid input.");
        form.name.focus();
        return false;
    }

    if(form.email.value == "")
    {
        alert("Email is required, Invalid input.");
        form.email.focus();
       
         return false;
    }
    var phoneno = /^\d{10}$/;
    if(!(form.phone.value.match(phoneno)) || form.phone.value == "")
    {
            alert("Phone is required, Invalid input.");
            form.phone.focus();
            return false; 
    }

    if(!(form.idst.value.match(/^\d+/)) || form.idst.value == "")
    {
        alert("ID is required, Invalid input.");
        form.idst.focus();
        return false;
    }

    if(document.form.department.selectedIndex=="")
    {
        alert ( "Please, select department!");
        form.department.focus();
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
        alert("GPA is required, Invalid input.");
        form.gpa.focus();
        return false;
    }

    if(form.date.value == "")
    {
        alert("This field is required.");
        form.date.focus();
        return false;
    }
    
    var option=document.getElementsByName('gender');
     
    if (!(option[0].checked || option[1].checked)) {
        alert("Please, Select Your Gender.");
        return false;
    }

    var option=document.getElementsByName('status');
     
    if (!(option[0].checked || option[1].checked)) {
        alert("Please, Select Your Status.");
        return false;
    }

    else{
        alert("A new student has been added successfully...");
        return true;
    }


}
