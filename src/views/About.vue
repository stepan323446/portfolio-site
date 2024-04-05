<template>
    <VueFileManager :title="title">
        <template v-slot:sidebar>
            <VueSidebarDropdown title="personal-info">
                <VueFolder title="biography">
                    <slot>Hello world</slot>
                </VueFolder>
            </VueSidebarDropdown>
            
            <VueSidebarDropdown title="contacts">
                <VueContactLinks/>
            </VueSidebarDropdown>
        </template>
    </VueFileManager>
</template>

<script>
    import VueFileManager from '@/components/UI/VueFileManager';
    import VueFolder from '@/components/UI/VueFolder.vue';

    export default {
        name: 'AboutPage',
        components: {
            VueFileManager, VueFolder
        },
        data() {
            return {
                title: "bio"
            }
        }
    }
</script>

<style scoped>
    
</style>