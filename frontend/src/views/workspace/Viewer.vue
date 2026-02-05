<template>
  <div class="viewer-container">
    <h2>{{ uiText.pages.workspace.viewer.title }}</h2>
    <p>{{ uiText.pages.workspace.viewer.subtitle }}</p>
    <!-- Model viewer content will go here -->
  </div>
</template>

<script setup>
import { uiText } from '@/config/uiText.js';
</script>

<style scoped>
.viewer-container {
  padding: var(--space-lg);
}
</style>
