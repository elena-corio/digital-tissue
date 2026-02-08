<template>
  <div class="prompt-bar">
    <label>
      {{ uiText.promptBar.projectIdLabel }}
      <input v-model="projectId" :placeholder="uiText.promptBar.projectIdPlaceholder" />
    </label>
    <label>
      {{ uiText.promptBar.modelId1Label }}
      <input v-model="modelId1" :placeholder="uiText.promptBar.modelId1Placeholder" />
    </label>
    <label>
      {{ uiText.promptBar.modelId2Label }}
      <input v-model="modelId2" :placeholder="uiText.promptBar.modelId2Placeholder" />
    </label>
    <button class="btn btn-tertiary" @click="emitUpdate">{{ uiText.promptBar.updateBtn }}</button>
  </div>
</template>

<script setup>
import { defineEmits, defineProps, ref, watch } from 'vue';
import { uiText } from '@/config/uiText.js';
const emit = defineEmits(['update']);
const props = defineProps({
  projectId: String,
  modelId1: String,
  modelId2: String
});

const projectId = ref(props.projectId);
const modelId1 = ref(props.modelId1);
const modelId2 = ref(props.modelId2);

watch(() => props.projectId, val => projectId.value = val);
watch(() => props.modelId1, val => modelId1.value = val);
watch(() => props.modelId2, val => modelId2.value = val);

function emitUpdate() {
  emit('update', { projectId: projectId.value, modelId1: modelId1.value, modelId2: modelId2.value });
}
</script>

<style scoped>
.prompt-bar {
  display: flex;
  gap: 16px;
  align-items: center;
  padding: 24px 32px 0 32px;
  width: 100vw;
}
.prompt-bar label {
  display: flex;
  flex-direction: column;
  font-size: 14px;
}
.prompt-bar input {
  margin-top: 4px;
  padding: 6px 10px;
  border-radius: 6px;
  border: 1px solid #ccc;
  font-size: 14px;
}
/* Remove prompt-bar button override so .btn.btn-tertiary global style applies */
</style>
