import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { clerkPlugin } from '@clerk/vue'


import './assets/styles/globals.css'

const app = createApp(App)
app.use(router)
app.use(clerkPlugin, {
  publishableKey: import.meta.env.VITE_CLERK_PUBLISHABLE_KEY,
  signInUrl: '/digital-tissue/sign-in',
  signUpUrl: '/digital-tissue/sign-up',
  afterSignOutUrl: '/digital-tissue/sign-in'
})

// Handle GitHub Pages 404.html redirect for SPA routes
const urlParams = new URLSearchParams(window.location.search);
const redirectPath = urlParams.get('redirect');
if (redirectPath) {
  // Remove the ?redirect param from the URL
  window.history.replaceState({}, '', window.location.pathname.replace(/\?.*$/, ''));
  // Push the redirect path to the router
  router.replace(redirectPath);
}

app.mount('#app')
