$("#submit").click(function(){
    grabData();
})

function grabData(){
    var name = $("#name").val();
    $.ajax({
        url:"http://www.omdbapi.com/?t="+name,
        success:function(result){
            console.log(result);
        }
    })
}

function print(obj){
    $('#content').text('');
    $('#poster').text('');
    for(var prop in obj){
        if (prop!="Poster"){
            $('#content').append('<p>'+prop+': '+obj[prop]+'</p>');
        }
        if (prop=="Poster"){
            $('#poster').append('<img src="'+obj[prop]+'">');
        }
    }
}

$('#submit').click(function(){
    grabData();
})