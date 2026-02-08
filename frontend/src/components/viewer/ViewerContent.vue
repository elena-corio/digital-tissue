<template>
  <div class="viewer-container">
    <slot />
  </div>
</template>

<script setup>
// No sidebar or buttons for now
</script>

<style scoped>
.viewer-container {
  width: 100%;
  height: 100%;
  min-height: 0;
  min-width: 0;
  max-width: 100vw;
  max-height: 100vh;
  position: relative;
  background: transparent;
  box-sizing: border-box;
  overflow: hidden;
  display: flex;
  align-items: stretch;
  justify-content: stretch;
}
html, body, #app {
  width: 100vw;
  height: 100vh;
  margin: 0;
  padding: 0;
  overflow: hidden;
  box-sizing: border-box;
}
</style>
