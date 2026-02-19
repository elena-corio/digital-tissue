<template>
  <div id="clerk-sign-in" />
</template>


<script setup>
import { onMounted } from 'vue'

onMounted(() => {
  const key = import.meta.env.VITE_CLERK_PUBLISHABLE_KEY
  if (window.Clerk && key) {
    window.Clerk.load({ publishableKey: key }).then(() => {
      window.Clerk.openSignIn({
        afterSignInUrl: '/workspace',
        afterSignUpUrl: '/workspace',
      })
    })
  }
})
</script>
