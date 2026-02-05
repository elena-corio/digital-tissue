<template>
  <header class="header">
    <div class="header-container">
      <router-link to="/" class="header-logo-wrapper">
        <img src="@/assets/images/logo.svg" alt="Digital Tissue Logo" class="header-logo" />
        <h1 class="header-title">{{ uiText.app.title }}</h1>
      </router-link>
      <router-link to="/login" class="btn btn-tertiary">
        {{ uiText.navigation.login }}
      </router-link>
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
  box-shadow: var(--shadow-md);
}

.header-container {
  padding: 0 var(--space-lg);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.header-logo-wrapper {
  display: flex;
  align-items: center;
  gap: var(--space-md);
  text-decoration: none;
  color: inherit;
  transition: opacity 0.3s ease;
}

.header-logo-wrapper:hover {
  opacity: 0.75;
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
