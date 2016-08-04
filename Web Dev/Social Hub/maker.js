var makerURL="https://maker.ifttt.com/trigger/receive/with/key/bca0JCyikAT23ZXM7ujUOV";

function submitIt(){
    var message=$("#message").val();
    var img=$("#imgURL").val();
    var sendoff={
        "value1":message,
        "value2":img,
    }
    $.post(makerURL,sendoff);
    
    $("#message").val("");
    $("#imgURL").val("");
}