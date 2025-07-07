<template>
<div class="avatar" :style="{ backgroundImage: `url(${url})` }"></div>
</template>

<script>
export default {
    name: "Avatar",
    props: {
        url: {
            type: String,
            required: true
        }
    }
}
</script>

<style scoped>
.avatar {
    background-size: cover;
    width: 40px;
    height: 40px;
    border: 2px solid #fff;
    border-radius: 100%;
}
</style>