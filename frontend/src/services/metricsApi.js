import { useAuth } from '@clerk/vue'
import { metricDefinitions, metricPlaceholders } from '@/config/metricsConfig.js'

const isAuthBypassEnabled = import.meta.env.DEV && import.meta.env.VITE_SKIP_AUTH === 'true'
const API_URL = import.meta.env.VITE_API_URL

async function buildAuthHeaders() {
  // Skip auth headers only in development when explicitly enabled
  if (isAuthBypassEnabled) {
    return {}
  }

  const auth = useAuth()
  console.log('DEBUG useAuth() result:', auth)
  const { getToken } = auth
  if (typeof getToken !== 'function') {
    console.error('getToken is not a function! useAuth() result:', auth)
    return {}
  }
  const token = await getToken()

  if (!token) {
    return {}
  }

  return {
    Authorization: `Bearer ${token}`
  }
}

/**
 * Fetch the latest metrics from backend
 * @returns {Promise<Object>} Raw metrics object keyed by slug
 */
export async function fetchLatestMetrics() {
  try {
    const headers = await buildAuthHeaders()
    const response = await fetch(`${API_URL}/api/metrics`, { headers })
    
    if (!response.ok) {
      let detail = ''
      try {
        const errorBody = await response.json()
        detail = errorBody?.detail || ''
      } catch {
        detail = ''
      }

      if (response.status === 404) {
        throw new Error('Metrics not available. Please calculate metrics first.')
      }
      throw new Error(
        detail
          ? `Failed to fetch metrics from backend (${response.status}): ${detail}`
          : `Failed to fetch metrics from backend (${response.status})`
      )
    }
    
    const metricsData = await response.json()
    return enrichMetricsWithFrontendConfig(metricsData)
  } catch (error) {
    console.error('Error fetching metrics:', error)
    throw error
  }
}

/**
 * Fetch metrics for a specific version (for history)
 * @param {string} versionId - The Speckle version ID
 * @returns {Promise<Object>} Raw metrics object keyed by slug
 */
export async function fetchMetricsByVersion(versionId) {
  try {
    const headers = await buildAuthHeaders()
    const response = await fetch(`${API_URL}/api/metrics/${versionId}`, { headers })
    
    if (!response.ok) {
      let detail = ''
      try {
        const errorBody = await response.json()
        detail = errorBody?.detail || ''
      } catch {
        detail = ''
      }

      if (response.status === 404) {
        throw new Error(`Metrics not found for version ${versionId}`)
      }
      throw new Error(
        detail
          ? `Failed to fetch metrics from backend (${response.status}): ${detail}`
          : `Failed to fetch metrics from backend (${response.status})`
      )
    }
    
    const metricsData = await response.json()
    return enrichMetricsWithFrontendConfig(metricsData)
  } catch (error) {
    console.error('Error fetching metrics:', error)
    throw error
  }
}

function enrichMetricsWithFrontendConfig(metricsData) {
  const enriched = {}

  for (const [metricSlug, backendMetric] of Object.entries(metricsData || {})) {
    const frontendMetric = metricDefinitions[metricSlug] || {}

    enriched[metricSlug] = {
      ...backendMetric,
      name: frontendMetric.name || backendMetric?.name || metricSlug,
      label: frontendMetric.label || backendMetric?.label || null,
      formula: frontendMetric.formula || backendMetric?.formula || null,
      action: frontendMetric.action || backendMetric?.action || null,
      benchmark: backendMetric?.benchmark ?? null,
      value_placeholder: metricPlaceholders.value,
      benchmark_placeholder: metricPlaceholders.benchmark
    }
  }

  return enriched
}

/**
 * List all saved metric versions (history)
 * @returns {Promise<Object>} List of available versions
 */
export async function listMetricVersions() {
  try {
    const headers = await buildAuthHeaders()
    const response = await fetch(`${API_URL}/api/metrics/history`, { headers })
    
    if (!response.ok) {
      throw new Error('Failed to fetch metric versions from backend')
    }
    
    return await response.json()
  } catch (error) {
    console.error('Error listing metric versions:', error)
    throw error
  }
}

/**
 * Parse metrics from backend response
 * Handles None/null values by replacing with 0 and logging warning
 * @param {Object} metricsData - Raw metrics data from backend
 * @returns {Object} Parsed metrics with values
 */
function parseMetrics(metricsData) {
  const parsed = {}
  
  for (const [metricKey, metricData] of Object.entries(metricsData)) {
    // Handle MetricResult object
    if (metricData && typeof metricData === 'object') {
      const value = metricData.total_value
      
      if (value === null || value === undefined) {
        console.warn(`⚠️ Metric "${metricData.name}" has no value. Using 0 as fallback.`)
        parsed[metricData.name] = {
          value: 0,
          benchmark: metricData.benchmark || 0,
          action: metricData.action,
          chart_data: metricData.chart_data,
          value_per_level: metricData.value_per_level,
          value_per_cluster: metricData.value_per_cluster,
        }
      } else {
        parsed[metricData.name] = {
          value: value,
          benchmark: metricData.benchmark || 0,
          action: metricData.action,
          chart_data: metricData.chart_data,
          value_per_level: metricData.value_per_level,
          value_per_cluster: metricData.value_per_cluster,
        }
      }
    }
  }
  
  return parsed
}

/**
 * Match metrics from backend with KPIs from uiText
 * Converts metric slugs to full metric objects with backend data
 * @param {Array} kpis - KPI list from uiText (with metric slugs)
 * @param {Object} backendMetrics - Metrics from backend (keyed by slug)
 * @returns {Array} KPIs with metrics as objects containing backend data
 */
export function matchMetricsToKPIs(kpis, backendMetrics) {
  const updatedKPIs = JSON.parse(JSON.stringify(kpis)) // Deep copy
  
  updatedKPIs.forEach(kpi => {
    const metricSlugs = Array.isArray(kpi.metrics)
      ? kpi.metrics
          .map(metric => {
            if (typeof metric === 'string') {
              return metric
            }
            if (metric && typeof metric === 'object') {
              return metric.slug || metric.key || metric.name || null
            }
            return null
          })
          .filter(Boolean)
      : Object.keys(kpi.metrics || {})

    // Convert metric slugs to metric objects
    kpi.metrics = metricSlugs.map(metricSlug => {
      const backendMetric = backendMetrics[metricSlug]
      const frontendMetric = metricDefinitions[metricSlug] || {}
      
      if (backendMetric) {
        return {
          name: frontendMetric.name || backendMetric.name || metricSlug,
          slug: metricSlug,
          value: backendMetric.total_value,
          benchmark: backendMetric.benchmark ?? null,
          label: frontendMetric.label || backendMetric.label,
          formula: frontendMetric.formula || backendMetric.formula,
          action: frontendMetric.action || backendMetric.action,
          value_placeholder: metricPlaceholders.value,
          benchmark_placeholder: metricPlaceholders.benchmark,
          chart_data: backendMetric.chart_data,
          value_per_level: backendMetric.value_per_level,
          value_per_cluster: backendMetric.value_per_cluster,
        }
      } else {
        console.warn(`⚠️ Metric "${metricSlug}" not found in backend response`)
        return {
          name: frontendMetric.name || metricSlug,
          slug: metricSlug,
          value: null,
          benchmark: null,
          label: frontendMetric.label || null,
          formula: frontendMetric.formula || null,
          action: frontendMetric.action || null,
          value_placeholder: metricPlaceholders.value,
          benchmark_placeholder: metricPlaceholders.benchmark,
        }
      }
    })
  })
  
  return updatedKPIs
}
