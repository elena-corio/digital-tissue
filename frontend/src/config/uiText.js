export const uiText = {
  app: {
    title: 'digital.tissue',
  },
  navigation: {
    home: 'Home',
    workspace: 'Workspace',
    about: 'About',
    login: 'Login'
  },
  pages: {
    homepage: {
      title: 'A living data system for design intelligence',
      subtitle: 'Explore your models | Track key metrics | Collaborate seamlessly',
      getStarted: 'Get Started',
      learnMore: 'Learn More'
    },
    workspace: {
      title: 'Workspace',
      subtitle: 'Active workspace environment',
      tabs: {
        viewer: 'Viewer',
        metrics: 'Metrics'
      },
      viewer: {
        title: 'Model Viewer',
        subtitle: 'View and interact with your project models'
      },
      metrics: {
        title: 'Performance Metrics',
        subtitle: 'Track key performance indicators and analytics'
      }
    },
    about: {
      title: 'Living data system',
    },
    login: {
      title: 'Login'
    }
  },
  cards: {
    card1: {
      name: 'Framework',
      description: 'Genetic code - How the system grows and evolves',
      icon: 'dna.svg',
      bullets: [
        'Design rulebook',
        'Data structure',
        'Standard protocols'
      ]
    },
    card2: {
      name: 'Automation',
      description: 'Synapses - How models and tools exchange meaning',
      icon: 'synapses.svg',
      bullets: [
        'Automated workflows',
        'Tools integration',
        'Version control'
      ]
    },
    card3: {
      name: 'Monitoring',
      description: 'Metabolism - How the system stays healthy and responsive',
      icon: 'metabolism.png',
      bullets: [
        'KPIs & metrics',
        'Data validation',
        'Feedback loops'
      ]
    },
    card4: {
      name: 'Coordination',
      description: 'Network - How different parts of the system work together',
      icon: 'network.svg',
      bullets: [
        'Decision tracking',
        'Project timeline',
        'Collaboration tools'
      ]
    }
  },
   kpis: {
    kpi1: {
      name: 'Liveability',
      description: 'Capacity to support everyday wellbeing',
      icon: 'livable.svg',
      metrics: [
      {name: 'Service Density Index', formula: 'service_area / users_count', benchmark: '0.05', value: '0.04'},
      {name: 'Urban Green Space Indicator', formula: 'residents_close_to_green_count / residents_count', benchmark: '1.0', value: '0.8'},
      ]
    },
    kpi2: {
      name: 'Interconnection',
      description: 'Connections between people and programs',
      icon: 'synapses.svg',
      metrics: [
      {name: 'Program Diversity Index', formula: '1 - program_frequencies / (program_units_count)²', benchmark: '0.7', value: '0.75'},
      {name: 'Circulation-to-Program Ratio', formula: 'circulation_area / program_area', benchmark: '0.3', value: '0.35'},
      ]
    },
    kpi3: {
      name: 'Monitoring',
      description: 'Capacity of spaces and systems to transform over time',
      icon: 'adaptable.png',
      metrics: [
        {name: 'Mixed-Use Area Ratio', formula: 'hybrid_program_area / program_area', benchmark: '0.4', value: '0.3'},
        {name: 'Column-free Area Ratio', formula: 'net_floor_area / gross_floor_area', benchmark: '0.7', value: '0.8'},
      ]
    },
    kpi4: {
      name: 'Sustainability',
      description: 'Environmental performance and long-term resilience',
      icon: 'sustainable.svg',
      metrics: [
        {name: 'Daylight and Ventilation Potential', formula: 'window_area / net_floor_area', benchmark: '0.2', value: '0.3'},
        {name: 'Data Embodied Carbon Intensity', formula: 'embodied_carbon / gross_floor_area', benchmark: '500', value: '650'},
      ]
    }
  },
  common: {
    loading: 'Loading...',
    error: 'An error occurred',
    save: 'Save',
    cancel: 'Cancel',
    delete: 'Delete',
    edit: 'Edit',
    close: 'Close',
    confirm: 'Confirm'
  }
};

export default uiText;
