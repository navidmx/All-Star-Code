var url="http://maps.googleapis.com/maps/api/staticmap?center=Pier+A+Harbor+House,+Battery+Place,+New+York,+NY&zoom=17&scale=1&size=600x400&maptype=satellite&format=png&visual_refresh=true";

pokemon = ["http://pwo-wiki.info/images/thumb/7/77/Pikachu.png/64px-Pikachu.png","http://cdn.bulbagarden.net/upload/e/e9/Spr_3f_004.png","http://pldh.net/media/pokemon/gen3/rusa/001.png","http://orig12.deviantart.net/8024/f/2015/183/5/9/leader_of_the_squirtle_squad_by_merry255-d8zow49.gif"];
var loc = ["Pier A Harbor House, Battery Place, New York, NY", "36 Battery Pl, New York, NY 10280", "20 Battery Pl, New York, NY 10004", "2 Washington St, New York, NY 10004"];
var poke = Math.floor(Math.random()*4);
var locrandom = Math.floor(Math.random()*4);

url = url+"&markers=icon:"+pokemon[poke]+"%7Cshadow:true%7C"+loc[locrandom];
encodeURI(url);

var htmlIMG=document.createElement("img");
$("body").append(htmlIMG);
$("img").attr("src", url);