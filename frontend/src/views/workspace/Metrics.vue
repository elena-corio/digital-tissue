<template>
  <div class="metrics-container">
    <div class="grid-content">
      <h1 class="grid-title">{{ uiText.pages.workspace.metrics.title }}</h1>
      
      <div class="cards-grid">
        <!-- First row: Title cards -->
        <TitleCard 
          v-for="(kpi, key) in uiText.kpis"
          :key="`title-${key}`"
          :name="kpi.name"
          :description="kpi.description"
          :icon="kpi.icon"
        />
        <!-- Second row: Metric cards (metrics[0]) -->
        <MetricCard 
          v-for="(kpi, key) in uiText.kpis"
          :key="`metric0-${key}`"
          :name="kpi.metrics[0].name"
          :value="kpi.metrics[0].value"
          :benchmark="kpi.metrics[0].benchmark"
          :formula="kpi.metrics[0].formula"
        />
        <!-- Third row: Metric cards (metrics[1]) -->
        <MetricCard 
          v-for="(kpi, key) in uiText.kpis"
          :key="`metric1-${key}`"
          :name="kpi.metrics[1].name"
          :value="kpi.metrics[1].value"
          :benchmark="kpi.metrics[1].benchmark"
          :formula="kpi.metrics[1].formula"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import { uiText } from '@/config/uiText.js';
import TitleCard from '@/components/cards/TitleCard.vue';
import MetricCard from '@/components/cards/MetricCard.vue';
</script>

<style scoped>
.metrics-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: calc(100vh - 280px);
  width: 100%;
  max-width: 1280px;
  margin: 0 auto;
}
</style>
