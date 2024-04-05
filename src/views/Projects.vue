<template>
    <VueFileManager :title="title">
        <template v-slot:sidebar>
            <VueSidebarDropdown title="Just text">
                Hello world
            </VueSidebarDropdown>
        </template>
        Hello world
    </VueFileManager>
</template>

<script>
    import VueFileManager from '@/components/UI/VueFileManager';

    export default {
        name: 'ProjectsPage',
        components: {
            VueFileManager
        },
        data() {
            return {
                title: "projects"
            }
        }
    }
</script>

<style scoped>
    
</style>