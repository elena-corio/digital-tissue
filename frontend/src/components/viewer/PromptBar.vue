<template>
<div class="prompt-bar">
  <div class="prompt-row">
    <label class="prompt-label">{{ uiText.promptBar.modelIdLabel }}</label>
    <input class="form-input" v-model="modelId" :placeholder="uiText.promptBar.modelIdPlaceholder" />
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
}
.prompt-row {
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 12px;
  width: 100%;
  white-space: nowrap;
  overflow-x: auto;
}

.form-input {
  min-width: 0;
  flex: 1 1 0;
  white-space: nowrap;
  overflow-x: auto;
  text-overflow: ellipsis;
}
.prompt-btn {
  margin-top: 12px;
  background-color: white;
  color: var(--navy-blue-100);
  box-shadow: var(--shadow-md);
  transition: background 0.2s;
}
.prompt-btn:hover {
  background:var(--light-grey-50);
}
</style>
