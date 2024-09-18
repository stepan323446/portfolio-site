<template>
    <div class="content-page">
        <aside class="sidebar scrollbar">
            <slot name="sidebar"></slot>
        </aside>
        <div class="container">
            <div class="page-title">
                {{ title }}
            </div>
            <div class="content" v-if="!hasSeparate" v-show="!loadingContent">
                <slot></slot>
            </div>
            <div class="content content-split" v-else v-show="!loadingContent">
                <div class="left scrollbar scrollbar-always">
                    <slot name="leftContent"></slot>
                </div>
                <div class="right scrollbar scrollbar-always">
                    <slot name="rightContent"></slot>
                </div>
            </div>
            <div class="content loading-content" v-show="loadingContent">
                <div class="loading-wrapper">
                    <div class="loading-title">
                        Just a second...
                    </div>
                    <div class="loading-bar"></div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { mapGetters } from 'vuex';

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
    },
    computed: {
        ...mapGetters(['loadingContent'])
    }
}
</script>

<style scoped>
@keyframes slide {
    from {
        background-position-x: 0;
    }

    to {
        background-position-x: var(--fundamentalBase);
    }
}
.loading-content {
    display: flex;
    justify-content: center;
}
.loading-wrapper {
    text-align: center;
    max-width: 700px;
    width: 100%;
    margin-top: 30px;
}
.loading-bar {
    min-height: 10px;
    border-radius: 10px;
    width: 100%;

    box-shadow: 0px 10px 13px -6px rgba(44, 62, 80, 1);
    background-color: var(--colour2);
    background-image: repeating-linear-gradient(45deg,
            transparent,
            transparent calc(var(--stripeWidth) / 2),
            var(--colour1) calc(var(--stripeWidth) / 2),
            var(--colour1) var(--stripeWidth));

    animation: slide var(--speed) linear infinite;
    will-change: background-position;
}
.loading-title {
    margin-bottom: 20px;
}

.sidebar {
    width: var(--sidebar-header-width);
    height: 100%;
    border-right: 2px solid var(--borders-color);
    flex-shrink: 0;
    overflow: auto;
}

.sidebar>>>a {
    text-transform: lowercase;
    color: var(--text-color);
}

.sidebar>>>a path {
    fill: var(--text-color);
}

.sidebar>>>a:hover {
    color: var(--active-text-color);
}

.sidebar>>>a:hover path {
    fill: var(--active-text-color);
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
    padding: 20px 40px;
    overflow: auto;

    height: calc(100% - 39px);
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

.content-split>.left,
.content-split>.right {
    padding: 20px 40px;
    width: 50%;
}

.content>.left {
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

    .content-split>.left,
    .content-split>.right {
        padding: 20px 14px;
    }
}
</style>