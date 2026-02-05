<template>
  <div class="page-container">
    <div class="homepage-content">
      <h1>{{ uiText.pages.homepage.title }}</h1>
      <h2>{{ uiText.pages.homepage.subtitle }}</h2>
    </div>
  </div>
</template>

<script setup>
import { uiText } from '@/config/uiText.js'
</script>

<style scoped>
.page-container {
  padding: var(--space-lg);
}

.homepage-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  gap: var(--space-lg);
  margin-top: var(--space-xl);
}
</style>