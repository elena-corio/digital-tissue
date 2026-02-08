<template>
  <div class="viewer-page">
    
    <SpeckleViewer 
      ref="viewerRef"
      model-url="https://app.speckle.systems/projects/dcca94731b/models/827526cd48"
      :show-stats="true"
      :verbose="true"
      height="700px"
      @viewer-ready="onViewerReady"
      @model-loaded="onModelLoaded"
      @error="onError"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue';
import SpeckleViewer from '@/components/viewer/SpeckleViewer.vue';

const viewerRef = ref(null);

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
  padding: var(--space-lg, 24px);
  height: 100vh;
}

h1 {
  margin-bottom: var(--space-md, 16px);
}
</style>
