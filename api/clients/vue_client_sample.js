// Sample usage of the REST API from Vue.js (JavaScript)
// Place this in a Vue component or a composable

async function fetchMetrics() {
  const response = await fetch('http://localhost:8000/metrics');
  if (!response.ok) {
    throw new Error('Failed to fetch metrics');
  }
  const data = await response.json();
  console.log('MetricA:', data.metricA);
  console.log('MetricB:', data.metricB);
  return data;
}

// Example usage in setup()
// onMounted(() => { fetchMetrics(); });
