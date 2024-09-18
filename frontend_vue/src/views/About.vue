<template>
    <VueFileManager title="About me">
        <template v-slot:sidebar>
            <VueSidebarDropdown title="personal-info">
                <div v-if="primaryInfo.photo" class="primary-photo image image-cover">
                    <img :src="primaryInfo.photo" alt="">
                </div>
                <div class="content" v-html="primaryInfo.description"></div>
            </VueSidebarDropdown>

            <VueSidebarDropdown title="contacts">
                <VueContactLinks />
            </VueSidebarDropdown>
        </template>
        <slot>
            <VueFileContent v-for="post in posts" :post="post"></VueFileContent>
        </slot>
    </VueFileManager>
</template>

<script>
import VueFileManager from '@/components/UI/VueFileManager';
import VueFolder from '@/components/UI/VueFolder.vue';
import VueFile from '@/components/UI/VueFile.vue';
import VueFileContent from '@/components/UI/VueFileConent.vue';

import axios from "axios";

export default {
    name: 'AboutPage',
    components: {
        VueFileManager, VueFolder, VueFile, VueFileContent
    },
    data() {
        return {
            posts: [ ],
            primaryInfo: { }
        }
    },
    methods: {

    },
    mounted() {
        // Fetch data
        this.$store.commit('setLoadingStatus', true);
        Promise.all([
            axios.get('/api/v1/bio/primary-info/'),
            axios.get('/api/v1/bio/file-list/')
        ]).then(([primaryInfoResponse, filesResponse]) => {
            this.primaryInfo = primaryInfoResponse.data;
            this.posts = filesResponse.data;
            
        }).catch((error) => {
            console.log(error);

        }).finally(() => {
            this.$store.commit('setLoadingStatus', false);
        });
    }
}
</script>

<style scoped>


.folder-content li {
    margin-bottom: 10px;
}

.folder-content ul {
    list-style: none;
}
.primary-photo {
    width: 150px;
    height: 150px;
    margin: 0 auto;
    border-radius: 3px;
    overflow: hidden;
    margin-bottom: 15px;
}
.content >>> h1, 
.content >>> h2 {
    font-size: 20px;
    font-weight: 400;
    color: var(--active-text-color);
    margin-bottom: 10px
}
.content >>> p {
    font-size: 16px;
    line-height: 20px;
}
</style>