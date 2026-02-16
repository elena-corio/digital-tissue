<template>
  <div class="workspace-container">
    <div class="tabs">
      <router-link 
        to="/workspace/viewer" 
        class="tab"
        active-class="tab-active"
      >
        {{ uiText.pages.workspace.tabs.viewer }}
      </router-link>
      <router-link 
        to="/workspace/metrics" 
        class="tab"
        active-class="tab-active"
      >
        {{ uiText.pages.workspace.tabs.metrics }}
      </router-link>
      <router-link 
        to="/workspace/insight" 
        class="tab"
        active-class="tab-active"
      >
        {{ uiText.pages.workspace.tabs.insight }}
      </router-link>
    </div>
    
    <div class="workspace-content">
      <router-view />
    </div>
  </div>
</template>

<script setup>
import { uiText } from '@/config/uiText.js'
</script>

<style scoped>
.workspace-container {
  padding: var(--space-lg);
}

.tabs {
  display: flex;
  gap: var(--space-md);
  border-bottom: 2px solid var(--light-grey-100);
  margin-bottom: var(--space-lg);
}

.tab {
  padding: var(--space-md) var(--space-lg);
  text-decoration: none;
  color: var(--navy-blue-50);
  font-weight: var(--font-weight-medium);
  border-bottom: 3px solid transparent;
  transition: all 0.2s ease;
  position: relative;
  bottom: -2px;
}

.tab:hover {
  color: var(--navy-blue-100);
  background-color: var(--light-lila-50);
}

.tab-active {
  color: var(--fucsia-100);
  border-bottom-color: var(--fucsia-100);
}

.workspace-content {
  min-height: 400px;
}
</style>
