<template>
  <div class="login-center-container">
    <div class="login-tab-card">
      <h2 class="login-tab-title">{{ uiText.pages.login.authTab }}</h2>
      <form class="login-tab-form" @submit.prevent="handleLogin">
        <label class="login-tab-label">{{ uiText.pages.login.usernameLabel }}</label>
        <input v-model="username" type="text" class="login-tab-input" :placeholder="uiText.pages.login.usernamePlaceholder" />
        <label class="login-tab-label">{{ uiText.pages.login.tokenLabel }}</label>
        <input v-model="token" type="password" class="login-tab-input" :placeholder="uiText.pages.login.tokenPlaceholder" required />
        <button type="submit" class="login-tab-btn">{{ uiText.pages.login.loginBtn }}</button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { uiText } from '@/config/uiText.js'
import { useRouter } from 'vue-router'
import { login } from '@/store/auth.js'

const username = ref('')
const token = ref('')

const router = useRouter()

const handleLogin = () => {
  login(token.value, username.value)
  router.push({ name: 'homepage' })
}
</script>

<style scoped>
.login-center-container {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--light-lila-50);
  margin: 0;
  padding: 0;
  overflow: hidden;
}

.login-tab-card {
  background: white;
  border-radius: var(--radius-large);
  box-shadow: var(--shadow-lg);
  padding: var(--space-xl) var(--space-lg);
  min-width: 320px;
  max-width: 400px;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.login-tab-title {
  font-size: var(--font-size-h2);
  font-weight: var(--font-weight-bold);
  margin-bottom: var(--space-lg);
  color: var(--navy-blue-100);
}

.login-tab-form {
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: var(--space-md);
}

.login-tab-label {
  font-size: var(--font-size-body);
  color: var(--navy-blue-100);
  margin-bottom: 0.25rem;
}

.login-tab-input {
  padding: var(--space-sm);
  border-radius: var(--radius-small);
  border: 1px solid var(--light-grey-100);
  font-size: var(--font-size-body);
  background: var(--light-lila-50);
  margin-bottom: 0.5rem;
}

.login-tab-btn {
  margin-top: var(--space-md);
  padding: var(--space-sm) var(--space-lg);
  border-radius: var(--radius-medium);
  border: none;
  background: var(--navy-blue-100);
  color: white;
  font-size: var(--font-size-body);
  font-weight: var(--font-weight-semibold);
  cursor: pointer;
  box-shadow: var(--shadow-sm);
}
.login-tab-btn:hover {
  background: var(--navy-blue-50);
}

.login-tab-note {
  font-size: var(--font-size-small);
  color: var(--color-info);
  margin-bottom: 0.5rem;
}
</style>
