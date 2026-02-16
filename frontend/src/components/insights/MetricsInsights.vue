<template>
  <div class="metrics-insights">
    <h2 class="insights-title">Metrics Insights</h2>
    <p class="insights-placeholder">
      This section will display detailed metrics insights, analysis, and visualizations.
    </p>
  </div>
</template>

<script setup>
// Placeholder component for metrics insights
// Will be populated with charts, analysis, and metric details
</script>

<style scoped>
.metrics-insights {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
}

.insights-title {
  font-size: var(--font-size-2xl);
  font-weight: var(--font-weight-bold);
  color: var(--navy-blue-100);
  margin-bottom: var(--space-md);
}

.insights-placeholder {
  font-size: var(--font-size-lg);
  color: var(--navy-blue-50);
  max-width: 400px;
  line-height: 1.6;
}
</style>
