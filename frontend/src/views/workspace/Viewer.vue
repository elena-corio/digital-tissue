<template>
  <div class="viewer-page">
    <div class="viewer-grid">
      <ViewerPanel 
        v-model:modelId="inputModelId1"
        :projectId="projectId"
      />
      <ViewerPanel 
        v-model:modelId="inputModelId2"
        :projectId="projectId"
      />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

import ViewerPanel from '@/components/viewer/ViewerPanel.vue';
import { viewerModels } from '@/config/modelConfig.js';

const projectId = viewerModels.structure.projectId;
const inputModelId1 = ref(viewerModels.structure.modelId);
const inputModelId2 = ref(viewerModels.program.modelId);
</script>

<style scoped>
.viewer-page {
  padding: 0;
  margin: 0;
  width: 100vw;
  height: 100vh;
  min-height: 0;
  min-width: 0;
  box-sizing: border-box;
  overflow-x: hidden;
  overflow-y: hidden;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
}
.viewer-grid {
  display: flex;
  flex-direction: row;
  gap: 24px;
  align-items: flex-start;
  justify-content: center;
  margin-top: 48px;
  margin-right: 72px;
  margin-left: 12px;
  width: 96vw;
}
.viewer-grid > * {
  aspect-ratio: 16 / 9;
  width: 100%;
  min-width: 320px;
  max-width: 600px;
  height: auto;
  display: flex;
  flex-direction: column;
}
</style>
