<template>
    <VueFileManager :title="post.title">
        <template v-slot:sidebar>
            <VueSidebarDropdown title="personal-info">
                <VueFolder v-for="folder in folders" :title="folder.name">
                    <slot>
                        <ul>
                            <li v-for="file in folder.files">
                                <VueFile :file="file" />
                            </li>
                        </ul>

                    </slot>
                </VueFolder>
            </VueSidebarDropdown>

            <VueSidebarDropdown title="contacts">
                <VueContactLinks />
            </VueSidebarDropdown>
        </template>
        <slot>
            <div class="text-content">
                <div v-html="post.content">

                </div>
                <div class="skill-category" v-for="category in post.skillCategories">
                    <h2>## {{ category.title }}</h2>
                    <VueSkills :skills="category.skills" />
                </div>
                <div class="expierences">
                    <VueExpierences :expierences="post.jobs" />
                </div>
            </div>
        </slot>
    </VueFileManager>
</template>

<script>
import VueFileManager from '@/components/UI/VueFileManager';
import VueFolder from '@/components/UI/VueFolder.vue';
import VueExpierences from '@/components/UI/VueExpierences.vue';
import VueFile from '@/components/UI/VueFile.vue';

export default {
    name: 'AboutPage',
    components: {
        VueFileManager, VueFolder, VueExpierences, VueFile
    },
    data() {
        return {
            post: {
                title: "bio",
                content: "<h2>Nice</h2><p>One thing the Intersection Observer API can't tell you: the exact number of pixels that overlap or specifically which ones they are; however, it covers the much more common use case of \"If they intersect by somewhere around N%, I need to do something.\"</p>",
                skillCategories: [
                    {
                        title: "Frontend",
                        skills: [
                            {
                                name: "HTML",
                                icon: "http://steve-dekart.xyz/media/icons/html5.svg"
                            },
                            {
                                name: "CSS",
                                icon: "http://steve-dekart.xyz/media/icons/css3.svg"
                            },
                            {
                                name: "JS",
                                icon: "http://steve-dekart.xyz/media/icons/css3.svg"
                            }
                        ]
                    },
                    {
                        title: "Backend",
                        skills: [
                            {
                                name: "Wordpress",
                                icon: "http://steve-dekart.xyz/media/icons/wordpress.png"
                            }
                        ]
                    }
                ],
                jobs: [
                    {
                        image_url: "http://steve-dekart.xyz/media/jobs/vue-js-icon-512x442-k8qh9h45.png",
                        name: "Xbox developer",
                        company: "Microsoft",
                        start_date: "12 April, 2021",
                        end_date: "Present",
                        skills: "HTML • CSS • JavaScript",
                        descpr: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras interdum, purus a volutpat consequat, dolor lectus consectetur ligula"
                    }
                ]
            },


            folders: [
                {
                    name: "biography",
                    files: [
                        {
                            name: "bio",
                            slug: "bio"
                        },
                        {
                            name: "hobby",
                            slug: "hobby"
                        }
                    ]
                }
            ],


        }
    }
}
</script>

<style scoped>
.text-content {
    line-height: 1.4;
}

.text-content>>>p {
    margin-bottom: 20px;
}

.text-content>>>h1,
.text-content>>>h2,
.text-content>>>h3 {
    color: var(--active-text-color);
    font-size: 18px;
    font-weight: 400;
    margin-bottom: 15px;
}

.text-content>>>h1 {
    font-size: 24px;
}

.text-content>>>h3 {
    font-size: 16px;
}

.folder-content li {
    margin-bottom: 10px;
}

.folder-content ul {
    list-style: none;
}
</style>