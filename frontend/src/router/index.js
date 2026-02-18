import { createRouter, createWebHistory } from 'vue-router'

import Homepage from '@/views/Homepage.vue'
import Workspace from '@/views/Workspace.vue'
import About from '@/views/About.vue'
import SignIn from '@/views/SignIn.vue'
import SignUp from '@/views/SignUp.vue'

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
    path: '/sign-in',
    name: 'sign-in',
    component: SignIn
  },
  {
    path: '/sign-up',
    name: 'sign-up',
    component: SignUp
  },
  {
    path: '/workspace',
    name: 'workspace',
    component: Workspace,
    redirect: { name: 'workspace-viewer' },
    meta: { requiresAuth: true },
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
  }
]


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

const isAuthBypassEnabled = import.meta.env.DEV && import.meta.env.VITE_SKIP_AUTH === 'true'

router.beforeEach(async (to, from, next) => {
  // Skip authentication only in development when explicitly enabled
  if (isAuthBypassEnabled) {
    next()
    return
  }



  next()
})

export default router
