<template>
  <div class="insight-page">
    <div class="insight-grid">
      <ViewerPanel 
        v-model:modelId="inputModelId"
        :projectId="projectId"
      />
      
      <div class="insights-container">
        <MetricsInsights />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

import ViewerPanel from '@/components/viewer/ViewerPanel.vue';
import MetricsInsights from '@/components/insights/MetricsInsights.vue';

import { viewerModels } from '@/config/modelConfig.js';

const projectId = viewerModels[0].projectId;
const inputModelId = ref(viewerModels[0].modelId);
</script>

<style scoped>
.insight-page {
  width: 100%;
  height: 100%;
}

.insight-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-md);
  height: calc(100vh - 200px);
}

.insights-container {
  background-color: var(--light-lila-50);
  border-radius: var(--radius-md);
  padding: var(--space-lg);
  overflow-y: auto;
}

@media (max-width: 768px) {
  .insight-grid {
    grid-template-columns: 1fr;
    height: auto;
  }
}
</style>
