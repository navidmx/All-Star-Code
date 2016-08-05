var database = firebase.database().ref();

function sendMessage(){
    var name = $('#name').val();
    var message = $('#message').val();
    //Sending messages
    database.push({
        'name':name,
        'message':message
    });
}

database.on('child_added',function(dataRow){
    var row = dataRow.val();
    $("#messageBoard").append("<p>"+row.name+": "+row.message+"</p>");
})