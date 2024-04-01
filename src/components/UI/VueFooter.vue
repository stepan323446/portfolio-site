<template>
    <footer class="footer">
        <div class="text">
            find me in:
        </div>
        <a href="https://www.linkedin.com/in/stepan-turitsin-009354243/" target="_blank">
            <FontAwesomeIcon :icon="faLinkedin" />
        </a>
        <a href="https://stackoverflow.com/users/13722200" target="_blank">
            <FontAwesomeIcon :icon="faStackOverflow" />
        </a>
        <a href="https://github.com/stepan323446" target="_blank"><span>@stepan323446 </span>
            <FontAwesomeIcon :icon="faGithub" />
        </a>

    </footer>
</template>

<script>
import { faGithub, faStackOverflow, faLinkedin } from '@fortawesome/free-brands-svg-icons';

export default {
    name: 'VueFooter',

    data() {
        return {
            faGithub,
            faStackOverflow,
            faLinkedin
        }
    }
}
</script>

<style scoped>
footer a:hover {
    color: var(--active-text-color);
}
footer a {
    display: inline-block;
    text-decoration: none;
    color: var(--text-color);
}
.footer {
    display: flex;
    border-top: 2px solid var(--borders-color);
}

.footer>* {
    border-right: 2px solid var(--borders-color);
    padding: 14px 22px;
}

.footer>*:last-child {
    border-left: 2px solid var(--borders-color);
    margin-left: auto;
}
@media only screen and (max-width: 1200px) {
    .footer > *:last-child span {
        display: none;
    }
}
</style>