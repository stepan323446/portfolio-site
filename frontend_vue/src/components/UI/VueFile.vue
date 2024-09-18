<template>
    <RouterLink :class="{
        'file': true
    }" :to="{name: 'about', params: {slug: file.slug}}"><FontAwesomeIcon :icon="faFile" /> {{ file.name }}</RouterLink>
</template>

<script>
import { faFile } from '@fortawesome/free-solid-svg-icons';

export default {
    name: "VueFile",
    props: {
        file: {
            type: Object,
            required: true
        }
    },
    data() {
        return {
            faFile
        }
    },
}
</script>

<style scoped>
.file.router-link-active  {
    color: var(--active-text-color);
}
</style>