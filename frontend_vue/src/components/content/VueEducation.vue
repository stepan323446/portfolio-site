<template>
    <div class="education">
        <div class="header">
            <div class="image">
                <img :src="education.icon" alt="">
            </div>
            <div class="header-info">
                <a :href="education.url" class="title">## {{ education.name }}
                    <FontAwesomeIcon :icon="faUpRightFromSquare" />
                </a>
                <div class="subtitle">{{ education.subname }}</div>
                <div class="date">{{ education.time_start }} - {{ education.time_end }}</div>
            </div>

        </div>
        <div class="content" v-html="education.content"></div>
        <div v-if="education.document" class="file">
            <a :href="education.document" :download="education.document" target="_blank">{{ education.document_name
                }}</a>
        </div>
        <VueSkills :skills="education.skills" />
    </div>
</template>

<script>
import { faUpRightFromSquare } from '@fortawesome/free-solid-svg-icons';

export default {
    name: 'VueEducation',
    props: {
        education: {
            type: Object,
            required: true
        }
    },

    data() {
        return {
            faUpRightFromSquare
        }
    },
}
</script>

<style scoped>
.education {
    padding: 15px;
    background: var(--input-background-color);
    border: 1px solid var(--borders-color);
    max-width: 800px;
    border-radius: 15px;

    margin: 0 auto;
}

.header {
    display: flex;
}
.header >>> svg {
    width: 14px;
    height: 14px;
}

.image {
    width: 48px;
    height: 48px;
    flex-shrink: 0;
    margin-right: 15px;
}

.image img {
    object-fit: contain;
}

.header {
    margin-bottom: 20px;
}

.header-info .title {
    color: var(--active-text-color);
    font-size: 18px;
    font-weight: 400;
}
.file {
    display: inline-block;
    margin-bottom: 15px;
}
.date {
    font-size: 14px;
}
</style>