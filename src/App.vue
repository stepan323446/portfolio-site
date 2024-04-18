<template>
  <VueHeader />
  <div class="page">
    <RouterView/>
  </div>
  
  <VueFooter/>
</template>


<script>
import VueHeader from '@/components/UI/VueHeader';
import VueFooter from '@/components/UI/VueFooter';

export default {
  components: {
    VueHeader, VueFooter
  }
}
</script>

<style>
@import url('./assets/css/reset.css');
@import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500&display=swap');

:root {
  --background-body: #011627;
  --borders-color: #1E2D3D;

  --index-title-color: #E5E9F0;

  --active-text-color: #fff;
  --text-color: #607B96;

  --input-background-color: #011221;
  --input-color: #465E77;

  --btn-bg-color: #1C2B3A;
  --btn-font-color: #fff;

  --btn-bg-hover-color: #505ed1;
  --btn-font-hover-color: #fff;

  --btn-primary-bg-color: var(--accent);
  --btn-primary-font-color: #01080E;

  --sidebar-header-width: 300px;

  --accent: #FEA55F;
  --accent-2: #43D9AD;
  --accent-3: #4D5BCE;

}

*:not(i) {
  box-sizing: border-box;
  font-family: 'Fira Code', monospace;
}

*[hidden] {
  display: none !important;
}

a {
  color: var(--accent);
  text-decoration: none;
}

a:hover {
  color: var(--accent-2);
}

body {
  background: var(--background-body);
  color: var(--text-color);
}

.scrollbar {
  overflow-y: auto;
}

.scrollbar::-webkit-scrollbar {
  width: 20px;
  padding: 3px;
  background-color: transparent;
  border-left: 2px solid var(--borders-color);
}

.scrollbar::-webkit-scrollbar-thumb {
  background-color: var(--text-color);
  background-clip: padding-box;
  border: 5px solid transparent;
  outline: 0;
}

.scrollbar.scrollbar-always {
  overflow-y: scroll;
}

.image img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

.image-cover img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.page {
    height: calc(100vh - 53px - 50px);
}
.inside-block {
    background: var(--input-background-color);
    border-radius: 15px;
}
.hljs {
    font-weight: 500;
    line-height: 1.6;
}
.hljs-comment {
    color: var(--text-color);
}
.hljs-keyword {
    color: #4D5BCE;
}
.hljs-string {
    color: #E99287;
}
.hljs-ln-numbers {
    color: var(--text-color);
    padding-right: 40px !important;
}

.function_ {
    color: #d1ca6d;
}
.hljs-attr {
    color: #a7a7a7;
}

@media only screen and (max-width: 1200px) {
  .scrollbar-alway {
        overflow-y: auto;
    }
    body {
        overflow: auto;
        padding-top: 51px;
    }
    pre {
        text-wrap: balance;
    }
    .page {
        height: calc(100vh - 53px);
    }
}
</style>
