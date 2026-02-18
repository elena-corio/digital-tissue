<template>
  <div class="auth-container">
    <div class="auth-card">
      <div class="auth-header">
        <h1>Create Account</h1>
        <p>Sign up to get started with Digital Tissue</p>
      </div>
      <SignUp routing="vue" />
    </div>
  </div>
</template>

<script setup>
import { SignUp } from '@clerk/vue';
</script>

<style scoped>
.auth-container {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: var(--background-color);
  padding: var(--space-lg);
}

.auth-card {
  width: 100%;
  max-width: 480px;
  background: white;
  border-radius: var(--radius-medium);
  box-shadow: var(--shadow-lg);
  padding: var(--space-xl);
}
</style>