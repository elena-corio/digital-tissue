<template>
  <div class="card metric-card">
    <div class="info-icon" @mouseenter="showTooltip = true" @mouseleave="showTooltip = false">
      <span>ⓘ</span>
      <div v-if="showTooltip" class="tooltip">
        <strong>Formula:</strong><br>{{ formula }}
      </div>
    </div>
    <div class="metric-header">
      <span class="metric-name">{{ name }}</span>
    </div>
    <div class="metric-value">
      <span class="value" :class="valueClass">{{ value }}</span>
      <span class="benchmark">/ {{ benchmark }}</span>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';

const props = defineProps({
  name: String,
  value: String,
  benchmark: String,
  formula: String
});

const showTooltip = ref(false);

const isAboveBenchmark = computed(() => {
  const numValue = parseFloat(props.value);
  const numBenchmark = parseFloat(props.benchmark);
  if (Number.isNaN(numValue) || Number.isNaN(numBenchmark)) {
    return null;
  }
  return numValue >= numBenchmark;
});

const valueClass = computed(() => {
  if (isAboveBenchmark.value === null) {
    return '';
  }
  return isAboveBenchmark.value ? 'value-above' : 'value-below';
});
</script>

<style scoped>
.metric-card {
  padding: var(--space-lg);
  width: 100%;
  position: relative;
}

.metric-header {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: var(--space-sm);
  position: relative;
}

.metric-name {
  font-size: var(--font-size-body);
  font-weight: var(--font-weight-semibold);
  color: var(--navy-blue-100);
}

.info-icon {
  position: absolute;
  top: 5px;
  right: 5px;
  cursor: help;
  color: var(--navy-blue-50);
  font-size: var(--font-size-body);
  user-select: none;
  padding: var(--space-xs);
  z-index: 20;
  background: white;
  border-radius: 50%;
}

.info-icon:hover {
  color: var(--fucsia-100);
}

.tooltip {
  position: absolute;
  top: 100%;
  right: 0;
  margin-top: var(--space-sm);
  padding: var(--space-sm) var(--space-md);
  background: var(--navy-blue-100);
  color: white;
  border-radius: var(--radius-small);
  box-shadow: var(--shadow-lg);
  white-space: nowrap;
  font-size: var(--font-size-small);
  z-index: 10;
  pointer-events: none;
}

.metric-value {
  display: flex;
  align-items: baseline;
  justify-content: center;
  gap: var(--space-sm);
}

.value {
  font-size: var(--font-size-h2);
  font-weight: var(--font-weight-bold);
  color: var(--color-error); /* Default: below benchmark */
}

.value.value-above {
  color: var(--color-success);
}

.value.value-below {
  color: var(--color-error);
}

.benchmark {
  font-size: var(--font-size-h3);
  font-weight: var(--font-weight-medium);
}
</style>
