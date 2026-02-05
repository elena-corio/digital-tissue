<template>
  <header class="header">
    <div class="header-container">
      <div class="header-logo-wrapper">
        <img src="@/assets/images/logo.svg" alt="Digital Tissue Logo" class="header-logo" />
        <h1 class="header-title">{{ uiText.app.title }}</h1>
      </div>
    </div>
  </header>
</template>

<script setup>
import { uiText } from '@/config/uiText.js';
</script>

<style scoped>
.header {
  background-color: var(--navy-blue-100);
  color: white;
  padding: var(--space-md) 0;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.header-container {
  padding: 0 var(--space-lg);
}

.header-logo-wrapper {
  display: flex;
  align-items: center;
  gap: var(--space-md);
}

.header-logo {
  height: 2.5rem;
  width: auto;
}

.header-title {
  margin: 0;
  font-size: var(--font-size-h2);
  font-weight: var(--font-weight-bold);
}
</style>
