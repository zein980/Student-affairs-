function confirmBox() {
    let text;
    if (confirm("Are you sure you want to delete this student") == true) {
        text = "Delete is done";
    }
    else {
        text = "Delete is canceled"
    }
    document.getElementById("confirmText").innerHTML = text;

}