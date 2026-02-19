<template>
  <div id="clerk-sign-up" />
</template>

<script setup>
import { onMounted } from 'vue'
onMounted(() => {
  if (window.Clerk && window.Clerk.mountSignUp) {
    window.Clerk.mountSignUp('#clerk-sign-up');
  } else {
    const interval = setInterval(() => {
      if (window.Clerk && window.Clerk.mountSignUp) {
        clearInterval(interval);
        window.Clerk.mountSignUp('#clerk-sign-up');
      }
    }, 50);
  }
})
</script>
