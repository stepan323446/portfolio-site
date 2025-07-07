<template>
    <div class="items">
        <div v-for="contrib in contributors" :key="contrib.id" class="item inside-block">
            <div class="item-header">
                <Avatar :url="contrib.avatar" />
                <a :href="contrib.url" target="_blank" class="item-title">{{ contrib.name }}</a>
            </div>
            <div class="item-description">
                {{ contrib.description }}
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "VueContributors",
    props: {
        contributors: {
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
    border: 2px solid var(--borders-color);
    padding: 10px;
    margin-right: 15px;
    margin-bottom: 15px;
}
.item-header {
    display: flex;
    align-items: center;
    margin-bottom: 14px;
}
.item-title {
    margin-left: 15px;
}
</style>