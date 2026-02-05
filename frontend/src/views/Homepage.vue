<template>
  <div class="page-container">
    <div class="homepage-content">
      <h1>{{ uiText.pages.homepage.title }}</h1>
      <h2>{{ uiText.pages.homepage.subtitle }}</h2>
      <div class="button-group">
        <button class="btn btn-primary">
          {{ uiText.pages.homepage.getStarted }}
        </button>
        <button class="btn btn-secondary">
          {{ uiText.pages.homepage.learnMore }}
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { uiText } from '@/config/uiText.js'
</script>

<style scoped>
.page-container {
  padding: var(--space-lg);
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: calc(100vh - 80px);
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
</style>