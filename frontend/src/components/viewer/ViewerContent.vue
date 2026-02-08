<template>
  <div class="viewer-container aspect">
    <div class="button-bar-fixed">
      <slot name="toolbar" />
    </div>
    <slot />
  </div>
</template>

<script setup>
// Pure layout component: toolbar and content slots
</script>

<style scoped>
.viewer-container.aspect {
  aspect-ratio: 16 / 9;
  width: 100%;
  min-width: 0;
  min-height: 0;
  max-width: 100vw;
  max-height: 100vh;
  position: relative;
  background: transparent;
  box-sizing: border-box;
  overflow: hidden;
  display: flex;
  align-items: stretch;
  justify-content: stretch;
  box-shadow: var(--shadow-lg);
}
.button-bar-fixed {
  position: absolute;
  top: 110px;
  left: 32px;
  z-index: 10;
  width: auto;
  height: auto;
  pointer-events: none; /* Do not block viewer below */
}
.button-bar-fixed > * {
  pointer-events: auto; /* Buttons are clickable */
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
