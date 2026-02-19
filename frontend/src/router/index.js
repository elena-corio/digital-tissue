import { createRouter, createWebHistory } from 'vue-router'
import { useClerk } from '@/composables/useClerk'

import Homepage from '@/views/Homepage.vue'
import Workspace from '@/views/Workspace.vue'
import About from '@/views/About.vue'
import Login from '@/views/Login.vue'

const routes = [
  {
    path: '/',
    name: 'homepage',
    component: Homepage
  },
  {
    path: '/about',
    name: 'about',
    component: About
  },
  {
    path: '/workspace',
    name: 'workspace',
    component: Workspace,
    redirect: '/workspace/viewer',
    children: [
      {
        path: 'viewer',
        name: 'workspace-viewer',
        component: () => import('@/views/workspace/Viewer.vue')
      },
      {
        path: 'metrics',
        name: 'workspace-metrics',
        component: () => import('@/views/workspace/Metrics.vue')
      },
      {
        path: 'insight',
        name: 'workspace-insight',
        component: () => import('@/views/workspace/Insight.vue')
      }
    ]
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  }
]



const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

// Clerk route protection (no wrapper, no hash)
router.beforeEach(async (to, from, next) => {
  const { requireAuth } = useClerk();
  // Only protect routes with meta.requiresAuth
  if (to.matched.some(r => r.meta && r.meta.requiresAuth)) {
    await requireAuth(router, to, next);
    return;
  }
  next();
});

export default router
