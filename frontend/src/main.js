import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { clerkPlugin } from '@clerk/vue'


import './assets/styles/globals.css'

const app = createApp(App)
app.use(router)
app.use(clerkPlugin, {
  publishableKey: import.meta.env.VITE_CLERK_PUBLISHABLE_KEY
})
app.mount('#app')
