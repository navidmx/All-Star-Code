$('#submit').click(function(){
    grabData();
})
function grabData(){
    var name=$('#name').val();
    $.ajax({
        type: "GET",
        dataType: "JSON ",
        url: 'http://cors.io/?u=https://api-explorer.khanacademy.org/api/v1/'+name+'/videos',
        success: function(result){
            print(result);
        }
    })
}
function print(object){
    $('#content').text('');
    $('#content').append('<p>'+"Link"+': '+object.youtube_id+'</p>');
}


$('#submit').click(function(){
    grabData();
})