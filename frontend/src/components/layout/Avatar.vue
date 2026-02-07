<template>
  <div class="avatar-circle">
    <div class="avatar-body"></div>
    <div class="avatar-head" :style="{ background: headColor }"></div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const colors = [
  'var(--blue-100)',
  'var(--light-blue-100)',
  'var(--fucsia-100)',
  'var(--orange-100)'
]
const headColor = ref(colors[Math.floor(Math.random() * colors.length)])
</script>

<style scoped>
.avatar-circle {
  width: 34px;
  height: 34px;
  border-radius: 50%;
  background:  white;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  box-shadow: var(--shadow-sm);
}
.avatar-body {
  width: 24px;
  height: 12px;
  border-radius: 50%;
  background: var(--light-grey-100);
  position: absolute;
  bottom: 3px;
  left: 50%;
  transform: translateX(-50%);
}
.avatar-head {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  position: absolute;
  top: 6px;
  left: 50%;
  transform: translateX(-50%);
  box-shadow: 0 1px 2px rgba(0,0,0,0.08);
}
</style>
