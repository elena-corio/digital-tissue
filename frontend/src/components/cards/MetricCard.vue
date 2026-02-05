<template>
  <div class="metric-card">
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
      <span class="value">{{ value }}</span>
      <span class="benchmark">/ {{ benchmark }}</span>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

defineProps({
  name: String,
  value: String,
  benchmark: String,
  formula: String
});

const showTooltip = ref(false);
</script>

<style scoped>
.metric-card {
  background: white;
  padding: var(--space-md);
  border-radius: var(--radius-medium);
  box-shadow: var(--shadow-md);
  transition: box-shadow 0.2s ease;
}

.metric-card:hover {
  box-shadow: var(--shadow-lg);
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
  color: var(--fucsia-100);
}

.benchmark {
  font-size: var(--font-size-h3);
  font-weight: var(--font-weight-medium);
  color: var(--navy-blue-50);
}
</style>
