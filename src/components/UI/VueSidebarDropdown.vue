<template>
    <div class="dropdown">
        <div 
        @click="changeState" 
        class="dropdown-btn sidebar-dropdown-btn" 
        :class="{
            'active': isActive
        }">
            <FontAwesomeIcon :icon="faCaretRight" /> {{ title }}
        </div>
        <div class="dropdown-content sidebar-content scrollbar" v-if="isActive">
            <slot></slot>
        </div>
    </div>
</template>

<script>
import { faCaretRight } from '@fortawesome/free-solid-svg-icons';

export default {
    name: "VueSidebarDropdown",
    props: {
        title: {
            type: String,
            required: true
        }
    },
    data() {
        return {
            faCaretRight,
            isActive: true
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
.sidebar-dropdown-btn,
.container .tab {
    padding: 10px 15px;
    color: var(--active-text-color);

    border-top: 2px solid var(--borders-color);
    border-bottom: 2px solid var(--borders-color);
    cursor: pointer;
    user-select: none;
}
.sidebar a {
    text-transform: lowercase;
    color: var(--text-color);
}
.sidebar a:hover {
    color: var(--active-text-color);
}
.dropdown:first-child .sidebar-dropdown-btn {
    border-top: 0;   
}
.sidebar-content {
    padding: 23px 16px;
}
.dropdown-btn > svg:first-child {
    transition: 0.15s ease;
}
.dropdown-btn.active > svg:first-child {
    transform: rotate(90deg);
}
@media only screen and (max-width: 1200px) {
    .sidebar-dropdown-btn {
        background: #1E2D3D;
    }
}
</style>