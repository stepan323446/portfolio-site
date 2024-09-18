<template>
    <div class="folder">
        <div @click="changeState" class="folder-title" :class="{
            'active': !isActive
        }">
            <FontAwesomeIcon :icon="faChevronDown" /> <FontAwesomeIcon :icon="faFolder" /> {{ title }}
        </div>
        <div class="folder-content" v-if="isActive">
            <slot></slot>
        </div>
    </div>
</template>

<script>
import { faChevronDown, faFolder } from '@fortawesome/free-solid-svg-icons';

export default {
    name: "VueFolder",

    props: {
        title: {
            type: String,
            required: true
        },
        initialActive: {
            type: Boolean,
            default: true
        }
    },
    data() {
        return {
            faChevronDown,
            faFolder,

            isActive: this.$props.initialActive
        }
    },
    methods: {
        changeState() {
            this.isActive = !this.isActive;
        }
    }
}
</script>

<style scoped>
.folder {
    user-select: none;
}
.folder .folder-title {
    cursor: pointer;
}
.folder .folder-title:hover {
    color: #fff;
}
.folder.folder-1 .fa-folder {
    color: var(--accent);
}
.folder.folder-2 .fa-folder {
    color: var(--accent-2);
}
.folder.folder-3 .fa-folder {
    color: var(--accent-3);
}
.folder-content {
    margin-bottom: 6px;
    padding: 10px 0 0 40px;
}

.folder-title.active > .fa-chevron-down {
    transform: rotate(90deg);
}
.folder-title.active .fa-chevron-down {
    transform: rotate(-90deg) !important;
}
.folder-content.active {
    height: auto;
}
.folder-content ul {
    list-style: none;
    padding: 10px 0 0 40px;
}
</style>