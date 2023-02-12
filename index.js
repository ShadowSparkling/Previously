//CONSTANTS  & Variables
let direction = {x:0,y:0};
// const foodSound = new Audio('food.mp3');
// const gameOverSound = new Audio('gameover.mp3');
// const moveSound = new Audio('move.mp3');
// const musicSound = new Audio('music.mp3');
let speed =2;
let lastPaintTime = 0;
let snakeArr = [
    {x: 13, y: 15}
]
let food = {x:14,y:15};



//Game Functions
function main(ctime){
    window.requestAnimationFrame(main);
    if((ctime-lastPaintTime)/1000 <1/speed){
        return;
    }
    lastPaintTime = ctime;
    gameEngine();

}

function gameEngine(){
    // Part 1: Updating the snake array & food.

    // Part 2 : Display the snake and food.

    //Display the snake
    board.innerHTML = "";
    snakeArr.forEach((e,index)=>{
        snakeELement = document.createElement('div');
        snakeElement.style.gridRowStart= e.y;
        snakeElement.style.gridColumnStart= e.x;
        if(index===0){
        snakeElement.classList.add('head');}
        snakeElement.classList.add('snake');
        board.appendChild(snakeElement);
    });
    //Display the food
        foodELement = document.createElement('div');
        foodElement.style.gridRowStart= food.y;
        foodElement.style.gridColumnStart= food.x;
        foodElement.classList.add('food');
        board.appendChild(foodElement);
    }










//Main Logic starts here
window.requestAnimationFrame(main);
window.addEventListener('keydown', e=>{
    inputDir = {x: 0, y: 1} //Start the game
    movesound.play();
    switch (e.key) {
        case "ArrowUp":
            console.log("ArrowUp")
            break;
        case "ArrowDown":
            console.log("ArrowDown")
            break;
        case "ArrrowLeft":
            console.log("ArrowLeft")
            break;
        case "ArrowRight":
            console.log("ArrowRight")
            break;
    
        default:
            break;
    }
})
