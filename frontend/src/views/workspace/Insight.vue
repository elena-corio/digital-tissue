<template>
  <div class="insight-page">
    <div class="insight-grid">
      <ViewerPanel 
        v-model:modelId="inputModelId"
        :projectId="projectId"
      />
      
      <div class="insights-container">
        <!-- Metric Selector -->
        <div class="metric-selector">
          <label for="metric-select">Select Metric:</label>
          <select id="metric-select" v-model="selectedMetricKey" class="metric-dropdown">
            <option value="">-- Choose a metric --</option>
            <option v-for="(metric, key) in availableMetrics" :key="key" :value="key">
              {{ metric.name }}
            </option>
          </select>
        </div>

        <!-- Metrics Insights Component -->
        <MetricsInsights 
          :metricData="selectedMetricData"
          :loading="loading"
          :error="error"
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';

import ViewerPanel from '@/components/viewer/ViewerPanel.vue';
import MetricsInsights from '@/components/insights/MetricsInsights.vue';
import { fetchLatestMetrics } from '@/services/metricsApi.js';
import { metricDefinitions, metricPlaceholders } from '@/config/metricsConfig.js';

import { viewerModels } from '@/config/modelConfig.js';

const projectId = viewerModels.data.projectId;
const inputModelId = ref(viewerModels.data.modelId);

function buildDefaultMetrics() {
  return Object.fromEntries(
    Object.entries(metricDefinitions).map(([slug, metric]) => [
      slug,
      {
        slug,
        name: metric.name || slug,
        label: metric.label || null,
        formula: metric.formula || null,
        action: metric.action || null,
        total_value: null,
        benchmark: null,
        value_placeholder: metricPlaceholders.value,
        benchmark_placeholder: metricPlaceholders.benchmark,
        value_per_level: {},
        value_per_cluster: {},
        chart_data: null
      }
    ])
  );
}

function mergeMetrics(defaultMetrics, backendMetrics) {
  const merged = { ...defaultMetrics };

  for (const [slug, backendMetric] of Object.entries(backendMetrics || {})) {
    merged[slug] = {
      ...(merged[slug] || {
        slug,
        name: slug,
        value_placeholder: metricPlaceholders.value,
        benchmark_placeholder: metricPlaceholders.benchmark,
        value_per_level: {},
        value_per_cluster: {},
        chart_data: null
      }),
      ...backendMetric,
      slug,
      name: backendMetric?.name || merged[slug]?.name || slug,
      total_value: backendMetric?.total_value ?? merged[slug]?.total_value ?? null,
      benchmark: backendMetric?.benchmark ?? merged[slug]?.benchmark ?? null,
      value_placeholder: merged[slug]?.value_placeholder || metricPlaceholders.value,
      benchmark_placeholder: merged[slug]?.benchmark_placeholder || metricPlaceholders.benchmark,
      value_per_level: backendMetric?.value_per_level || merged[slug]?.value_per_level || {},
      value_per_cluster: backendMetric?.value_per_cluster || merged[slug]?.value_per_cluster || {},
      chart_data: backendMetric?.chart_data || merged[slug]?.chart_data || null
    };
  }

  return merged;
}

// Metrics data
const metricsData = ref(buildDefaultMetrics());
const selectedMetricKey = ref('');
const loading = ref(true);
const error = ref(null);

// Get list of available metrics with names
const availableMetrics = computed(() => {
  const metrics = {};
  for (const [key, data] of Object.entries(metricsData.value)) {
    if (data?.name) {
      metrics[key] = { name: data.name };
    }
  }
  return metrics;
});

// Get the selected metric's full data
const selectedMetricData = computed(() => {
  if (!selectedMetricKey.value || !metricsData.value[selectedMetricKey.value]) {
    return null;
  }
  return metricsData.value[selectedMetricKey.value];
});

// Fetch metrics on mount
async function loadMetrics() {
  loading.value = true;
  error.value = null;
  const defaultMetrics = buildDefaultMetrics();
  try {
    const data = await fetchLatestMetrics();
    metricsData.value = mergeMetrics(defaultMetrics, data);
    
    // Auto-select first metric if available
    const keys = Object.keys(metricsData.value);
    if (keys.length > 0) {
      selectedMetricKey.value = keys.includes(selectedMetricKey.value) ? selectedMetricKey.value : keys[0];
    }
  } catch (e) {
    metricsData.value = defaultMetrics;
    error.value = e.message;
    console.error('Failed to load metrics:', e);
    const keys = Object.keys(defaultMetrics);
    if (keys.length > 0 && !selectedMetricKey.value) {
      selectedMetricKey.value = keys[0];
    }
  } finally {
    loading.value = false;
  }
}

onMounted(loadMetrics);
</script>

<style scoped>
.insight-page {
  width: 100%;
  height: 100%;
}

.insight-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-md);
  height: calc(100vh - 200px);
}

.insights-container {
  background-color: white;
  border-radius: var(--radius-md);
  padding: var(--space-lg);
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  gap: var(--space-md);
  box-shadow: var(--shadow-lg);
}

.metric-selector {
  display: flex;
  flex-direction: column;
  gap: var(--space-xs);
background-color: white;
  border-radius: var(--radius-medium);
}

.metric-selector label {
  font-size: var(--font-size-sm);
  color: var(--navy-blue-100);
}

.metric-dropdown {
  padding: var(--space-sm) var(--space-md);
  font-size: var(--font-size-md);
  border: 2px solid var(--light-grey-100);
  border-radius: var(--radius-sm);
  background-color: white;
  color: var(--navy-blue-100);
  cursor: pointer;
  transition: border-color 0.2s ease;
}

.metric-dropdown:hover {
  border-color: var(--fucsia-100);
}

.metric-dropdown:focus {
  outline: none;
  border-color: var(--fucsia-100);
  box-shadow: 0 0 0 3px var(--fucsia-25);
}

@media (max-width: 768px) {
  .insight-grid {
    grid-template-columns: 1fr;
    height: auto;
  }
}
</style>
