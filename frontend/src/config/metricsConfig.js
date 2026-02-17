export const metricDefinitions = {
  daylight_potential: {
    name: 'Daylight Potential',
    label: 'Glazed facade area',
    formula: 'window_area / net_floor_area',
    action: 'The windows area to be increased to meet the benchmark.'
  },
  green_space_index: {
    name: 'Green Space Index',
    label: 'Distance to green space',
    formula: 'max (0, 1 - distance_to_green / target*)\n*300 m',
    action: 'The distance of residential units to green space needs to be decreased to meet the benchmark.'
  },
  program_diversity_index: {
    name: 'Program Diversity Index',
    label: 'Program distribution',
    formula: '1 - (program_frequencies / program_units_count²)',
    action: 'The diversity of programs needs to be increased to meet the benchmark.'
  },
  circulation_efficiency: {
    name: 'Circulation Efficiency',
    label: 'Circulation area ratio',
    formula: '1 - (circulation_area / total_area)',
    action: 'The circulation area needs to be decreased to meet the benchmark.'
  },
  occupancy_efficiency: {
    name: 'Occupancy Efficiency',
    label: 'Usable area ratio',
    formula: 'usable_area / total_area',
    action: 'The usable area needs to be increased to meet the benchmark.'
  },
  net_floor_area_ratio: {
    name: 'Net-Floor-Area Ratio',
    label: 'Net-floor-area ratio',
    formula: 'net_floor_area / gross_floor_area',
    action: 'The net-floor-area ratio needs to be optimized to meet the benchmark.'
  },
  envelope_efficiency: {
    name: 'Envelope Efficiency',
    label: 'Envelope components',
    formula: 'building_volume / envelope_area',
    action: 'The envelope efficiency needs to be optimized to meet the benchmark.'
  },
  carbon_efficiency: {
    name: 'Carbon Efficiency',
    label: 'Carbon by material',
    formula: 'max (0, 1 - embodied_carbon_intensity / target*)\n*600 kgCO2e/kg',
    action: 'The embodied carbon needs to be decreased to meet the benchmark.'
  }
}

export const metricPlaceholders = {
  value: 'xx.XX',
  benchmark: 'xx.XX'
}

export default metricDefinitions
