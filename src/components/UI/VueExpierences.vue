<template>
    <div class="expierence" v-for="item in expierences">
        <div class="exp-header">
            <div class="image image-cover logo">
                <img :src="`${item.image_url}`" alt="">
            </div>
            <div class="exp-header__info">
                <h2>## {{ item.name }}</h2>
                <div class="company">{{ item.company }}</div>
                <div class="date">{{ item.start_date }} - {{ item.end_date }}</div>
            </div>
        </div>
        <div class="exp-info">
            {{ item.descpr }}
        </div>

        <div class="exp-skills">
            <div class="exp-skills__title">
                skills:
            </div>
            <div class="exp-skills__text">
                {{ item.skills }}
            </div>
        </div>

    </div>
</template>

<script>
export default {
    name: "VueExpierences",
    props: {
        expierences: {
            type: Array,
            required: true
        }
    },
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
    margin-bottom: 5px;
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
</style>