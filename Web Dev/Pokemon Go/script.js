var url="http://maps.googleapis.com/maps/api/staticmap?center=Pier+A+Harbor+House,+Battery+Place,+New+York,+NY&zoom=17&scale=1&size=600x400&maptype=satellite&format=png&visual_refresh=true";

pokemon = ["http://cdn.bulbagarden.net/upload/e/e9/Spr_3f_004.png","http://pldh.net/media/pokemon/gen3/rusa/001.png","http://media-cerulean.cursecdn.com/avatars/238/38/7.png.png","http://media-cerulean.cursecdn.com/avatars/238/344/16.png.png","http://i1205.photobucket.com/albums/bb432/dontbeamahoushoujo/019rattata.png","http://cdn.bulbagarden.net/upload/3/35/Spr_3f_021.png","http://cdn.bulbagarden.net/upload/4/44/Spr_3e_013.png","http://vignette2.wikia.nocookie.net/pokemon/images/1/17/Caterpie_BW.gif/revision/latest?cb=20120627233636"];
pokerandom = [];

for (i=0; i<8; i++){
    var poke = Math.floor(Math.random() * (8));
    locrandomx = (Math.random() * (40.706222 - 40.703615) + 40.703615).toFixed(8);
    locrandomy = (Math.random() * (-74.018795 - -74.013566) + -74.013566).toFixed(8);
    pokerandom.push("&markers=icon:"+pokemon[poke]+"%7Cshadow:true%7C"+locrandomx+", "+locrandomy);
    url = url+pokerandom[i];
}

encodeURI(url);

var htmlIMG=document.createElement("img");
$("body").append(htmlIMG);
$("img").attr("src", url);