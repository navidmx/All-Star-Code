var clickTime
var score = 0

function setup() {
    createCanvas(610,710)
}

function draw() {
    fill(255)
    rect(0,610,600,30)
    var grid = []
    var mole = []
        for (var x = 0; x < 6; x += 1){
            grid[x]=0
            mole[x]=0
            for (var y = 0; y < 6; y += 1){
                 //This is one of the only lines that may be a bit complex for students, it should either be given directly or as a hint. There are probably other ways of achieving the same goal, this just seemed easiest.
                    rand=round(random(10))
                    grid[x][y]=0
                    mole[x][y]=0
                    if (rand==0){
                            mole[x]=1
                            mole[y]=1
                        }
                    }
                    if (grid[x]==0 || grid[y]==0){
                        fill(76,153,0)
                        rect((x*100),(y*100),100,100)
                    }
                    if (mole[x]==1 && mole[y]==1){
                        fill(102,51,0)
                        rect((x*100),(y*100),100,100)
                }
            fill(0)
            textSize(16)
            text("Score = "+score,20,630)
        }
    }
}