import { createRouter, createWebHistory } from 'vue-router'
import IndexView from '@/views/Index'
import ProjectsView from '@/views/Projects'
import ContactView from '@/views/Contact'
import AboutView from '@/views/About.vue'

const titleConst = " - Stepan Turitsin";
const routes = [
  {
    path: '/',
    name: 'index',
    component: IndexView,
    meta: {
      title: "Stepan Turitsin - web developer"
    }
  },
  {
    path: '/about/:slug',
    name: 'about',
    component: AboutView,
    meta: {
      title: "Bio" + titleConst
    }
  },
  {
    path: '/projects',
    name: 'projects',
    component: ProjectsView,
    meta: {
      title: "Projects" + titleConst
    }
  },
  {
    path: '/contacts',
    name: 'contact',
    component: ContactView,
    meta: {
      title: "Contact me" + titleConst
    }
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});
router.beforeEach((to, from, next) => {
  document.title = to.meta.title;
  next();
});

export default router
