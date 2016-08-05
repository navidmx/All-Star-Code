var randomWord;
var responseString;
var foundTrack=0;

function RandomWord() {
    var requestStr = "http://randomword.setgetgo.com/get.php";
    $.ajax({
        type: "GET",
        url: requestStr,
        dataType: "jsonp",
        jsonpCallback: 'RandomWordComplete'
    });
}

$("#submit").click(function(){
    RandomWord();
})

function RandomWordComplete(data) {
    randomWord=data.Word;
}

function httpGet(){
    if (window.XMLHttpRequest)
    {// code for IE7+, Firefox, Chrome, Opera, Safari
       xmlhttp=new XMLHttpRequest();
    }
    else
    {// code for IE6, IE5
       xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }
    xmlhttp.onreadystatechange=function()
    {
       if (xmlhttp.readyState==4 && xmlhttp.status==200)
       {
           responseString = xmlhttp.response;
           checkList(responseString);
       }
    }
    xmlhttp.open("GET", "https://api.spotify.com/v1/search?q="+randomWord+"&type=track", false );
    var albumLink=xmlhttp;
   
    xmlhttp.send();
}
httpGet();

function checkList(obj){
    obj = obj.split(" ");
    for (var item in obj){
        if (obj[item-2]=='"spotify"' && foundTrack<3){
            foundTrack+=1;
            if (foundTrack==3){
                console.log(obj[item]);
            }
        }
    }  
}