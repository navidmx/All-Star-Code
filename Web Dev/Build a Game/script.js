var bullets = [];
var timer,masterTimer;
var count,score;
var pacman,pacmanX,pacmanY;
var ghostX,ghostY,ghostSpeed;
var redGhostX,redGhostY,redGhostSpeed;
var orangeGhostX,orangeGhostY,orangeGhostSpeed;
var activeGhost = false;
var redActiveGhost = false;
var orangeActiveGhost = false;
var lose=false;
var startGame=false;
var database = firebase.database().ref();

function preload(){
    pacman=loadAnimation("http://i.imgur.com/1o2HATt.png", "http://i.imgur.com/1o2HATt.png", "http://i.imgur.com/FqKY7Gv.png", "http://i.imgur.com/FqKY7Gv.png");
    normalpacman=loadAnimation("http://i.imgur.com/1o2HATt.png");
    ghost=loadAnimation("http://i.imgur.com/2dH1SQG.png");
    redGhost=loadAnimation("http://i.imgur.com/XrA4iP3.png");
    orangeGhost=loadAnimation("http://i.imgur.com/LbXpxZw.png");
}

function setup(){
    createCanvas(600,500);
    pacmanX=100;
    pacmanY=250;
    ghostX=650;
    ghostY=50;
    redGhostX=650;
    redGhostY=50;
    orangeGhostX=650;
    orangeGhostY=50;
    ghostSpeed=4;
    redGhostSpeed=4;
    orangeGhostSpeed=4;
    timer=0;
    masterTimer=0;
    score=0;
    noStroke();
}

function keyPressed(){
    if (keyIsDown(UP_ARROW) || keyIsDown(87)){
        pacmanY-=3;
    }
    if (keyIsDown(DOWN_ARROW) || keyIsDown(83)){ 
        pacmanY+=3;
    }
    if (keyIsDown(LEFT_ARROW) || keyIsDown(65)){
        pacmanX-=3;
    }
    if (keyIsDown(RIGHT_ARROW) || keyIsDown(68)){
        pacmanX+=3;
    }
    if (startGame==true){
        if (keyIsDown(32)){ //32 = Space
            animation(pacman, pacmanX, pacmanY);
            if (timer==0){
                {
                  var temp = new Bullet(pacmanX, pacmanY);
                  bullets.push(temp);
                  count=true;
                }
            }
        }
    }
    if (startGame==false){
        if (keyIsDown(32)){
            startGame=true;
        }
    }
    else{
        animation(normalpacman, pacmanX, pacmanY);
    }
}

function Bullet (tempX, tempY) {
  this.bulletX = tempX
  this.bulletY = tempY
}

function createGhost(){
    ghostY=random(50,450);
    ghostSpeed=random(2,5);
    activeGhost=true;
}

function createOrangeGhost(){
    orangeGhostY=random(50,450);
    orangeGhostSpeed=random(3,6);
    orangeActiveGhost=true;
}

function createRedGhost(){
    redGhostY=random(50,450);
    redGhostSpeed=random(4,7);
    redActiveGhost=true;
}

function logic(){
    for (i=0; i<bullets.length; i++) {
        var bullet = bullets[i];
        bullet.bulletX += 5
        fill(255);
        ellipse(bullet.bulletX, bullet.bulletY, 12, 12);
    }
    if (count==true){
        timer+=1;
    }
    if (timer==20){
        timer = 0;
        count=false;
    }
    if (lose==false){
        if (ghostX<0){
            activeGhost=false;
            ghostX=650;
        }
        if (masterTimer>600){
            if (orangeGhostX<0){
                orangeActiveGhost=false;
                orangeGhostX=650;
            }
        }
        if (masterTimer>1200){
            if (redGhostX<0){
                redActiveGhost=false;
                redGhostX=650;
            }
        }
    }
    animation(ghost,ghostX,ghostY);
    ghostX-=ghostSpeed;
    if (masterTimer>600){
        animation(orangeGhost,orangeGhostX,orangeGhostY);
        orangeGhostX-=orangeGhostSpeed;
    }
    if (masterTimer>1200){
        animation(redGhost,redGhostX,redGhostY);
        redGhostX-=redGhostSpeed;
    }
}

function walls(){
    if (pacmanX<25){
        pacmanX+=5
    }
    if (pacmanX>575){
        pacmanX-=5
    }
    if (pacmanY<25){
        pacmanY+=5
    }
    if (pacmanY>475){
        pacmanY-=5
    }  
}

function ghostCollision(){
    for (i=0; i<bullets.length; i++) {
        var bullet = bullets[i];
        if (bullet.bulletX > ghostX-20 && bullet.bulletX < ghostX+20 && bullet.bulletY > ghostY-20 && bullet.bulletY < ghostY+25){
            score+=1;
            ghostX=650;
            activeGhost=false;
        }
        if (bullet.bulletX > orangeGhostX-20 && bullet.bulletX < orangeGhostX+20 && bullet.bulletY > orangeGhostY-20 && bullet.bulletY < orangeGhostY+25){
            score+=1;
            orangeGhostX=650;
            orangeActiveGhost=false;
        }
        if (bullet.bulletX > redGhostX-20 && bullet.bulletX < redGhostX+20 && bullet.bulletY > redGhostY-20 && bullet.bulletY < redGhostY+25){
            score+=1;
            redGhostX=650;
            redActiveGhost=false;
        }
    }
    if (pacmanX > ghostX-20 && pacmanX < ghostX+20 && pacmanY > ghostY-20 && pacmanY < ghostY+25){
        lose=true;
    }
    if (pacmanX > orangeGhostX-20 && pacmanX < orangeGhostX+20 && pacmanY > orangeGhostY-20 && pacmanY < orangeGhostY+25){
        lose=true;
    }
    if (pacmanX > redGhostX-20 && pacmanX < redGhostX+20 && pacmanY > redGhostY-20 && pacmanY < redGhostY+25){
        lose=true;
    }
}

function draw(){
    background(0);
    keyPressed();
    if (startGame==false){
        fill(255);
        textAlign(CENTER);
        textSize(32);
        text("PACMAN FIGHTS BACK", 300, 100)
        textSize(24);
        text("Click space to start", 300, 140)
    }
    if (startGame==true){
        logic();
        walls();
        ghostCollision();
        masterTimer+=1;
        if (lose==false){
            if (activeGhost==false){
                createGhost();
            }
            if (masterTimer>600){
                if (orangeActiveGhost==false){
                    createOrangeGhost();
                }
            }
            if (masterTimer>1200){
                if (redActiveGhost==false){
                    createRedGhost();
                }
            }
            fill(255,255,0);
            textSize(18);
            text("SCORE: "+score, 475, 50);
        }
        if (lose==true){
            textAlign(CENTER);
            fill(255,255,0);
            textSize(36);
            text("YOU LOSE :(", 300, 250);
            pacmanX=1000;
            fill(255);
            textSize(24);
            text("Final Score: "+score, 300, 285);
        }
    }
}

function sendPoints(){
    var name = $('#name').val();
    var points = score;
    database.push({
        'name':name,
        'points':points,
    });
}

database.orderByChild("points").limitToLast(5).on('child_added',function(dataRow){
    var row = dataRow.val();
    $("#highScores").append("<h3>"+": "+row.name+" - "+row.points+"</h3>");
    })
