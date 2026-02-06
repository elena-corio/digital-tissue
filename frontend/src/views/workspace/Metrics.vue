<template>
  <div class="metrics-container">
    <div class="metrics-content">
    <h1 class="metrics-title">{{ uiText.pages.workspace.metrics.title }}</h1>
    <div class="kpis-grid">
      <div 
        v-for="(kpi, key) in uiText.kpis" 
        :key="key"
        class="kpi-column"
      >
        <TitleCard 
          :name="kpi.name"
          :description="kpi.description"
          :icon="kpi.icon"
        />
        <MetricCard
          v-for="(metric, index) in kpi.metrics"
          :key="index"
          :name="metric.name"
          :value="metric.value"
          :benchmark="metric.benchmark"
          :formula="metric.formula"
        />
      </div>
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
  padding: var(--space-lg);
}

.metrics-content {
  width: 100%;
  max-width: 1400px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--space-xl);
}

.kpis-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: var(--space-lg);
  max-width: 1400px;
  margin: 0 auto;
}

.kpi-column {
  display: flex;
  flex-direction: column;
  gap: var(--space-md);
}
</style>
