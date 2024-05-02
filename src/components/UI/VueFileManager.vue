<template>
    <div class="content-page">
        <aside class="sidebar">
            <slot name="sidebar"></slot>
        </aside>
        <div class="container">
            <div class="page-title">
                {{ title }}
            </div>
            <div class="content" v-if="!hasSeparate">
                <slot></slot>
            </div>
            <div class="content content-split" v-else>
                <div class="left scrollbar scrollbar-always">
                    <slot name="leftContent"></slot>
                </div>
                <div class="right scrollbar scrollbar-always">
                    <slot name="rightContent"></slot>
                </div>
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
        },
        hasSeparate: {
            type: Boolean,
            required: false,
            default: false
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
    overflow: auto;
}
.content::-webkit-scrollbar {
    width: 20px;
    padding: 3px;
    background-color: transparent;
    border-left: 2px solid var(--borders-color);
}
.content::-webkit-scrollbar-thumb {
    background-color: var(--text-color);
    background-clip: padding-box;
    border: 5px solid transparent;
    outline: 0;
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
@media only screen and (max-width: 1200px) {
    .content-page {
        flex-direction: column;
    }
    .sidebar {
        width: 100%;
        height: auto;
    }
    .sidebar-dropdown-btn {
        background: #1E2D3D;
    }
    .page-title {
        border: 2px solid var(--borders-color);
    }
    .content {
        height: auto;
        padding: 20px 10px;
    }
    .scrollbar::-webkit-scrollbar {
        width: 0;
    }
}
@media only screen and (max-width: 1000px) {
    .projects {
        grid-template-columns: repeat(2, 1fr);
        gap: 30px;
    }
}
@media only screen and (max-width: 715px) {
    .projects {
        grid-template-columns: repeat(1, 1fr);
        gap: 30px;
    }
    .content-split > .left,
    .content-split > .right {
        padding: 20px 14px;
    }
}
</style>