<template>
  <div class="viewer-page">
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
import { ref, computed } from 'vue';
import SpeckleViewer from '@/components/viewer/SpeckleViewer.vue';
import ViewerContent from '@/components/viewer/ViewerContent.vue';
import { viewerModels } from '@/config/modelConfig.js';

const viewerRef1 = ref(null);
const viewerRef2 = ref(null);

const modelLinks = computed(() => viewerModels.map(m => `https://app.speckle.systems/projects/${m.projectId}/models/${m.modelId}`));

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
  align-items: flex-start;
  justify-content: center;
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
