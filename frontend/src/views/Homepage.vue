<template>
  <div class="page-container homepage-center">
    <div class="homepage-content">
      <h1>{{ uiText.pages.homepage.title }}</h1>
      <h2>{{ uiText.pages.homepage.subtitle }}</h2>
      <div class="button-group">
        <button
          class="btn btn-primary get-started-btn"
          @click="handleGetStarted"
        >
          {{ uiText.pages.homepage.getStarted }}
        </button>
        <router-link to="/about" class="btn btn-secondary">
          {{ uiText.pages.homepage.learnMore }}
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { uiText } from '@/config/uiText.js'
import { useRouter } from 'vue-router'
import { useAuth } from '@clerk/vue'

const router = useRouter()
const { isSignedIn } = useAuth()

function handleGetStarted() {
  if (isSignedIn.value) {
    router.push({ name: 'workspace' })
  } else {
    router.push({ name: 'sign-in', query: { redirect: '/workspace' } })
  }
}
</script>

<style scoped>
.page-container.homepage-center {
  padding: var(--space-lg);

}

.homepage-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: var(--space-lg);
}

.button-group {
  display: flex;
  gap: var(--space-lg);
  margin-top: var(--space-md);
}

.get-started-btn.btn-disabled {
  background: var(--fucsia-50);
  color: white;
  cursor: pointer;
}
</style>