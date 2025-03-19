const mario = document.querySelector(".mario");
const pipe = document.querySelector(".pipe");
const clouds = document.querySelector('.clouds');

const btnRestart = document.querySelector(".restart");
const gameOver = document.querySelector('.game-over');

let loop;

const jump = (e) => {
   if (e.key === "ArrowUp") {
      if (!mario.classList.contains("jump")) {
         mario.classList.add("jump");

         setTimeout(() => {
            mario.classList.remove("jump");
         }, 500);
      }
   }
};

const resetMario = () => {
   mario.src = "./images/mario.gif";
   mario.style.width = "150px";
   mario.style.marginLeft = "0";
   mario.style.bottom = "0";
   mario.style.animation = ""
};

const resetPipe = () => {
   pipe.style.animation = "pipe-animation 1.5s infinite linear";
   pipe.style.left = "";
};

const resetClouds = () => {
   clouds.style.animation = "clouds-animation 20s infinite linear"
}

const startGame = () => {
   resetMario();
   resetPipe();
   resetClouds();

   gameOver.classList.remove("active");

   if (loop) clearInterval(loop);

   loop = setInterval(() => {
      const pipePosition = pipe.offsetLeft;
      const marioPosition = +window
         .getComputedStyle(mario)
         .bottom.replace("px", "");
      const cloudsPosition = +window.getComputedStyle(clouds).right.replace('px', '');
      
      console.log(cloudsPosition)
      if (pipePosition <= 120 && pipePosition > 0 && marioPosition <= 80) {
         pipe.style.animation = "none";
         pipe.style.left = `${pipePosition}px`;

         mario.style.animation = "death-animation 1.8s ease-out forwards";
         mario.style.bottom = `${marioPosition}px`;

         mario.src = "./images/game-over.png";
         mario.style.width = "75px";
         mario.style.marginLeft = "50px";

         clouds.style.animation = "none";
         clouds.style.right = `${cloudsPosition}px`

         clearInterval(loop);
         gameOver.classList.add("active");
      }
   }, 10);
};

btnRestart.addEventListener("click", startGame);
document.addEventListener("keydown", jump);

startGame();
