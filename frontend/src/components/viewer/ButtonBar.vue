<template>
  <div class="button-bar">
    <slot />
  </div>
</template>

<script setup>
// No logic needed for now
</script>

<style scoped>
.button-bar {
  display: flex;
  flex-direction: column;
  gap: 12px;
  align-items: center;
  justify-content: center;
  background: white;
  border-radius: 12px;
  box-shadow: var(--shadow-lg);
  padding: 12px 8px;
  width: 56px;
}
</style>
