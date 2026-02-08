<template>
  <div class="viewer-container aspect">
    <ButtonBar class="button-bar-fixed">
      <IconButton icon="/src/assets/images/icons/dna.svg" @click="$emit('measure')" />
      <IconButton icon="/src/assets/images/icons/network.svg" @click="$emit('section')" />
      <IconButton icon="/src/assets/images/icons/synapses.svg" @click="$emit('filter')" />
    </ButtonBar>
    <slot />
  </div>
</template>

<script setup>
import ButtonBar from './ButtonBar.vue';
import IconButton from './IconButton.vue';
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
