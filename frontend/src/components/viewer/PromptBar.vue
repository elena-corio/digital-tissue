<template>
<div class="prompt-bar">
  <div class="prompt-row">
    <label class="prompt-label">{{ uiText.promptBar.modelIdLabel }}</label>
    <input class="prompt-input" v-model="modelId" :placeholder="uiText.promptBar.modelIdPlaceholder" />
  </div>
  <button class="btn btn-tertiary prompt-btn" @click="emitUpdate">{{ uiText.promptBar.updateBtn }}</button>
</div>
</template>

<script setup>
import { defineEmits, defineProps, ref, watch } from 'vue';
import { uiText } from '@/config/uiText.js';
const emit = defineEmits(['update']);
const props = defineProps({
  modelId1: String
});

const modelId = ref(props.modelId1);

watch(() => props.modelId1, val => modelId.value = val);

function emitUpdate() {
  emit('update', { modelId1: modelId.value });
}
</script>

<style scoped>
.prompt-bar {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  padding: 24px 32px 0 32px;
  width: 100vw;
}
.prompt-row {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 12px;
  width: 100%;
}
.prompt-btn {
  margin-top: 12px;
  background-color: white;
  color: var(--navy-blue-100)
}
</style>
