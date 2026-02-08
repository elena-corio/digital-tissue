<template>
  <div class="viewer-page">
    <ViewerContent>
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
    </ViewerContent>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import SpeckleViewer from '@/components/viewer/SpeckleViewer.vue';
import ViewerContent from '@/components/viewer/ViewerContent.vue';

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
  padding: 0;
  margin: 0;
  width: 100vw;
  height: 100vh;
  min-height: 0;
  min-width: 0;
  box-sizing: border-box;
  overflow-x: hidden;
  overflow-y: hidden;
}
</style>
