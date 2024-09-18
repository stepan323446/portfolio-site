<template>
    <RouterLink v-if="to" :to="to" class="btn">
        <slot></slot>
    </RouterLink>
    
    <a v-else-if="href" :href="href">
        <slot></slot>
    </a>

    <button v-else class="btn">
        <slot></slot>
    </button>
</template>

<script>
export default {
    name: "VueButton",
    data() {
        return { }
    },
    props: {
        to: {
            type: Object,
            required: false
        },
        href: {
            type: String,
            required: false
        }
    }
}
</script>

<style scoped>
.btn {
    color: var(--btn-font-color);
    font-weight: 500;
    font-size: 14px;
    text-wrap: nowrap;
    padding: 10px 14px;
    border-radius: 8px;
    background: var(--btn-bg-color);
    border: 0;
    user-select: none;
    cursor: pointer;
}
.btn-primary {
    color: var(--btn-primary-font-color);
    background: var(--btn-primary-bg-color);
}
.btn:hover:not(:disabled) {
    color: var(--btn-font-hover-color);
    background: var(--btn-bg-hover-color);
}
.btn:disabled {
    opacity: 0.5;
    cursor: progress;
}
</style>