var url="http://maps.googleapis.com/maps/api/staticmap?"

//center=104+Lexington+Avenue&zoom=16&scale=false&size=600x300&maptype=roadmap&format=png&visual_refresh=true&markers=icon:http://vignette3.wikia.nocookie.net/pokemon/images/3/3c/Pikachu_BW.gif/revision/latest?cb=20120627233813%7Cshadow:true%7C104+Lexington+Avenue";//

var center= "104 Lexington Avenue";
var zoom= "16";
var size= "600x300";

url = url + "center=" + center + "&zoom=" + zoom + "&size=" + size;
url = encodeURI(url);

var htmlIMG=document.createElement("img");
$("body").append(htmlIMG);
$("img").attr("src", url);