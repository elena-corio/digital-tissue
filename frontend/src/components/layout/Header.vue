<template>
  <header class="header">
    <div class="header-container">
      <router-link to="/" class="header-logo-wrapper">
        <img :src="logoSrc" alt="Digital Tissue Logo" class="header-logo" />
        <h2 class="header-title">{{ uiText.app.title }}</h2>
      </router-link>
      <template v-if="isSignedIn">
        <div class="header-avatar-logout">
          <Avatar class="header-avatar" />
          <button @click="handleSignOut" class="btn btn-tertiary">
            Sign Out
          </button>
        </div>
      </template>
      <router-link v-else to="/sign-in" class="btn btn-tertiary">
        Sign In
      </router-link>
    </div>
  </header>
</template>

<script setup>
import { useClerk } from '@/composables/useClerk.js';
import { uiText } from '@/config/uiText.js';
import logoSrc from '@/assets/images/logo.svg';
import Avatar from '@/components/layout/Avatar.vue';

const { isSignedIn, signOut } = useClerk();

const handleSignOut = async () => {
  const baseUrl = import.meta.env.BASE_URL;
  await signOut({ redirectUrl: baseUrl });
};
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
  color: white
}

.header-avatar-logout {
  display: flex;
  align-items: center;
  gap: var(--space-md);
}

.header-avatar {
  margin-right: var(--space-sm);
}
</style>
