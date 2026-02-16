<template>
  <div class="insight-page">
    <div class="insight-grid">
      <ViewerContent>
        <template #toolbar>
          <ButtonBar>
            <IconButton icon="ruler.svg" title="Measure" @click="$emit('measure')" />
            <IconButton icon="scissors.svg" title="Section" @click="$emit('section')" />
            <IconButton icon="filter.svg" title="Filter" @click="$emit('filter')" />
          </ButtonBar>
        </template>
        <template #prompt>
          <PromptBar
            :modelId1="inputModelId"
            @update="({ modelId1 }) => updateModelId(modelId1)"
          />
        </template>
        <SpeckleViewer 
          ref="viewerRef"
          :model-url="modelLink"
          :key="modelLink"
          :show-stats="true"
          :verbose="true"
          height="auto"
          @viewer-ready="onViewerReady"
          @model-loaded="onModelLoaded"
          @error="onError"
        />
      </ViewerContent>
      
      <div class="insights-container">
        <MetricsInsights />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';

import SpeckleViewer from '@/components/viewer/SpeckleViewer.vue';
import ViewerContent from '@/components/viewer/ViewerContent.vue';
import PromptBar from '@/components/viewer/PromptBar.vue';
import ButtonBar from '@/components/viewer/ButtonBar.vue';
import IconButton from '@/components/viewer/IconButton.vue';
import MetricsInsights from '@/components/insights/MetricsInsights.vue';

import { viewerModels } from '@/config/modelConfig.js';

const viewerRef = ref(null);

const projectId = viewerModels[0].projectId;
const inputModelId = ref(viewerModels[0].modelId);

const modelLink = computed(() => 
  `https://app.speckle.systems/projects/${projectId}/models/${inputModelId.value}`
);

function updateModelId(modelId) {
  inputModelId.value = modelId;
}

const onViewerReady = (viewer) => {
  console.log('✅ Viewer initialized:', viewer);
};

const onModelLoaded = (url) => {
  console.log('✅ Model loaded:', url);
};

const onError = (error) => {
  console.error('❌ Error:', error);
};
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
  background-color: var(--white);
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
