<template>
    <a href="mailto:stevedekart2020@gmail.com"><FontAwesomeIcon :icon="faEnvelope" /> stevedekart2020@gmail.com</a>
</template>

<script>
import { faEnvelope } from '@fortawesome/free-solid-svg-icons';

export default {
    name: "VueContactLinks",
    data() {
        return {
            faEnvelope
        }
    }
}
</script>

<style scoped>
    
</style>