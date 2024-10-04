<template>
    <VueFileManager title="Error 404 - page not found">
        <slot>
            <div class="not-found-page">
                <h1>404</h1>
                <h2>Page not found</h2>
            </div>
        </slot>
    </VueFileManager>
</template>

<script>
    import VueFileManager from '@/components/UI/VueFileManager';
    export default {
        components: { VueFileManager },
    }
</script>

<style scoped>
    .not-found-page {
        height: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .not-found-page h1 {
        display: block;
        font-size: 64px;
        margin-bottom: 10px;
    }
    .not-found-page h2 {
        display: block;
    }
</style>