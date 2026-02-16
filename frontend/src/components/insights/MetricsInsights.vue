<template>
  <div class="metrics-insights">
    <div v-if="loading" class="loading">
      Loading metrics...
    </div>
    
    <div v-else-if="error" class="error">
      {{ error }}
    </div>
    
    <div v-else-if="!metricData" class="no-data">
      <p>No metric selected or data unavailable</p>
    </div>
    
    <div v-else class="metric-content">
      <!-- Header -->
      <div class="metric-header">
        <h2 class="metric-name">{{ metricData.name }}</h2>
        <div class="metric-summary">
          <div class="summary-item">
            <span class="label">Value:</span>
            <span class="value" :class="valueClass">{{ formatValue(metricData.total_value) }}</span>
          </div>
          <div class="summary-item">
            <span class="label">Benchmark:</span>
            <span class="benchmark">{{ formatValue(metricData.benchmark) }}</span>
          </div>
        </div>
      </div>

      <!-- Formula and Action -->
      <div class="metric-details">
        <div class="detail-box">
          <h3>Formula</h3>
          <p class="formula">{{ metricData.formula }}</p>
        </div>
        <div class="detail-box">
          <h3>Action</h3>
          <p class="action">{{ metricData.action }}</p>
        </div>
      </div>

      <!-- Per Level Data -->
      <div v-if="hasLevelData" class="data-section">
        <h3>Value per Level</h3>
        <div class="data-list">
          <div v-for="(value, level) in metricData.value_per_level" :key="level" class="data-item">
            <span class="data-key">Level {{ level }}:</span>
            <span class="data-value">{{ formatValue(value) }}</span>
          </div>
        </div>
      </div>

      <!-- Per Cluster Data -->
      <div v-if="hasClusterData" class="data-section">
        <h3>Value per Cluster</h3>
        <div class="data-list">
          <div v-for="(value, cluster) in metricData.value_per_cluster" :key="cluster" class="data-item">
            <span class="data-key">Cluster {{ cluster }}:</span>
            <span class="data-value">{{ formatValue(value) }}</span>
          </div>
        </div>
      </div>

      <!-- Chart Data -->
      <div v-if="hasChartData" class="data-section">
        <h3>{{ metricData.chart_data.label }}</h3>
        <div class="chart-data">
          <div v-for="(value, range) in metricData.chart_data.values" :key="range" class="chart-item">
            <span class="chart-label">{{ range }}</span>
            <div class="chart-bar">
              <div class="chart-fill" :style="{ width: `${value}%` }"></div>
              <span class="chart-value">{{ formatValue(value) }}%</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
  metricData: {
    type: Object,
    default: null
  },
  loading: {
    type: Boolean,
    default: false
  },
  error: {
    type: String,
    default: null
  }
});

const hasLevelData = computed(() => 
  props.metricData?.value_per_level && Object.keys(props.metricData.value_per_level).length > 0
);

const hasClusterData = computed(() => 
  props.metricData?.value_per_cluster && Object.keys(props.metricData.value_per_cluster).length > 0
);

const hasChartData = computed(() => 
  props.metricData?.chart_data && props.metricData.chart_data.values
);

const valueClass = computed(() => {
  if (!props.metricData?.total_value || !props.metricData?.benchmark) return '';
  return props.metricData.total_value >= props.metricData.benchmark ? 'success' : 'warning';
});

function formatValue(val) {
  return val !== null && val !== undefined ? Number(val).toFixed(2) : 'N/A';
}
</script>

<style scoped>
.metrics-insights {
  width: 100%;
  height: 100%;
  overflow-y: auto;
}

.loading, .error, .no-data {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  font-size: var(--font-size-lg);
  color: var(--navy-blue-50);
}

.error {
  color: var(--red-100);
}

.metric-content {
  display: flex;
  flex-direction: column;
  gap: var(--space-lg);
}

.metric-header {
  border-bottom: 2px solid var(--light-grey-100);
  padding-bottom: var(--space-md);
}

.metric-name {
  font-size: var(--font-size-2xl);
  font-weight: var(--font-weight-bold);
  color: var(--navy-blue-100);
  margin-bottom: var(--space-sm);
}

.metric-summary {
  display: flex;
  gap: var(--space-xl);
}

.summary-item {
  display: flex;
  flex-direction: column;
  gap: var(--space-xs);
}

.label {
  font-size: var(--font-size-sm);
  color: var(--navy-blue-50);
  text-transform: uppercase;
}

.value, .benchmark {
  font-size: var(--font-size-xl);
  font-weight: var(--font-weight-bold);
}

.value.success {
  color: var(--green-100);
}

.value.warning {
  color: var(--orange-100);
}

.benchmark {
  color: var(--navy-blue-100);
}

.metric-details {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-md);
}

.detail-box {
  background-color: var(--white);
  padding: var(--space-md);
  border-radius: var(--radius-md);
  border: 1px solid var(--light-grey-100);
}

.detail-box h3 {
  font-size: var(--font-size-md);
  font-weight: var(--font-weight-semibold);
  color: var(--navy-blue-100);
  margin-bottom: var(--space-sm);
}

.formula, .action {
  font-size: var(--font-size-sm);
  color: var(--navy-blue-75);
  line-height: 1.6;
}

.data-section {
  background-color: var(--white);
  padding: var(--space-md);
  border-radius: var(--radius-md);
  border: 1px solid var(--light-grey-100);
}

.data-section h3 {
  font-size: var(--font-size-lg);
  font-weight: var(--font-weight-semibold);
  color: var(--navy-blue-100);
  margin-bottom: var(--space-md);
}

.data-list {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: var(--space-sm);
  max-height: 200px;
  overflow-y: auto;
}

.data-item {
  display: flex;
  justify-content: space-between;
  padding: var(--space-xs) var(--space-sm);
  background-color: var(--light-lila-25);
  border-radius: var(--radius-sm);
}

.data-key {
  font-size: var(--font-size-sm);
  color: var(--navy-blue-75);
}

.data-value {
  font-size: var(--font-size-sm);
  font-weight: var(--font-weight-semibold);
  color: var(--navy-blue-100);
}

.chart-data {
  display: flex;
  flex-direction: column;
  gap: var(--space-sm);
}

.chart-item {
  display: flex;
  align-items: center;
  gap: var(--space-md);
}

.chart-label {
  min-width: 100px;
  font-size: var(--font-size-sm);
  color: var(--navy-blue-75);
}

.chart-bar {
  flex: 1;
  height: 24px;
  background-color: var(--light-grey-50);
  border-radius: var(--radius-sm);
  position: relative;
  overflow: hidden;
}

.chart-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--fucsia-100), var(--fucsia-75));
  transition: width 0.3s ease;
}

.chart-value {
  position: absolute;
  right: var(--space-sm);
  top: 50%;
  transform: translateY(-50%);
  font-size: var(--font-size-xs);
  font-weight: var(--font-weight-semibold);
  color: var(--navy-blue-100);
}
</style>
