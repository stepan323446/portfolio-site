<template>
    <header class="header">
        <div class="header__inner">
            <div class="header-title">
                stepan-turitsin
            </div>
            <nav class="header-nav">
                <ul>
                    <li>
                        <RouterLink :to="{name: 'index'}">_hello</RouterLink>
                    </li>
                    <li>
                        <RouterLink :to="{name: 'about', params: {slug: 'bio'}}" :class="{
                            'active': $route.name == 'about'
                        }">_about-me</RouterLink>
                    </li>
                    <li>
                        <RouterLink :to="{name: 'projects'}">_projects</RouterLink>
                    </li>
                    <li>
                        <RouterLink :to="{name: 'contact'}">_contact-me</RouterLink>
                    </li>
                </ul>
            </nav>
            <div id="mobile-btn" class="burger-menu">
                <FontAwesomeIcon :icon="faBars"/>
                <FontAwesomeIcon :icon="faX" />
            </div>
        </div>
    </header>
</template>

<script>
import { faBars, faX }  from "@fortawesome/free-solid-svg-icons";


export default {
    name: "VueHeader",
    data() {
        return {
            faBars,
            faX
        }
    }
}
</script>

<style scoped>
header {
    font-size: 16px;
}
.burger-menu {
    display: none;
}

.header__inner,
.header-nav ul {
    display: flex;
}

header a,
footer a {
    display: inline-block;
    text-decoration: none;
    color: var(--text-color);
}

.header-title,
.header a {
    position: relative;
    padding: 17px 32px;
    border-right: 2px solid var(--borders-color);
}

.header li:last-child a {
    border-left: 2px solid var(--borders-color);
}

.header a.router-link-active,
.header a.active {
    color: var(--active-text-color);
}

.header a.router-link-active::before,
.header a.active::before {
    content: '';
    position: absolute;

    width: 100%;
    height: 3px;
    background: var(--accent);
    left: 0;
    bottom: 0;
}

.header a:hover {
    color: var(--active-text-color);
}

.header-nav {
    width: 100%;
}

header li:last-child {
    margin-left: auto;
}

.header-title {
    width: var(--sidebar-header-width);
    flex-shrink: 0;
}

header {
    border-bottom: 2px solid var(--borders-color);
}

@media only screen and (max-width: 1200px) {
    header {
        position: fixed;
        left: 0;
        top: 0;
        width: 100%;
        z-index: 999;
        background: var(--background-body);
    }
    .header-title {
        width: auto;
        border-right: 0;
    }
    .header__inner {
        position: relative;
        justify-content: space-between;
    }
    .burger-menu {
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 23px;
        width: 50px;
    }
    .burger-menu .fa-x {
        display: none;
    }
    .burger-menu.active .fa-x {
        font-size: 16px;
        display: inline;
    }
    .burger-menu.active .fa-bars {
        display: none;
    }
    .header-nav {
        display: none;
    }
    .header-nav.active {
        position: fixed;
        display: block;
        margin-top: 52px;
        height: calc(100% - 51px - 47px);
        z-index: 999;
        background: var(--background-body);
    }
    .header-nav ul {
        flex-direction: column;
    }
    .header-nav a {
        color: var(--active-text-color);
        width: 100%;
        border-right: 0;
        border-bottom: 1px solid var(--borders-color);
    }
    .header a.active::before {
        width: 7px;
        height: 100%;
    }
    header li:last-child {
        margin-left: 0;
    }
}
</style>