<template>
    <div class="index">
        <div class="index-container">
            <div class="index-info">
                <div class="index-title">
                    <span class="welcome-span">Hi all, I am</span>
                    <h1>Stepan Turitsin</h1>
                    <span id="who-i">> <span id="index-typing">Front-end developer</span><span
                            id="cursor-typing">|</span></span>
                </div>
                <pre v-highlightjs><code class="language-js game-code">
// Let's play snake for a bit
// you can also see it on my Github page
const githubLink = "https://github.com/stepan323446/snake2d"</code></pre>

                <pre v-highlightjs><code class="language-js mobile-index-code">
// find my profile on Github:
const githubLink = "https://github.com/stepan323446"</code></pre>
            </div>
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
                                <div id="snake2d-text" class="text" hidden>
                                    Game Over
                                </div>
                                <button id="snake2d-start" type="button" class="btn btn-primary">start-game</button>
                            </div>
                            <canvas id="snake2d" class="first-show" width="225" height="390"></canvas>
                        </div>
                        <div class="game-info">
                            <div class="game-info__control game-info__container">
                                <span>// use keyboard<br>// arrows to play</span>

                                <div class="game-keys">
                                    <div></div>
                                    <div class="arrow" key="ArrowUp"><FontAwesomeIcon :icon="faCaretUp"/></div>
                                    <div></div>

                                    <div class="arrow" key="ArrowLeft"><FontAwesomeIcon :icon="faCaretLeft"/></div>
                                    <div class="arrow" key="ArrowDown"><FontAwesomeIcon :icon="faCaretDown"/></div>
                                    <div class="arrow" key="ArrowRight"><FontAwesomeIcon :icon="faCaretRight"/></div>
                                </div>
                            </div>
                            <div class="game-info__container">
                                <span>// food left</span>
                                <div class="food-list">
                                    <div class="food"></div>
                                    <div class="food"></div>
                                    <div class="food"></div>
                                    <div class="food"></div>
                                    <div class="food"></div>

                                    <div class="food"></div>
                                    <div class="food"></div>
                                    <div class="food"></div>
                                    <div class="food"></div>
                                    <div class="food"></div>
                                </div>
                            </div>
                        </div>
                    </div>

                </div>
            </div>


        </div>
    </div>
</template>

<script>
import { faCaretUp, faCaretDown, faCaretLeft, faCaretRight }  from "@fortawesome/free-solid-svg-icons";
import hljs from 'highlight.js';
import snake2d from '@/assets/js/snake2d'

export default {
    name: 'IndexPage',
    data() {
        return {
            faCaretUp,
            faCaretLeft,
            faCaretDown,
            faCaretRight
        }
    }
}
</script>

<style scoped>
.index {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 100%;

    overflow: hidden;
}
.index-title {
    line-height: 1.3;
}

.index-title .welcome-span {
    color: #E5E9F0;
    font-size: 18px;
    font-weight: 500;
}

.index-title h1 {
    color: #E5E9F0;
    font-weight: 400;
    font-size: 62px;
}

.index-container {
    display: flex;
    justify-content: space-between;
    max-width: 1160px;
    padding: 0 10px;
    width: 100%;
    height: 100%;
}

.index-info {
    display: flex;
    flex-direction: column;
    justify-content: center;
}

#who-i {
    color: #4D5BCE;
    font-size: 32px;
    font-weight: 500;
}

.index-container .index-preview {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    margin-left: 20px;
}

.mobile-index-code {
    display: none;
}

.index-container .blur {
    position: absolute;

    width: 500px;
    height: 500px;
    opacity: 0.3;
    background: radial-gradient(circle at center, rgba(67, 217, 173, 1) 0%, rgba(67, 217, 173, 0) 70%);
}

.index-container .blur.blur-green {
    top: calc(50% - 160px);
    left: calc(50% - 140px);
    transform: translate(-50%, -50%);
}

.index-container .blur.blur-blue {
    bottom: calc(50% - 80px);
    right: calc(50% - 120px);
    transform: translate(50%, 50%);

    background: radial-gradient(circle at center, #4D5BCE 0%, #4d5bce00 70%);
}

.index-container .blur.blur-3 {
    bottom: calc(50% - 150px);
    right: calc(50% + 80px);
}
.hljs {
    color: #43D9AD;
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

.index-container .blur-1 {
    animation: blur-1-anim 7s infinite;
    animation-timing-function: linear;
}

.index-container .blur-2 {
    animation: blur-2-anim 7s infinite;
    animation-timing-function: linear;
}

.index-container .blur-3 {
    animation: blur-3-anim 7s infinite;
    animation-timing-function: linear;
}

.index-container .game-box {
    position: relative;

    width: 510px;
    height: 475px;
    box-shadow: 2px 2px 15px -2px rgba(0, 0, 0, 0.53);

    background: linear-gradient(156deg, rgba(23, 85, 83, 1) 0%, rgba(67, 217, 173, 0.20) 100%);


    border: 3px solid #000;
    border-radius: 8px;
}

.index-container .game-box__inner {
    display: flex;
    box-shadow: inset -3px 16px 0px -12px rgb(255 255 255 / 29%);
    padding: 35px 30px;
    border-radius: 8px;
}

.index-container .game-box .pin {
    position: absolute;
    width: 13px;
    height: 13px;
    background: radial-gradient(circle, rgba(25, 108, 106, 1) 0%, rgba(17, 75, 74, 1) 100%);
    box-shadow: 3px 4px 10px -2px rgba(0, 0, 0, 0.75);
    border-radius: 100%;
}

.index-container .game-box .pin-inner {
    position: relative;
    box-shadow: inset -1px 9px 18px -17px rgb(255 255 255 / 75%);
    width: 100%;
    height: 100%;
    border-radius: 100%;
}

.index-container .game-box .pin.top {
    top: 12px;
}

.index-container .game-box .pin.bottom {
    bottom: 12px;
}

.index-container .game-box .pin.left {
    left: 12px;
}

.index-container .game-box .pin.right {
    right: 12px;
}

.index-container .game-box .pin-inner::before,
.index-container .game-box .pin-inner::after {
    content: '';
    top: 6px;
    left: 3px;

    position: absolute;
    width: 7px;
    height: 2px;
    background: #114944;
}

.index-container .game-box .pin-inner::before {
    transform: rotateZ(45deg);
}

.index-container .game-box .pin-inner::after {
    transform: rotateZ(-45deg);
}

.index-container .game-canvas {
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

.index-container .game-canvas__info {
    position: absolute;
    display: flex;
    align-items: center;
    flex-direction: column;
    left: 0;
    bottom: 65px;
    width: 100%;
}

.index-container .game-canvas__info .text {
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

@keyframes cursor-typing-animation {

    0%,
    100% {
        opacity: 1;
    }

    50% {
        opacity: 0;
    }
}

#cursor-typing {
    animation: cursor-typing-animation 1s infinite;
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