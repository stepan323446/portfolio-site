<template>
    <div class="index">
        <div class="index-container">
            <div class="index-info">
                <div class="index-title">
                    <span class="welcome-span">Hi all, I am</span>
                    <h1>Stepan Turitsin</h1>
                    <span id="who-i">
                        > <VueTyping :lines="linesTyping"/>
                    </span>
                </div>
                <pre v-highlightjs><code class="language-js game-code">
// Let's play snake for a bit
// you can also see it on my Github page
const githubLink = "https://github.com/stepan323446/snake2d"</code></pre>

                <pre v-highlightjs><code class="language-js mobile-index-code">
// find my profile on Github:
const githubLink = "https://github.com/stepan323446"</code></pre>
            </div>
            <snakeGame/>


        </div>
    </div>
</template>

<script>

import snakeGame from "@/components/snakeGame.vue";
import hljs from 'highlight.js';

export default {
    name: 'IndexPage',
    components: {
        snakeGame
    },
    data() {
        return {
            linesTyping: [
                "Web Developer",
                "Frontend Developer",
                "Programmer"
            ]
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

.mobile-index-code {
    display: none;
}


.hljs {
    color: #43D9AD;
}


</style>