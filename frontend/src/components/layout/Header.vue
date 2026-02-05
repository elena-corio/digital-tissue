<template>
  <header class="header">
    <div class="header-container">
      <div class="header-logo-wrapper">
        <img src="@/assets/images/logo.svg" alt="Digital Tissue Logo" class="header-logo" />
        <h1 class="header-title">{{ uiText.app.title }}</h1>
      </div>
            <button class="login-button">
        {{ uiText.navigation.login }}
      </button>
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

.login-button {
  background-color: var(--light-blue-100);
  color: white;
  padding: var(--space-sm) var(--space-lg);
  border-radius: var(--radius-medium);
  font-size: var(--font-size-body);
  font-weight: var(--font-weight-medium);
  transition: background-color 0.3s ease;
}

.login-button:hover {
  background-color: var(--light-blue-50);
}
</style>
