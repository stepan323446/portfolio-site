<template>
    <div v-if="projects.length > 0" class="projects">
        <VueProject v-for="(project, index) in projects" :project="project" :index="index" @view-project="ViewProject(project)" />

        <VueProjectSingle :project="viewed_project" v-model:visible="visible_modal" />
    </div>
</template>

<script>
import VueProject from '@/components/content/VueProject.vue';
import VueProjectSingle from '@/components/content/VueProjectSingle.vue';

export default {
    name: 'VueProjectList',
    components: { VueProject, VueProjectSingle },
    props: {
        projects: {
            type: Array,
            required: true,
            default: [ ]
        }
    },
    data() {
        return {
            visible_modal: false,
            viewed_project: null,
        }
    },
    methods: {
        ViewProject(project) {
            this.viewed_project = project;
            this.visible_modal = true;
            this.$store.commit('documentLockOverflow', true);
        }
    }
}
</script>

<style scoped>
.projects {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 40px;
    margin-top: 20px;
}
@media only screen and (max-width: 1000px) {
    .projects {
        grid-template-columns: repeat(2, 1fr);
        gap: 30px;
    }
}

@media only screen and (max-width: 715px) {
    .projects {
        grid-template-columns: repeat(1, 1fr);
        gap: 30px;
    }
}
</style>