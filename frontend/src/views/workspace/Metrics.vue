<script setup>
import { ref, onMounted } from 'vue'
import uiText from '@/config/uiText.js'
import { fetchLatestMetrics, matchMetricsToKPIs } from '@/services/metricsApi.js'
import TitleCard from '@/components/cards/TitleCard.vue'
import MetricCard from '@/components/cards/MetricCard.vue'

const kpis = ref(matchMetricsToKPIs(uiText.kpis, {}))
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
  const numericValue = Number(val)
  if (val === null || val === undefined || Number.isNaN(numericValue)) {
    return null
  }
  return numericValue.toFixed(2)
}

function displayValue(metric) {
  return formatValue(metric?.value) ?? metric?.value_placeholder ?? 'xx.XX'
}

function displayBenchmark(metric) {
  return formatValue(metric?.benchmark) ?? metric?.benchmark_placeholder ?? 'xx.XX'
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
          :name="kpi.metrics?.[0]?.name ?? 'Metric'"
          :value="displayValue(kpi.metrics?.[0])"
          :benchmark="displayBenchmark(kpi.metrics?.[0])"
          :formula="kpi.metrics?.[0]?.formula"
        />
        <!-- Third row: Metric cards (metrics[1]) -->
        <MetricCard 
          v-for="(kpi, idx) in kpis" 
          :key="`metric1-${idx}`"
          :name="kpi.metrics?.[1]?.name ?? 'Metric'"
          :value="displayValue(kpi.metrics?.[1])"
          :benchmark="displayBenchmark(kpi.metrics?.[1])"
          :formula="kpi.metrics?.[1]?.formula"
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
