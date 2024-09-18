<template>
    <div class="index">
        <div class="index-container">
            <div class="index-info">
                <div class="index-title">
                    <span class="welcome-span">Hi all, I am</span>
                    <h1>Stepan Turitsin</h1>
                    <span id="who-i"> >
                        <VueTyping :lines="linesTyping" />
                    </span>
                </div>
                <div class="game-code__wrapper">
                    <pre v-highlightjs><code class="language-js game-code">
// Let's play snake for a bit
// you can also see it on my Github page
const githubLink = "https://github.com/stepan323446/snake2d"</code></pre>
                </div>

                <div class="link-to-btn">
                    <VueButton :to="{name: 'about'}" class="btn-primary">about-me</VueButton>
                    <VueButton :to="{name: 'projects'}">projects</VueButton>
                </div>
            </div>
            <div class="snake-game__wrapper"></div>
            <snakeGame />
        </div>
    </div>
</template>

<script>
import snakeGame from "@/components/snakeGame.vue";
import hljs from "highlight.js";

export default {
    name: "IndexPage",
    components: {
        snakeGame,
    },
    data() {
        return {
            linesTyping: ["Web Developer", "Frontend Developer", "Programmer"],
        };
    },
};
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
    color: #e5e9f0;
    font-size: 18px;
    font-weight: 500;
}

.index-title h1 {
    color: #e5e9f0;
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
    color: #4d5bce;
    font-size: 32px;
    font-weight: 500;
}

.hljs {
    color: #43d9ad;
}
.link-to-btn {
    margin-top: 15px;
}
.link-to-btn > * {
    margin-right: 10px;
}
.link-to-btn >>> .btn-primary {
    padding-left: 30px;
    padding-right: 30px;
}

@media only screen and (max-width: 1200px) {
    .index-title h1 {
        font-size: 44px;
    }

    .index-container {
        overflow: hidden;
        justify-content: center;
    }
}

@media only screen and (max-width: 455px) {
    .game-code__wrapper {
        display: none;
    }
}
</style>
