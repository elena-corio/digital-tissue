<template>
  <div class="login-center-container">
    <div class="login-tab-card">
      <h2 class="login-tab-title">{{ uiText.pages.login.authTab }}</h2>
      <div class="login-placeholder">
        <p>This login page is a placeholder for future authentication (e.g., Clerk).</p>
        <p>No token is required at this time.</p>
      </div>
    </div>
  </div>
</template>


<style scoped>
.login-center-container {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
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

.login-tab-btn {
  margin-top: var(--space-md);
  padding: var(--space-sm) var(--space-lg);
  border-radius: var(--radius-medium);
  border: none;
  background: var(--navy-blue-100);
  color: white;
  font-size: var(--font-size-body);
  width: 100%;
  font-weight: var(--font-weight-semibold);
  cursor: pointer;
  box-shadow: var(--shadow-sm);
}
.login-tab-btn:hover {
  background: var(--navy-blue-50);
}
</style>
