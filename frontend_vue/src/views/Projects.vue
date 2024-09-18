<template>
    <VueFileManager :title="title">
        <template v-slot:sidebar>
            <VueSidebarDropdown title="filter">
                <VueFolder v-for="filterList in filterLists" :title="filterList.title" :initialActive="false">
                    <ul class="filters">
                        <li v-for="filter in getFilteredSkills(filterList.skills)">
                            <VueCheckbox @state="changeActiveFilters($event, filter.id)"><span class="skill-icon" v-html="filter.icon_svg"></span> {{ filter.name }}</VueCheckbox>
                        </li>
                    </ul>
                </VueFolder>
            </VueSidebarDropdown>
        </template>

        <VueProjectList :projects="getFilteredProjects" class="container-in-content" />
        
    </VueFileManager>
</template>

<script>
import VueProjectList from '@/components/content/VueProjectList.vue';
import VueFileManager from '@/components/UI/VueFileManager';
import VueFolder from '@/components/UI/VueFolder.vue';
import axios from 'axios'
import { RouterLink } from 'vue-router';

export default {
    name: 'ProjectsPage',
    components: {
        VueFileManager, VueFolder, VueProjectList
    },
    data() {
        return {
            title: "projects",
            filterLists: [],
            filters: [],
            activeFilters: [],
            projects: []
        }
    },
    computed: {
        getFilteredProjects() {
            if (this.activeFilters.length == 0)
                return this.projects;

            let filteredProjects = [];
            for (const project of this.projects) {
                let isIncluded = true;
                for (const filterID of this.activeFilters) {
                    if (!project.skills.includes(filterID)) {
                        isIncluded = false;
                        break;
                    }
                }

                if (isIncluded)
                    filteredProjects.push(project);
            }

            return filteredProjects;
        }
    },
    methods: {
        getFilteredSkills(filterList) {
            return filterList.filter(filter => filter.is_filter == true);
        },
        changeActiveFilters(active, filterID) {
            let existIndex = this.activeFilters.indexOf(filterID);
            if(active) {
                if(existIndex == -1)
                    this.activeFilters.push(filterID);
            }
            else {
                if(existIndex != -1)
                    this.activeFilters.splice(existIndex, 1);
            }
            this.updateTitle()
        },
        updateTitle() {
            let founded = false;
            this.title = "";
            for (const filterID of this.activeFilters) {
                let filter = this.filters.find(filter => filter.id === filterID);
                this.title += filter.name + ';';
            }
            if (this.activeFilters.length == 0)
                this.title = "projects";
        },
    },
    mounted() {
        this.$store.commit('setLoadingStatus', true);
        Promise.all([
            axios.get('/api/v1/projects/list/'),
            axios.get('/api/v1/bio/skill-category-list/')
        ]).then(([projectsResponse, filtersResponse]) => {
            this.projects = projectsResponse.data;
            this.filterLists = filtersResponse.data;

            for(let filterList of this.filterLists) {
                this.filters.push(...filterList.skills)
            }               

        }).catch((error) => {
            console.log(error);

        }).finally(() => {
            this.$store.commit('setLoadingStatus', false);       
        });
    }
}
</script>

<style scoped>
.filters {
    list-style: none;
}

.filters li {
    margin-bottom: 17px;
}
.skill-icon {
    display: inline-block;
    width: 16px;
    margin-right: 10px;
}
.skill-icon >>> path {
    fill: var(--text-color);
}
* >>> .folder {
    margin-bottom: 10px;
}
</style>