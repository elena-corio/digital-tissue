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
router.beforeEach((to, from, next) => {
  const { isSignedIn } = useClerk()
  
  if (to.meta.requiresAuth && !isSignedIn.value) {
    // Redirect to sign-in if route requires auth and user is not signed in
    next({ name: 'sign-in' })
  } else {
    next()
  }
})

export default router
