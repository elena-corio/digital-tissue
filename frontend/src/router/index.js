import { createRouter, createWebHistory } from 'vue-router'
import { useClerk } from '@/composables/useClerk.js'

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
    redirect: '/workspace/viewer',
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

// Navigation guard to protect routes requiring authentication
router.beforeEach(async (to, from, next) => {
  const { isSignedIn, initClerk } = useClerk()

  // Skip authentication in local development if VITE_SKIP_AUTH is set
  if (import.meta.env.VITE_SKIP_AUTH === 'true') {
    next()
    return
  }

  if (to.meta.requiresAuth) {
    try {
      await initClerk()
    } catch (error) {
      console.warn('Clerk initialization failed, redirecting to sign-in:', error)
      next({ name: 'sign-in', query: { redirect: to.fullPath } })
      return
    }

    if (!isSignedIn.value) {
      next({ name: 'sign-in', query: { redirect: to.fullPath } })
      return
    }
  }

  next()
})

export default router
