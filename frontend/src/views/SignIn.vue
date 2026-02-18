<template>
  <div class="auth-container">
    <div class="auth-card">
      <div class="auth-header">
        <h1>Welcome Back</h1>
        <p>Sign in to access your workspace</p>
      </div>
      <div ref="signInContainer"></div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
// TODO: Integrate Clerk Vue SDK for sign-in widget

const signInContainer = ref(null);
// TODO: Use Clerk Vue SDK's <SignIn /> component or composable here
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
