<template>
    <div class="index-preview">
        <div class="blur blur-green blur-1"></div>
        <div class="blur blur-blue blur-2"></div>
        <div class="blur blur-blue blur-3"></div>
        <div class="game-box">
            <div class="pin top left">
                <div class="pin-inner"></div>
            </div>
            <div class="pin top right">
                <div class="pin-inner"></div>
            </div>
            <div class="pin bottom left">
                <div class="pin-inner"></div>
            </div>
            <div class="pin bottom right">
                <div class="pin-inner"></div>
            </div>

            <div class="game-box__inner">
                <div class="game-canvas">
                    <div class="game-canvas__info">
                        <div id="snake2d-text" class="text" v-if="gameOver && !gameStarted">
                            Game Over
                        </div>
                        <VueButton type="button" class="btn-primary" v-if="!gameStarted" @click="startGame">start-game
                        </VueButton>
                    </div>
                    <canvas ref="canvas" :class="{
                            'first-show': !gameInit
                        }" width="225" height="390">
                    </canvas>
                </div>
                <div class="game-info">
                    <div class="game-info__control game-info__container">
                        <span>// use keyboard<br>// arrows to play</span>

                        <div class="game-keys">
                            <div></div>
                            <div class="arrow">
                                <FontAwesomeIcon :icon="faCaretUp" />
                            </div>
                            <div></div>

                            <div class="arrow" key="ArrowLeft">
                                <FontAwesomeIcon :icon="faCaretLeft" />
                            </div>
                            <div class="arrow" key="ArrowDown">
                                <FontAwesomeIcon :icon="faCaretDown" />
                            </div>
                            <div class="arrow" key="ArrowRight">
                                <FontAwesomeIcon :icon="faCaretRight" />
                            </div>
                        </div>
                    </div>
                    <div class="game-info__container">
                        <span>// food left</span>
                        <div class="food-list">
                            <div v-for="food in foodLeft" class="food"></div>
                            <div v-for="food in foodEaten" class="food eaten"></div>
                        </div>
                    </div>
                </div>
            </div>

        </div>
    </div>
</template>

<script>
import { faCaretUp, faCaretDown, faCaretLeft, faCaretRight } from "@fortawesome/free-solid-svg-icons";
import snake2d from '@/assets/js/snake2d'


const foodLimit = 10;

export default {
    name: "Snake2DGame",


    data() {
        return {
            faCaretUp,
            faCaretLeft,
            faCaretDown,
            faCaretRight,

            foodEaten: 0,

            gameStarted: false,
            gameInit: false,
            gameOver: false,
            buttons: new Set(),
            snakeGame: null
        }
    },

    methods: {
        startGame() {
            this.gameInit = true;
            this.snakeGame.Start();
        }
    },
    computed: {
        foodLeft() {
            return foodLimit - this.foodEaten;
        }
    },

    mounted() {
        snake2d.config.sizeCeil = 15;
        this.snakeGame = new snake2d({
            gameCanvas: this.$refs.canvas,

            onGameOver: () => {
                this.gameOver = true;
                this.gameStarted = false;
            },
            onStart: () => {
                this.gameStarted = true;
            },
            onGameScore: (score) => {
                this.foodEaten = score;
                if(this.foodEaten == foodLimit)
                    this.snakeGame.Stop();
            }
        });
        document.addEventListener("keydown", (e) => {
            if (!this.snakeGame._playing)
                return;

            // Control game by arrows
            this.snakeGame.snake.Control(e.code);

            // Key btn on display
            this.buttons.add(e.code);
        });
        document.addEventListener("keyup", (e) => {
            this.buttons.delete(e.code);
        });
    },
}
</script>

<style scoped>
.index-preview {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    margin-left: 20px;
}

.blur {
    position: absolute;

    width: 500px;
    height: 500px;
    opacity: 0.3;
    background: radial-gradient(circle at center, rgba(67, 217, 173, 1) 0%, rgba(67, 217, 173, 0) 70%);
}

.blur.blur-green {
    top: calc(50% - 160px);
    left: calc(50% - 140px);
    transform: translate(-50%, -50%);
}

.blur.blur-blue {
    bottom: calc(50% - 80px);
    right: calc(50% - 120px);
    transform: translate(50%, 50%);

    background: radial-gradient(circle at center, #4D5BCE 0%, #4d5bce00 70%);
}

.blur.blur-3 {
    bottom: calc(50% - 150px);
    right: calc(50% + 80px);
}

@keyframes blur-1-anim {

    0%,
    100% {
        top: calc(50% - 160px);
        left: calc(50% - 140px);
    }

    40% {
        top: calc(50% - 160px);
        left: calc(50% - 50px);
    }

    60% {
        top: calc(50% - 140px);
        left: calc(50% - 30px);
    }

    80% {
        top: calc(50% - 130px);
        left: calc(50% - 100px);
    }
}

@keyframes blur-2-anim {

    0%,
    100% {
        bottom: calc(50% - 80px);
        right: calc(50% - 120px);
    }

    40% {
        bottom: calc(50% - 200px);
        right: calc(50% - 100px);
    }

    60% {
        bottom: calc(50% - 140px);
        right: calc(50% - 30px);
    }

    80% {
        bottom: calc(50% - 130px);
        right: calc(50% - 100px);
    }
}

@keyframes blur-3-anim {

    0%,
    100% {
        bottom: calc(50% - 150px);
        right: calc(50% + 80px);
    }

    40% {
        bottom: calc(50% - 200px);
        right: calc(50% + 150px);
    }

    60% {
        bottom: calc(50% - 240px);
        right: calc(50% + 100px);
    }

    80% {
        bottom: calc(50% - 130px);
        right: calc(50% + 100px);
    }
}

.blur-1 {
    animation: blur-1-anim 7s infinite;
    animation-timing-function: linear;
}

.blur-2 {
    animation: blur-2-anim 7s infinite;
    animation-timing-function: linear;
}

.blur-3 {
    animation: blur-3-anim 7s infinite;
    animation-timing-function: linear;
}

.game-box {
    position: relative;

    width: 510px;
    height: 475px;
    box-shadow: 2px 2px 15px -2px rgba(0, 0, 0, 0.53);

    background: linear-gradient(156deg, rgba(23, 85, 83, 1) 0%, rgba(67, 217, 173, 0.20) 100%);


    border: 3px solid #000;
    border-radius: 8px;
}

.game-box__inner {
    display: flex;
    box-shadow: inset -3px 16px 0px -12px rgb(255 255 255 / 29%);
    padding: 35px 30px;
    border-radius: 8px;
}

.game-box .pin {
    position: absolute;
    width: 13px;
    height: 13px;
    background: radial-gradient(circle, rgba(25, 108, 106, 1) 0%, rgba(17, 75, 74, 1) 100%);
    box-shadow: 3px 4px 10px -2px rgba(0, 0, 0, 0.75);
    border-radius: 100%;
}

.game-box .pin-inner {
    position: relative;
    box-shadow: inset -1px 9px 18px -17px rgb(255 255 255 / 75%);
    width: 100%;
    height: 100%;
    border-radius: 100%;
}

.game-box .pin.top {
    top: 12px;
}

.game-box .pin.bottom {
    bottom: 12px;
}

.game-box .pin.left {
    left: 12px;
}

.game-box .pin.right {
    right: 12px;
}

.game-box .pin-inner::before,
.game-box .pin-inner::after {
    content: '';
    top: 6px;
    left: 3px;

    position: absolute;
    width: 7px;
    height: 2px;
    background: #114944;
}

.game-box .pin-inner::before {
    transform: rotateZ(45deg);
}

.game-box .pin-inner::after {
    transform: rotateZ(-45deg);
}

.game-canvas {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 240px;
    height: 405px;
    border-radius: 8px;
    box-shadow: inset -1px -2px 15px -2px rgba(0, 0, 0, 0.75);
    background: #011627;
}

.index-container canvas.first-show {

    background-image: url(../assets/snake.png);
    background-size: contain;
}

.game-canvas__info {
    position: absolute;
    display: flex;
    align-items: center;
    flex-direction: column;
    left: 0;
    bottom: 65px;
    width: 100%;
}

.game-canvas__info .text {
    color: var(--accent-2);
    font-size: 24px;
    font-weight: 500;
    text-transform: uppercase;
    text-align: center;
    background: #00101cd6;
    box-shadow: inset 2px 2px 15px -2px rgba(0, 0, 0, 0.53);

    width: 100%;
    padding: 12px 10px;
    margin-bottom: 20px;
}



.game-info {
    margin-left: 24px;
}

.game-info span {
    display: block;
    font-size: 14px;
    line-height: 1.3;
    color: #fff;
}

.game-info__container {
    padding: 13px;
}

.game-info__control {
    background: rgb(1 20 35 / 19%);
    border-radius: 8px;
    margin-bottom: 20px;
}

.game-info__control .game-keys {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    margin-top: 15px;
    gap: 5px;
    width: 100%;
}

.game-info__control .game-keys .arrow {
    display: flex;
    align-items: center;
    justify-content: center;

    color: #fff;
    line-height: 1;
    width: 49px;
    height: 28px;

    background: #010C15;
    border: 1px solid #1E2D3D;
    border-radius: 8px;
}

.game-info__control .game-keys .arrow.active {
    background: #4f5153;
}

.game-info .food-list {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    margin-top: 10px;
    column-gap: 0px;
    row-gap: 18px;
}

.game-info .food {
    position: relative;
    width: 11px;
    height: 11px;
    border-radius: 3px;
    background: var(--accent-2);

    box-shadow: 0px 0px 0px 5px #43d9ad2e;
}

.game-info .food.eaten {
    opacity: 0.3;
}
</style>