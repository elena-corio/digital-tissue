<template>
  <div class="viewer-page">
    <PromptBar
      :projectId="inputProjectId"
      :modelId1="inputModelId1"
      :modelId2="inputModelId2"
      @update="onPromptUpdate"
    />
    <div class="viewer-grid">
      <ViewerContent>
        <SpeckleViewer 
          ref="viewerRef1"
          :model-url="modelLinks[0]"
          :show-stats="true"
          :verbose="true"
          height="auto"
          @viewer-ready="onViewerReady"
          @model-loaded="onModelLoaded"
          @error="onError"
        />
      </ViewerContent>
      <ViewerContent>
        <SpeckleViewer 
          ref="viewerRef2"
          :model-url="modelLinks[1]"
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
import { viewerModels } from '@/config/modelConfig.js';

const viewerRef1 = ref(null);
const viewerRef2 = ref(null);

const inputProjectId = ref(viewerModels[0].projectId);
const inputModelId1 = ref(viewerModels[0].modelId);
const inputModelId2 = ref(viewerModels[1].modelId);

const modelLinks = ref([
  `https://app.speckle.systems/projects/${inputProjectId.value}/models/${inputModelId1.value}`,
  `https://app.speckle.systems/projects/${inputProjectId.value}/models/${inputModelId2.value}`
]);

function onPromptUpdate({ projectId, modelId1, modelId2 }) {
  inputProjectId.value = projectId;
  inputModelId1.value = modelId1;
  inputModelId2.value = modelId2;
  modelLinks.value = [
    `https://app.speckle.systems/projects/${projectId}/models/${modelId1}`,
    `https://app.speckle.systems/projects/${projectId}/models/${modelId2}`
  ];
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
.prompt-bar {
  width: 100vw;
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
}
</style>
