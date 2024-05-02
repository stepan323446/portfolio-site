<template>
    <VueFileManager :title="title">
        <template v-slot:sidebar>
            <VueSidebarDropdown title="filter">
                <ul class="filters">
                    <li v-for="filter in filters">
                        <VueCheckbox v-model:active="filter.isActive">{{ filter.name }}</VueCheckbox>
                    </li>

                </ul>
            </VueSidebarDropdown>
        </template>

        <div class="projects" v-if="getFilteredProjects.length > 0">

            <div class="project" v-for="(project, index) in getFilteredProjects">
                <div class="title">
                    <span>Project {{ index + 1 }}</span> // _{{ project.type_project }}
                </div>
                <div class="block">
                    <div class="image image-cover" :style="{ 'background-image': 'url(' + project.image_url + ')' }">

                        <span style="background: #fff;"><i class="fa-brands fa-wordpress"></i></span>

                    </div>
                    <div class="project-info">
                        <div class="text">
                            {{ project.excerpt }}
                        </div>
                        <a href="/projects/portalvirtualreality" class="btn">view-project</a>
                    </div>
                </div>
            </div>
           
        </div>
        <div v-else class="nothing">
                Nothing found by filter
        </div>
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
            title: "projects",
            filters: [
                {
                    id: 0,
                    name: 'Wordpress',
                    isActive: false,
                },
                {
                    id: 1,
                    name: 'Vue',
                    isActive: false,
                },
                {
                    id: 2,
                    name: 'HTML',
                    isActive: false,
                }
            ],
            activeFilters: [ ],
            projects: [
                {
                    title: 'portalvr',
                    type_project: 'cms-system',
                    image_url: 'http://steve-dekart.xyz/media/uploads/screenshot.png',
                    excerpt: 'Wordpress theme with many features.',
                    slug: 'portalvirtualreality',
                    skills: [0, 2]
                }
            ]
        }
    },
    watch: {
        filters: {
            handler(val) {
                this.updateTitleAndSetFilters();
            },
            deep: true
        }
    },
    computed: {
        getFilteredProjects() {
            if(this.activeFilters.length == 0)
                return this.projects;

            let filteredProjects = [ ];
            for (const project of this.projects) {
                if(project.skills.some(r => this.activeFilters.includes(r)))
                    filteredProjects.push(project);
            }
            
            return filteredProjects;
        }
    },
    methods: {
        updateTitleAndSetFilters() {
            let founded = false;
            this.activeFilters = [ ];
            for (const filter of this.filters) {
                if(filter.isActive) {
                    // title
                    if(!founded) {
                        this.title = '';
                    }
                    this.title += `${filter.name};`;
                    founded = true;

                    // filters
                    this.activeFilters.push(filter.id);
                }
            }
            if(!founded)
                this.title = "projects";
        }
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
.projects {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 40px;

    max-width: 1200px;
    margin: 0 auto;
    margin-top: 75px;
    
}
.project {
    position: relative;
}
.project .title {
    font-size: 16px;
    min-height: 32px;
}
.project .title span {
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
.project .image span {
    position: absolute;
    top: 15px;
    right: 15px;
    color: #000;
    font-size: 22px;
    width: 28px;
    height: 28px;
    border-radius: 2px;

    display: flex;
    align-items: center;
    justify-content: center;
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