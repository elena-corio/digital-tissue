
<template>
  <button class="icon-btn" @click="$emit('click')" :title="title">
    <img :src="iconUrl" alt="icon" class="icon" />
  </button>
</template>

<script setup>
import { computed } from 'vue'
const props = defineProps({
  icon: { type: String, required: true },
  title: { type: String, default: '' }
})
const iconUrl = computed(() =>
  new URL(`../../assets/images/icons/${props.icon}`, import.meta.url).href
)
</script>

<style scoped>
.icon-btn {
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  background:white;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.2s;
  padding: 0;
  box-shadow: var(--shadow-md);
}
.icon-btn:hover {
  background:var(--light-grey-50);
}
.icon {
  width: 24px;
  height: 24px;
}
</style>
