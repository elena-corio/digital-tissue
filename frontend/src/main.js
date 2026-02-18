import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { clerkPlugin } from '@clerk/vue'
import { CLERK_REDIRECTS } from '@/config/clerkRedirects.js'


import './assets/styles/globals.css'

const app = createApp(App)
app.use(router)
app.use(clerkPlugin, {
  publishableKey: import.meta.env.VITE_CLERK_PUBLISHABLE_KEY,
  signInUrl: CLERK_REDIRECTS.signInUrl,
  signUpUrl: CLERK_REDIRECTS.signUpUrl,
  afterSignOutUrl: CLERK_REDIRECTS.afterSignOutUrl,
  fallbackRedirectUrl: CLERK_REDIRECTS.fallbackRedirectUrl
})


app.mount('#app')
