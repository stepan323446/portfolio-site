<template>
    <button class="btn">
        <slot></slot>
    </button>
</template>

<script>
export default {
    name: "VueButton"
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
.btn:hover {
    color: var(--btn-font-hover-color);
    background: var(--btn-bg-hover-color);
}
</style>