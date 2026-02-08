<template>
  <div class="viewer-page">
    <div class="viewer-grid">
      <ViewerContent>
        <PromptBar
          :modelId1="inputModelId1"
          @update="({ modelId1 }) => updateModelId(0, modelId1)"
        />
        <SpeckleViewer 
          ref="viewerRef1"
          :model-url="modelLinks[0]"
          :key="modelLinks[0]"
          :show-stats="true"
          :verbose="true"
          height="auto"
          @viewer-ready="onViewerReady"
          @model-loaded="onModelLoaded"
          @error="onError"
        />
      </ViewerContent>
      <ViewerContent>
        <PromptBar
          :modelId1="inputModelId2"
          @update="({ modelId1 }) => updateModelId(1, modelId1)"
        />
        <SpeckleViewer 
          ref="viewerRef2"
          :model-url="modelLinks[1]"
          :key="modelLinks[1]"
          :show-stats="true"
          :verbose="true"
          height="auto"
          @viewer-ready="onViewerReady"
          @model-loaded="onModelLoaded"
          @error="onError"
        />
      </ViewerContent>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import SpeckleViewer from '@/components/viewer/SpeckleViewer.vue';
import ViewerContent from '@/components/viewer/ViewerContent.vue';
import PromptBar from '@/components/viewer/PromptBar.vue';

const viewerRef1 = ref(null);
const viewerRef2 = ref(null);

import { viewerModels } from '@/config/modelConfig.js';
import { computed } from 'vue';

const projectId = viewerModels[0].projectId;
const inputModelId1 = ref(viewerModels[0].modelId);
const inputModelId2 = ref(viewerModels[1].modelId);

const modelLinks = computed(() => [
  `https://app.speckle.systems/projects/${projectId}/models/${inputModelId1.value}`,
  `https://app.speckle.systems/projects/${projectId}/models/${inputModelId2.value}`
]);

function updateModelId(index, modelId) {
  if (index === 0) inputModelId1.value = modelId;
  if (index === 1) inputModelId2.value = modelId;
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
  margin-right: 56px;
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
