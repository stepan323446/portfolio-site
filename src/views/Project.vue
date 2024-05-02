<template>
    <VueFileManager :title="project.title">
        <template v-slot:sidebar>
            <VueSidebarDropdown title="contacts">
                <VueContactLinks />
            </VueSidebarDropdown>
        </template>

        <div class="project-single">
            <div class="image image-cover thumb" :style="{
        'background-image': 'url(' + project.image_url + ')'
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



                    <a href="https://portalvirtualreality.com/" target="_blank">run</a>

                </div>

            </div>
        </div>
    </VueFileManager>
</template>

<script>
import VueFileManager from '@/components/UI/VueFileManager.vue';
import VueContactLinks from '@/components/UI/VueContactLinks.vue';
import { titleConst } from '@/router/index';

export default {
    components: { VueFileManager, VueContactLinks },
    data() {
        return {
            project:
            {
                title: 'portalvirtualreality',
                type_project: 'cms-system',
                image_url: 'http://steve-dekart.xyz/media/uploads/screenshot.png',
                content: `
                <p>Quite an unusual project that differs from many other Wordpress projects.&nbsp;This project has a lot
                    of
                    unusual post types and non-standard functionality.</p>

                <h2>## Post types</h2>

                <p>There are many types of posts in this project, such as post, games, achievements, item, quiz</p>

                <p><strong>* post</strong> - regular news articles. <a
                        href="https://portalvirtualreality.com/valorant-epizod-8-akt-1-data-vyxoda-novoe-oruzhie-i-agent-skiny-boevoj-propusk-i-dr/"
                        target="_blank">Example</a></p>

                <p><strong>* games</strong> - special information about the game. <a
                        href="https://portalvirtualreality.com/games/valorant/" target="_blank">Example</a></p>

                <p><strong>* achievements</strong> - page of achievements for games. <a
                        href="https://portalvirtualreality.com/achievments/dostizheniya-persona-5-the-royal-pc/"
                        target="_blank">Example</a></p>

                <p><strong>* item</strong> - a specific game item with its description. <a
                        href="https://portalvirtualreality.com/item/sword-of-narzissenkreuz-in-genshin-impact/">Example</a>
                </p>

                <p><strong>* quiz</strong> - interesting tests for users.</p>

                <p>Some record types have a relationship through a linking taxonomy. Thus, a specific game can be linked
                    to each
                    post</p>`,
                slug: 'portalvirtualreality',
                skills: [
                    {
                        name: "Wordpress",
                        icon: "http://steve-dekart.xyz/media/icons/wordpress.png"
                    },
                    {
                        name: "HTML",
                        icon: "http://steve-dekart.xyz/media/icons/html5.svg"
                    },
                    {
                        name: "CSS",
                        icon: "http://steve-dekart.xyz/media/icons/css3.svg"
                    },
                ]
            }

        }
    },
    mounted() {
        document.title = this.project.title + titleConst;
    }
}
</script>

<style scoped>
.project-single {
    border: 2px solid var(--borders-color);
    overflow: hidden;
    border-radius: 8px;
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
    background: var(--input-background-color);
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