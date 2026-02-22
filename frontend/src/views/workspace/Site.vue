
<script setup>
import { uiText } from '@/config/uiText.js'
import ViewerPanel from '@/components/viewer/ViewerPanel.vue'
import { viewerModels } from '@/config/modelConfig.js'
import { ref } from 'vue';

const projectId = ref(viewerModels.site.projectId);
const modelIds = ref([viewerModels.site.siteModelId, viewerModels.site.hb01ModelId, viewerModels.site.hb02ModelId, viewerModels.site.hb03ModelId]);
</script>

<template>
	<div class="site-container">
		<div class="site-content">
            <h1 class="site-title">{{ uiText.pages.workspace.site.title }}</h1>
			<div class="viewer-wrapper">
				<ViewerPanel v-model:modelIds="modelIds" :projectId="projectId" />
			</div>
		</div>
	</div>
</template>

<style scoped>
.site-container {
	display: flex;
	justify-content: center;
	align-items: center;
	min-height: calc(100vh - 280px);
	width: 100%;
	max-width: 1280px;
	margin: 0 auto;
}
.site-content {
	width: 100%;
	text-align: center;
}
.site-title {
	margin-bottom: 2rem;
}
.viewer-wrapper {
	display: flex;
	justify-content: center;
	align-items: center;
	width: 80%;
	margin: 0 auto;
}
</style>
