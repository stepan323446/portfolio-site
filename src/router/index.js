import { createRouter, createWebHistory } from 'vue-router'
import IndexView from '@/views/Index'
import ProjectsView from '@/views/Projects'
import ContactView from '@/views/Contact'
import AboutView from '@/views/About.vue'

const routes = [
  {
    path: '/',
    name: 'index',
    component: IndexView
  },
  {
    path: '/about',
    name: 'about',
    component: AboutView
  },
  {
    path: '/projects',
    name: 'projects',
    component: ProjectsView
  },
  {
    path: '/contacts',
    name: 'contact',
    component: ContactView
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
