<template>
    <div class="contactLinks">
        <a v-for="contact in contacts" :href="contact.url"><span class="icon" v-html="contact.icon_svg"></span> {{
            contact.name }}</a>
    </div>
</template>

<script>
import { mapGetters } from 'vuex';
export default {
    name: "VueContactLinks",
    computed: {
        ...mapGetters(['contacts'])
    }
}
</script>

<style scoped>
.contactLinks a {
    display: flex;
    margin-bottom: 10px
}

.contactLinks .icon {
    margin-right: 10px;
}

.contactLinks a {
    text-transform: lowercase;
    color: var(--text-color);
}

.contactLinks a:hover {
    color: var(--active-text-color);
}
.contactLinks >>> path {
    fill: var(--text-color);
}
.contactLinks a:hover >>> path {
    fill: var(--active-text-color);
}

</style>