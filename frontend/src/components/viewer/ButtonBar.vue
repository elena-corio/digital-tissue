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
  background: rgba(255,255,255,0.95);
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  padding: 12px 8px;
  width: 56px;
}
</style>
