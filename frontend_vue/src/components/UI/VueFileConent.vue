<template>
    <div class="file-content container-in-content">
        <div class="text-content">
            <h2 :style="{'text-align': post.textAlign}">{{ post.title }}</h2>

            <!-- Text content -->
            <div v-html="post.content" :style="{'text-align': post.textAlign}"></div>

            <!-- Categories -->
             <div class="skills">
                <VueSkillCategory v-for="category in post.cats" :category="category"/>
             </div>

            <!-- Jobs -->
            <div v-if="post.jobs.length > 0" class="expierences vertical-timeline">
                <div v-for="job in post.jobs" class="line-timeline">
                    <VueExpierences  :expierence="job"/>
                    <div class="timeline-icon image image-cover">
                        <img :src="job.icon" alt="">
                    </div>
                    <div class="timeline-date">
                        {{ getJobDate(job.time_start) }} - {{ getJobDate(job.time_end) }}
                    </div>
                </div>
            </div>

            <!-- Projects -->
             <VueProjectList :projects="post.projects"/>

             <!-- Educations -->
              <div v-if="post.educations.length > 0" class="educations">
                <VueEducation v-for="education in post.educations" :education="education" />
              </div>
        </div>
    </div>
</template>

<script>
import VueExpierences from "@/components/content/VueExpierences.vue";
import VueSkillCategory from "@/components/content/VueSkillCategory.vue";
import VueEducation from "@/components/content/VueEducation.vue";
import VueProjectList from "@/components/content/VueProjectList.vue";
import { formatDate } from '@/utils/dateUtils';

export default {
    name: "VueFileContent",
    components: { VueExpierences, VueSkillCategory, VueProjectList, VueEducation },
    props: {
        post: {
            type: Object,
            required: true,
        },
    },
    methods: {
        getJobDate(date) {
            if(!date)
                return 'present'

            return formatDate(date)
        }
    }
};
</script>

<style scoped>
.file-content {
    margin-bottom: 60px;
}
/* Text content */
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
.text-content h2 {
    font-size: 24px;
}

.text-content>>>h1 {
    font-size: 24px;
}

.text-content>>>h3 {
    font-size: 16px;
}

/* Skills */
.skills {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
}
.vertical-timeline {
    position: relative;
    padding: 20px 0;
}
.vertical-timeline::before {
    content: '';
    position: absolute;
    left: 50%;
    height: 95%;
    transform: translateX(-50%);

    width: 3px;
    background: #fff;
}
.line-timeline {
    position: relative;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 80px;
}
.timeline-icon {
    position: absolute;
    top: 20px;
    left: 50%;
    transform: translateX(-50%);

    width: 50px;
    height: 50px;
    border: 2px solid #fff;
    border-radius: 100%;
    overflow: hidden;
}
.timeline-date {
    margin-top: 35px;
    color: var(--active-text-color);
}
.line-timeline:nth-child(even) .timeline-date {
    order: 0;
    text-align: right;
}
.line-timeline:nth-child(even) >>> .expierence {
    order: 1;
}

/* Educations */
.educations >>> .education {
    margin-bottom: 20px;
}

@media only screen and (max-width: 900px) {
    .line-timeline {
        display: block;
        margin-left: 45px
    }
    .vertical-timeline::before {
        left: 15px;
        transform: translate(0);
    }
    .timeline-icon {
        width: 40px;
        height: 40px;

        left: -47px;
        transform: translate(0);
    }
    .timeline-date {
        display: none;
    }
    .projects {
        grid-template-columns: repeat(2, 1fr);
    }
}
@media only screen and (max-width: 680px) {
    .skills {
        grid-template-columns: 1fr;
    }
    .projects {
        grid-template-columns: 1fr;
    }
}

</style>
