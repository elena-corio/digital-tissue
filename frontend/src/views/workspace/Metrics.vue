<script setup>
import { ref, onMounted } from 'vue'
import uiText from '@/config/uiText.js'
import { fetchLatestMetrics, matchMetricsToKPIs } from '@/services/metricsApi.js'
import TitleCard from '@/components/cards/TitleCard.vue'
import MetricCard from '@/components/cards/MetricCard.vue'

const kpis = ref(JSON.parse(JSON.stringify(uiText.kpis)))
const loading = ref(true)
const error = ref(null)

async function loadMetrics() {
  loading.value = true
  error.value = null
  try {
    // Fetch latest metrics from backend
    const backendMetrics = await fetchLatestMetrics()
    
    // Match backend metrics to KPIs from uiText
    kpis.value = matchMetricsToKPIs(kpis.value, backendMetrics)
  } catch (e) {
    error.value = e.message
    console.error('Failed to load metrics:', e)
  } finally {
    loading.value = false
  }
}

function formatValue(val) {
  return val !== undefined ? Number(val).toFixed(2) : 'N/A'
}

onMounted(loadMetrics)
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
          :value="formatValue(kpi.metrics[0].value)"
          :benchmark="formatValue(kpi.metrics[0].benchmark)"
          :formula="kpi.metrics[0].formula"
        />
        <!-- Third row: Metric cards (metrics[1]) -->
        <MetricCard 
          v-for="(kpi, idx) in kpis" 
          :key="`metric1-${idx}`"
          :name="kpi.metrics[1].name"
          :value="formatValue(kpi.metrics[1].value)"
          :benchmark="formatValue(kpi.metrics[1].benchmark)"
          :formula="kpi.metrics[1].formula"
        />
      </div>
    </div>
  </div>
</template>

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
