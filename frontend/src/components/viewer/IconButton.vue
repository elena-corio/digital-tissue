<template>
  <button class="icon-btn" @click="$emit('click')">
    <img :src="icon" alt="icon" class="icon" />
  </button>
</template>

<script setup>
defineProps({
  icon: { type: String, required: true }
})
</script>

<style scoped>
.icon-btn {
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #fff;
  border: 1px solid #eee;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.2s;
  padding: 0;
}
.icon-btn:hover {
  background: #f0f0f0;
}
.icon {
  width: 24px;
  height: 24px;
}
</style>
