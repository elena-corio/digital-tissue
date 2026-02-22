<script setup>
import { uiText } from '@/config/uiText.js'
</script>

<template>
	<div class="site-container">
		<div class="site-content">
			<h2 class="site-subtitle">{{ uiText.pages.workspace.site.subtitle }}</h2>
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
.site-subtitle {
	font-size: 2rem;
	font-weight: 500;
	color: var(--navy-blue-100);
}
</style>
