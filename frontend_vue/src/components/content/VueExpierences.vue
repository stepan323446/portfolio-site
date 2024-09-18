<template>
    <div class="expierence">
        <div class="exp-header">
            <div class="image image-cover logo">
                <img :src="`${expierence.icon}`" alt="">
            </div>
            <div class="exp-header__info">
                <h2>## {{ expierence.name }}</h2>
                <div class="company">{{ expierence.company }}</div>
                <div class="date">{{ getJobDate(expierence.time_start) }} - {{ getJobDate(expierence.time_end) }}</div>
            </div>
        </div>
        <div class="exp-info">
            {{ expierence.content }}
        </div>

        <div class="exp-skills">
            <div class="exp-skills__title">
                skills:
            </div>
            <div class="exp-skills__text">
                {{ expierence.skills }}
            </div>
        </div>

    </div>
</template>

<script>
import { formatDate } from '@/utils/dateUtils';

export default {
    name: "VueExpierences",
    props: {
        expierence: {
            type: Object,
            required: true
        }
    },
    methods: {
        getJobDate(date) {
            if(!date)
                return 'present'

            return formatDate(date)
        }
    }
}
</script>

<style scoped>
.expierence {
    padding: 15px;
    width: 100%;
    max-width: 650px;
    background: var(--input-background-color);
    border: 1px solid var(--borders-color);
    border-radius: 15px;
    margin-bottom: 15px;
}
.expierence .exp-header {
    display: flex;
    margin-bottom: 20px;
}
.expierence .logo {
    width: 50px;
    height: 50px;
    border-radius: 5px;
    border: 1px solid var(--borders-color);
    margin-right: 15px;
    flex-shrink: 0;
    overflow: hidden;
}
.expierence h2 {
    margin-bottom: 5px !important;
}
.expierence .company {
    margin-bottom: 0px;
    font-weight: 500;
}
.expierence .date {
    font-size: 14px;
}
.expierence .exp-info {
    line-height: 1.4;
    margin-bottom: 20px;
}
.expierence .exp-skills {
    display: flex;
}
.expierence .exp-skills .exp-skills__title {
    font-weight: 500;
    margin-right: 10px;
    color: #a8b8c7;
}
.exp-skills__text {
    line-height: 1.3;
}
@media only screen and (max-width: 680px) {
    .expierence .exp-skills {
        display: block;
    }
    .exp-skills__title {
        margin-bottom: 5px;
    }
}
@media only screen and (max-width: 415px) {
    .exp-info,
    .exp-skills {
        font-size: 13px;
    }

    .expierence h2 {
        font-size: 14px !important;
    }
}
</style>