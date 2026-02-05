<template>
  <div class="card metric-card">
    <div class="metric-header">
      <span class="metric-name">{{ name }}</span>
      <div class="info-icon" @mouseenter="showTooltip = true" @mouseleave="showTooltip = false">
        <span>ⓘ</span>
        <div v-if="showTooltip" class="tooltip">
          <strong>Formula:</strong><br>{{ formula }}
        </div>
      </div>
    </div>
    <div class="metric-value">
      <span class="value" :class="isAboveBenchmark ? 'value-above' : 'value-below'">{{ value }}</span>
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
  return numValue >= numBenchmark;
});
</script>

<style scoped>
.metric-card {
  padding: var(--space-md);
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
  right: 0;
  cursor: help;
  color: var(--navy-blue-50);
  font-size: var(--font-size-body);
  user-select: none;
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
  color: var(--fucsia-100); /* Default: below benchmark */
}

.value.value-above {
  color: var(--light-blue-100);
}

.value.value-below {
  color: var(--fucsia-100);
}

.benchmark {
  font-size: var(--font-size-h3);
  font-weight: var(--font-weight-medium);
  color: var(--navy-blue-50);
}
</style>
