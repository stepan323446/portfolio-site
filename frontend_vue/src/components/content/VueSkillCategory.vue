<template>
    <div v-if="category?.skills?.length > 0" class="skill-category">
        <h2># {{ category.title }} #</h2>
        <VueSkills :skills="category.skills" />
    </div>
</template>

<script>
export default {
    name: 'SkillCategory',
    props: {
        category: {
            type: Object,
            required: true
        }
    }
}
</script>

<style scoped>
.skill-category {
    padding: 15px;
    background: var(--input-background-color);
    border: 1px solid var(--borders-color);
    border-radius: 15px;
}
.skill-category h2 {
    text-align: center;
}
.skill-category >>> .items {
    justify-content: center;
}

</style>