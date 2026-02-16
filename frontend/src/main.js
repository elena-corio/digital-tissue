import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { clerkPubKey } from '@/config/clerk.js'
import { useClerk } from '@/composables/useClerk.js'

import './assets/styles/globals.css'

if (!clerkPubKey) {
  throw new Error('Missing Clerk publishable key')
}

const bootstrap = async () => {
  const { initClerk } = useClerk()

  try {
    await initClerk()
  } catch (error) {
    console.error('Failed to initialize Clerk:', error)
  }

  const app = createApp(App)
  app.use(router)
  app.mount('#app')
}

bootstrap()
