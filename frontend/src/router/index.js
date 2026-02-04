import { createRouter, createWebHistory } from 'vue-router';
import Homepage from '../views/Homepage.vue';
import Projects from '../views/Projects.vue';
import Workspace from '../views/Workspace.vue';

const routes = [
  {
    path: '/',
    name: 'Homepage',
    component: Homepage
  },
  {
    path: '/projects',
    name: 'Projects',
    component: Projects
  },
  {
    path: '/workspace',
    name: 'Workspace',
    component: Workspace
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
});

export default router;
