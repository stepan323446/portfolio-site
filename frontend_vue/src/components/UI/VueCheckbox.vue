<template>
    <div class="checkbox">
        <div :class="{
            'checkbox-input': true,
            'active': active
        }" @click="changeState">
            <FontAwesomeIcon :icon="faCheck" />
        </div>
        <input type="checkbox" :name="name" :id="id" project-target="skill-1">
        <label :for="id" @click="changeState">
            <slot></slot>
        </label>
    </div>

</template>

<script>
import { faCheck } from '@fortawesome/free-solid-svg-icons';
export default {
    name: "VueCheckbox",

    props: {
        defaultValue: {
            type: Boolean,
            default: false
        },
        name: {
            type: String,
            required: false
        }
    },
    data() {
        return {
            faCheck: faCheck,
            id: null,
            active: false
        }
    },
    methods: {
        changeState() {
            this.active = !this.active;
            this.$emit('state', this.active);
        }
    },
    mounted() {
        this.id = this._uid;
        this.active = this.$props.defaultValue;
    }
}
</script>

<style scoped>
.checkbox-input {
    display: inline-flex;
    justify-content: space-around;
    align-items: center;

    width: 16px;
    height: 16px;
    margin-right: 14px;
    border-radius: 3px;
    background: var(--input-background-color);
    border: 1px solid var(--text-color);
    cursor: pointer;
}

.checkbox-input.active {
    color: #000;
    background: var(--text-color);
}

.checkbox-input:not(.active) svg {
    display: none;
}

input[type="checkbox"] {
    display: none;
}
label {
    display: inline-flex;
    align-items: center;

    user-select: none;
    cursor: pointer;
}

</style>