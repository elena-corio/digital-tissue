<template>
  <div id="clerk-sign-in" />
</template>

<script setup>
import { onMounted } from 'vue'
onMounted(() => {
  if (window.Clerk && window.Clerk.mountSignIn) {
    window.Clerk.mountSignIn('#clerk-sign-in');
  } else {
    const interval = setInterval(() => {
      if (window.Clerk && window.Clerk.mountSignIn) {
        clearInterval(interval);
        window.Clerk.mountSignIn('#clerk-sign-in');
      }
    }, 50);
  }
})
</script>
