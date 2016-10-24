var charX = 50;
var charY = 300;
var charColTL, charColTR, charColBL, charColBR, wallCol, finishCol, charStartX, charStartY, level;

function setup() {
    var canvas = createCanvas(600,600);
    canvas.parent('sketch'); //This isn't necessary, but would be a neat tool to teach students, as it is very helpful for formatting in websites.
    level = 1; //Sets the first level to 1
}

function draw() {
    //Draws the board, reason for a rectangle shape rather than background(0) is to use stroke, which is necessary for collision test.
    fill(0);
    rect(0,0,600,600);
    //Runs move function, making sure the character moves accordingly on every keypress.
    move();
    checkLevel(); //Draws up the level (1-3)
    //Draws the red character
    noStroke();
    fill(255,0,0);
    ellipse(charX, charY, 30, 30);
    //Runs collision test through every loop
    collisionTest();
}

function levelOne(){ //Draws level one
    //Sets starting position when character hits wall.
    charStartX = 50;
    charStartY = 300;
    //Draws wall using color 225, for collision tests.
    noStroke();
    fill(225);
    rect(0,0,600,250);
    rect(0,350,600,250);
    //Draws the finish line, with RGB 45, 170, 223 for collision tests.
    fill(45,170,223);
    rect(520,275,50,50);
}

function levelTwo(){
    charStartX = 300;
    charStartY = 50;
    noStroke();
    fill(225);
    rect(0,0,50,600);
    rect(550,0,50,600);
    rect(0,100,450,50);
    rect(150,250,450,50);
    rect(0,400,450,50);
    fill(45,170,223);
    rect(275,500,50,50);
}

function levelThree(){
    charStartX = 50;
    charStartY = 50;
    noStroke();
    fill(225);
    ellipse(300,300,300,300);
    ellipse(500,100,80,80);
    ellipse(100,500,80,80);
    ellipse(75,300,40,40);
    ellipse(300,75,40,40);
    ellipse(525,300,50,50);
    ellipse(300,525,50,50);
    fill(45,170,223);
    rect(525,525,50,50);
}

function win(){
    noLoop();
    //Adds some punny, exciting and motivational text to announce that the player has won.
    $("h4").text("You win!");
    $("h4").css("color","green");
    $("h3").text("Now that, was a-maze-ing!");
    $("#button").text("Click here to do it again: ")
    //Creates a button when the game is won, which resets the game on click.
    if($("button").length==0){
    $("#button").append(document.createElement("button"));
    var resetButton = $("button");
    resetButton.text("Restart!");
    resetButton.click(function(){
    //On click, resets the characters location to the original, refreshes the text that displays the level, sets the level back to 1, and removes the button.
      charX=50;
      charY=300;
      level=1;
      $("h4").text(level);
      $("h4").css("color","black");
      $("h3").text("Current Level:");
      $("#button").text("")
      loop();
      resetButton.remove();
    })
    }
}

function collisionTest(){
    //The color "225" is set to the border.
    stroke(225);
    strokeWeight(5);
    //Since the top left corner of the canvas will always be the border, guarantees that no matter what border you decide on, the "wallCol" variable is set to that on collision.
    wallCol = get(0, 0);
    //Sets the RGB array of the finish line colors.
    finishCol = [45, 170, 223];
    charColTL = get(charX-15,charY-15); //Takes color at top left of character
    charColTR = get(charX+15,charY-15); //Takes color at top right of character
    charColBL = get(charX-15,charY+15); //Takes color at bottom left of character
    charColBR = get(charX+15,charY+15); //Takes color at bottom right of character
    //Collision test for walls - tests all four corners of the character, to see if they match with the designated wall color. If so, returns the character to that level's starting position.
    if (charColTL[1] == wallCol[1] || charColTR[1] == wallCol[1] || charColBL[1] == wallCol[1] || charColBR[1] == wallCol[1]){
        charX=charStartX;
        charY=charStartY;
    }
    //Collision test for finish line - tests all four corners of the character, to see if they match with the designated finish color. If so, runs nextLevel(), which advances the game to the next level, and sets it to the new starting position.
    if (charColTL[1] == finishCol[1] || charColTR[1] == finishCol[1] || charColBL[1] == finishCol[1] || charColBR[1] == finishCol[1]){
        nextLevel();
        charX = charStartX;
        charY = charStartY;
    }
}

function checkLevel(){
    //Checks what level the game is on, and draws appropriate level.
    if (level == 1){
        levelOne();
    }
    if (level == 2){
        levelTwo();
    }
    if (level == 3){
        levelThree();
    }
}

function nextLevel(){
    //If game is already on Level 3 when nextLevel() is run, advances game to the win() function, ending the game. Or else, simply advances the level.
    if (level == 3){
        win();
        level = 4; //This is just to reset the board
        charX = 1000;
        charY = 1000;
    }
    else{
        level++;
        //Prints the current level to the "h4" tag in index.html
        $("h4").text(level);
    }
}

function move() {
    //Uses up/down/left/right arrows as movement
    if (keyIsDown(LEFT_ARROW)){
        charX-=3;
    }
    if (keyIsDown(RIGHT_ARROW)){
        charX+=3;
    }
    if (keyIsDown(DOWN_ARROW)){
        charY+=3;
    }
    if (keyIsDown(UP_ARROW)){
        charY-=3;
    }
}