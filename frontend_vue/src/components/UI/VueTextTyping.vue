<template>
    <span class="text-typing">
        <span class="text-typing">{{ currentText }}</span>
        <span class="cursor-typing">|</span>
    </span>
</template>

<script>

export default {
    name: "VueTyping",

    props: {
        lines: {
            type: Array,
            required: true
        }
    },
    data() {
        return {
            currentText: "",
            sleepTime: 100,
            wordIndex: 0
        }
    },
    methods: {
        sleep(ms) {
            return new Promise((resolve) => setTimeout(resolve, ms))
        },
        async writeLoop() {
            while (true) {
                let curWord = this.$props.lines[this.wordIndex];

                for (let i = 0; i < curWord.length; i++) {
                    this.currentText = curWord.substring(0, i + 1);

                    await this.sleep(this.sleepTime);
                }
                await this.sleep(this.sleepTime * 10);

                for (let i = curWord.length; i > 0; i--) {
                    this.currentText = curWord.substring(0, i - 1);

                    await this.sleep(this.sleepTime);
                }
                await this.sleep(this.sleepTime * 5);

                if (this.wordIndex == this.$props.lines.length - 1)
                    this.wordIndex = 0;
                else
                    this.wordIndex++;
            }
        }
    },
    mounted() {
        this.writeLoop();
    }
}
</script>

<style scoped>
@keyframes cursor-typing-animation {

    0%,
    100% {
        opacity: 1;
    }

    50% {
        opacity: 0;
    }
}

.cursor-typing {
    animation: cursor-typing-animation 1s infinite;
}
</style>