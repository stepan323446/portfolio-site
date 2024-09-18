<template>
    <div class="project">
        <div class="title">
            <span class="title-span">{{ project.title }}</span> <span>// _{{ project.type }}</span> 
        </div>
        <div class="block">
            <div class="image image-cover" :style="{ 'background-image': 'url(' + project.background + ')' }">

                <span :style="{ background: project.primary_skill.background }"><span class="skill-icon"
                        v-html="project.primary_skill.icon_svg"></span></span>

            </div>
            <div class="project-info">
                <div class="text">
                    {{ project.excerpt }}
                </div>
                <VueButton @click="ViewProject()">view-project</VueButton>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'VueProject',
    data() {    
        return {

        }
    },
    props: {
        project: {
            type: Object,
            required: true
        },
        index: {
            type: Number,
            required: true
        }
    },
    methods: {
        ViewProject() {
            this.$emit('view-project');
        }
    }
}
</script>

<style scoped>
.project {
    position: relative;
    max-width: 380px;
    margin: 0 auto;
}

.project .title {
    font-size: 16px;
    margin-bottom: 15px;
    line-height: 20px;
}
.project .title span {
    display: inline-block;
}
.project .title .title-span {
    color: var(--accent-3);
    font-weight: 600;
}

.project .block {
    display: flex;
    flex-direction: column;

    height: calc(100% - 32px);
    background: var(--input-background-color);
}

.project .project-info {
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: start;

    border: 1px solid var(--borders-color);
    border-bottom-left-radius: 15px;
    border-bottom-right-radius: 15px;
    padding: 31px;
}

.project .text {
    line-height: 1.3;
    margin-bottom: 20px;
}

.project .btn {
    display: inline-block;
}

.project .image {
    position: relative;
    height: 145px;
    border: 1px solid var(--borders-color);
    border-top-left-radius: 15px;
    border-top-right-radius: 15px;
    flex-shrink: 0;

    background-size: cover;
    background-position: center;
}

.project .image > span {
    position: absolute;
    top: 15px;
    right: 15px;
    color: #000;
    font-size: 22px;
    width: 28px;
    height: 28px;
    border-radius: 2px;
}
.project .image .skill-icon {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 5px;
    width: 100% !important;
    height: 100%;
}
.project .image .skill-icon {
    margin-right: 0;
    width: 22px;
}
.project .image .skill-icon >>> path {
    fill: #000;
}
</style>