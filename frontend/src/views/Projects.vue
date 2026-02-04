<template>
  <div class="page-container">
    <h1>{{ uiText.pages.projects.title }}</h1>
  </div>
</template>

<script setup>
import { uiText } from '@/config/uiText.js'
</script>

<style scoped>
.page-container {
  padding: var(--space-lg);
}
</style>
