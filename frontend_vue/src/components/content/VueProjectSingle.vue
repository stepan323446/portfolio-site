<template>
    <div v-if="project && visible" class="project">
        <div class="background" @click="closeModal()"></div>

        <div class="project-single">
            <div class="project-header">
                <div class="title">{{ project.title }}</div>
                <button class="close" @click="closeModal()">
                    <FontAwesomeIcon :icon="faClose" />
                </button>
            </div>
            <div class="image image-cover thumb" :style="{
                'background-image': 'url(' + project.background + ')'
            }">
                <div class="image-inner">
                    <h1>{{ project.title }}</h1>
                </div>
            </div>
            <div class="project-single__content">
                <div class="content" v-html="project.content"></div>

                <h2>## Skills</h2>
                <VueSkills :skills="project.skills"></VueSkills>

                <div class="btns">
                    <a v-if="project.code_url" :href="project.code_url" target="_blank">view code</a> |
                    <a v-if="project.run_url" :href="project.run_url" target="_blank">run</a>
                </div>

            </div>
        </div>
    </div>

</template>

<script>
import VueFileManager from '@/components/UI/VueFileManager.vue';
import VueContactLinks from '@/components/UI/VueContactLinks.vue';
import { faClose, faL } from '@fortawesome/free-solid-svg-icons';

export default {
    name: 'VueProjectSingle',
    components: { VueFileManager, VueContactLinks },
    props: {
        project: {
            type: Object,
            required: true
        },
        visible: {
            type: Boolean,
            default: false
        }
    },
    data() {
        return {
            faClose
        }
    },
    methods: {
        closeModal() {
            this.$emit('update:visible', false);
            this.$store.commit('documentLockOverflow', false);
        }
    }
}
</script>

<style scoped>
.background {
    position: fixed;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background: #000;
    opacity: 0.7;
}
.project {
    position: fixed;
    left: 0;
    top: 0;
    padding: 0 20px;
    padding-bottom: 20px;
    width: 100%;
    height: 100%;
    overflow-y: auto;
    z-index: 999;
}
.project-single {
    position: relative;
    border: 2px solid var(--borders-color);
    overflow: hidden;
    border-radius: 8px;

    max-width: 790px;
    width: 100%;

    background: var(--input-background-color);
}

.project-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.project-header .title {
    padding: 10px;
}

.project-header .close {
    padding: 10px;
    font-size: 16px;
    color: var(--text-color);
    cursor: pointer;
    background: none;
    border: none
}

.project-header .close:hover {
    color: var(--active-text-color);
}

.project-single {
    max-width: 1000px;
    margin: 0 auto;
    margin-top: 40px;
}

.project-single .thumb {
    position: relative;
    text-align: center;
    height: 300px;
    overflow: hidden;
    border-bottom: 1px solid var(--borders-color);
    background-size: cover;
    background-position: center;
}

.project-single__content {
    line-height: 1.4;
    padding: 20px;
}

.content>>>p {
    margin-bottom: 20px;
}

.project-single__content>>>h2 {
    color: var(--active-text-color);
    font-size: 18px;
    font-weight: 400;
    margin-bottom: 15px;
}

h1 {
    color: var(--active-text-color);
    margin-bottom: 15px;
    font-size: 26px;
}

.project-single .thumb .image-inner {
    position: absolute;
    left: 0;
    bottom: 0;
    text-align: center;
    background: linear-gradient(0deg, rgba(0, 0, 0, 0.87) 0%, rgba(0, 0, 0, 0.61) 39%, rgba(255, 255, 255, 0) 100%);
    padding: 30px 10px 10px 10px;
    width: 100%;
}
</style>