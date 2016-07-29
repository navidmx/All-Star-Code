var ellipseX, ellipseY;
var ballR, ballG, ballB;
var color;
var pixelW, pixelS, pixelA, pixelD;

function setup(){
    createCanvas(500,500);
    ellipseX=25;
    ellipseY=25;
    color=2;
    noStroke();
}

function keyPressed(){
    if (key=="w"){
        ellipseY-=2;
        pixelW=get(ellipseX,ellipseY-15);
    }
    if (key==="s"){
        ellipseY+=2;
        pixelS=get(ellipseX,ellipseY+15);
    }
    if (key==="a"){
        ellipseX-=2;
        pixelA=get(ellipseX-15,ellipseY);
    }
    if (key==="d"){
        ellipseX+=2;
        pixelD=get(ellipseX+15,ellipseY)
    }
}

function ballColor(){
    if (color==1){
        ballR=255;
        ballG=255;
        ballB=255;
    } //White
    if (color==2){
        ballR=255;
        ballG=0;
        ballB=0;
    } //Red
    if (color==3){
        ballR=0;
        ballG=0;
        ballB=255;
    } //Blue
    if (color==4){
        ballR=0;
        ballG=255;
        ballB=0;
    } //Green
}

function levelOne(){ 
    fill(255,168,232)
    rect(0,50,150,10);
    rect(140,50,10,450);
    rect(350,0,10,450);
    rect(350,440,150,10);
}

function draw(){
    background(0);
    fill(156,248,122);
    rect(450,450,50,50);
    fill(ballR, ballG, ballB);
    ellipse(ellipseX,ellipseY,30,30);
    keyPressed();
    ballColor();
    levelOne();
}