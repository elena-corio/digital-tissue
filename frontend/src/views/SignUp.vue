<template>
  <div class="auth-container">
    <div class="auth-card">
      <div class="auth-header">
        <h1>Create Account</h1>
        <p>Sign up to get started with Digital Tissue</p>
      </div>
      <div ref="signUpContainer"></div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
// TODO: Integrate Clerk Vue SDK for sign-up widget

const signUpContainer = ref(null);
// TODO: Use Clerk Vue SDK's <SignUp /> component or composable here
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

.auth-header {
  text-align: center;
  margin-bottom: var(--space-xl);
}

.auth-header h1 {
  font-size: var(--font-size-h1);
  font-weight: var(--font-weight-bold);
  color: var(--navy-blue-100);
  margin-bottom: var(--space-sm);
}

.auth-header p {
  font-size: var(--font-size-body);
  color: var(--navy-blue-50);
}
</style>
