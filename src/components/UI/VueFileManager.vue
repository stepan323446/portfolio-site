<template>
    <div class="content-page">
        <aside class="sidebar">
            <slot name="sidebar"></slot>
        </aside>
        <div class="container">
            <div class="page-title">
                {{ title }}
            </div>
            <div class="content">
                <slot></slot>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "VueFileManager",
    props: {
        title: {
            type: String,
            required: true
        }
    }
}
</script>

<style scoped>
    .sidebar {
    width: var(--sidebar-header-width);
    height: 100%;
    border-right: 2px solid var(--borders-color);
    flex-shrink: 0;
}
.sidebar >>> a {
    text-transform: lowercase;
    color: var(--text-color);
}
.sidebar >>> a:hover {
    color: var(--active-text-color);
}
.content-page {
    display: flex;
    height: calc(100vh - 53px - 50px);
}

.container {
    height: 100%;
    width: 100%;
}

.content h1 {
    color: var(--active-text-color);
    margin-bottom: 15px;
    font-size: 26px;
}
.content p {
    margin-bottom: 20px;
}
.text-content {
    line-height: 1.4;
}
.page-title {
    display: flex;
    align-items: center;
    justify-content: center;
    text-transform: lowercase;

    height: 39px;
    border-bottom: 2px solid var(--borders-color);
}
.content {
    width: 100%;
    height: calc(100% - 39px);
    padding: 20px 40px;
}
.content-split {
    display: flex;
    padding: 0;
}
.content-split > .left,
.content-split > .right {
    padding: 20px 40px;
    width: 50%;
}
.content > .left {
    border-right: 2px solid var(--borders-color);
}
</style>