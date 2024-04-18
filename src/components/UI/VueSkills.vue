<template>
    <div class="items">
        
        <div class="item inside-block" v-for="item in skills">
            <div class="image"><img :src="`${item.icon}`" alt=""></div>
            <span>Wordpress</span>
        </div>
    </div>
</template>

<script>
export default {
    name: "VueSkills",
    props: {
        skills: {
            type: Array,
            required: true
        }
    }
}
</script>

<style scoped>
    .items {
        display: flex;
        flex-wrap: wrap;
    }
    .item {
        display: flex;
        align-items: center;
        border: 2px solid var(--borders-color);
        padding: 10px;
        margin-right: 15px;
        margin-bottom: 15px;
    }
    .image {
        width: 30px;
        height: 30px;
        margin-right: 10px;
        flex-shrink: 0;
    }
</style>