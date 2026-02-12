<script setup>
import { ref, onMounted } from 'vue'
import uiText from '@/config/uiText.js'
import TitleCard from '@/components/cards/TitleCard.vue';
import MetricCard from '@/components/cards/MetricCard.vue';

const kpis = ref(JSON.parse(JSON.stringify(uiText.kpis)))
const loading = ref(true)
const error = ref(null)

async function fetchMetricValues() {
  loading.value = true
  error.value = null
  try {
    const response = await fetch('http://localhost:8000/metrics')
    if (!response.ok) throw new Error('Failed to fetch metrics')
    const values = await response.json()
    // Merge values into metrics by name
    Object.values(kpis.value).forEach(kpi => {
      kpi.metrics.forEach(metric => {
        if (values.hasOwnProperty(metric.name)) {
          metric.value = values[metric.name]
        }
      })
    })
  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
  }
}

onMounted(fetchMetricValues)
</script>

<template>
  <div class="metrics-container">
    <div class="grid-content">
      <h1 class="grid-title">{{ uiText.pages.workspace.metrics.title }}</h1>
      <div class="cards-grid">
        <!-- First row: Title cards -->
        <TitleCard 
          v-for="(kpi, idx) in kpis" 
          :key="`title-${idx}`"
          :name="kpi.name"
          :description="kpi.description"
          :icon="kpi.icon"
        />
        <!-- Second row: Metric cards (metrics[0]) -->
        <MetricCard 
          v-for="(kpi, idx) in kpis" 
          :key="`metric0-${idx}`"
          :name="kpi.metrics[0].name"
          :value="kpi.metrics[0].value"
          :benchmark="kpi.metrics[0].benchmark"
          :formula="kpi.metrics[0].formula"
        />
        <!-- Third row: Metric cards (metrics[1]) -->
        <MetricCard 
          v-for="(kpi, idx) in kpis" 
          :key="`metric1-${idx}`"
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
}
</style>
