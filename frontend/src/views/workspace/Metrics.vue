<template>
  <div class="metrics-container">
    <h2>{{ uiText.pages.workspace.metrics.title }}</h2>
    <p>{{ uiText.pages.workspace.metrics.subtitle }}</p>
    <!-- Performance metrics content will go here -->
  </div>
</template>

<script setup>
import { uiText } from '@/config/uiText.js';
</script>

<style scoped>
.metrics-container {
  padding: var(--space-lg);
}
</style>
