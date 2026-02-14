export const uiText = {
  app: {
    title: 'digital.tissue',
  },
  navigation: {
    home: 'Home',
    workspace: 'Workspace',
    about: 'About',
    login: "Login",
    logout: "Logout",
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
        title: 'Key Performance Indicators',
        subtitle: 'Track key performance indicators and analytics'
      }
    },
    about: {
      title: 'Living data system',
    },
    login: {
      title: 'Login',
      authTab: 'Authentication',
      usernameLabel: 'Username:',
      usernamePlaceholder: 'Your name (optional)',
      tokenLabel: 'Speckle Token:',
      tokenPlaceholder: 'Paste your Speckle token',
      loginBtn: 'Login'
    }
  },
  cards: [
    {
      name: 'Framework',
      description: 'Genetic code - How the system grows and evolves',
      icon: 'dna.svg',
      bullets: [
        'Design rulebook',
        'Data structure',
        'Standard protocols'
      ]
    },
    {
      name: 'Automation',
      description: 'Synapses - How models and tools exchange meaning',
      icon: 'synapses.svg',
      bullets: [
        'Automated workflows',
        'Tools integration',
        'Version control'
      ]
    },
    {
      name: 'Monitoring',
      description: 'Metabolism - How the system stays healthy and responsive',
      icon: 'metabolism.png',
      bullets: [
        'KPIs & metrics',
        'Data validation',
        'Feedback loops'
      ]
    },
    {
      name: 'Coordination',
      description: 'Network - How different parts of the system work together',
      icon: 'network.svg',
      bullets: [
        'Decision tracking',
        'Project timeline',
        'Collaboration tools'
      ]
    }
  ],
   kpis: [
    {
      name: 'Liveability',
      description: 'Capacity to support everyday wellbeing',
      icon: 'livable.svg',
      metrics: [
      {name: 'Daylight Potential', formula: 'window_area / net_floor_area'},
      {name: 'Urban Green Space Index', formula: 'residents_close_to_green_count / residents_count'},
      ]
    },
    {
      name: 'Interconnection',
      description: 'Connections between people and programs',
      icon: 'synapses.svg',
      metrics: [
      {name: 'Program Diversity Index', formula: '1 - (program_frequencies / program_units_count ²)'},
      {name: 'Circulation Efficiency', formula: '1 - (circulation_area / total_area)'},
      ]
    },
    {
      name: 'Adaptability',
      description: 'Capacity of spaces and systems to transform over time',
      icon: 'adaptable.png',
      metrics: [
        {name: 'Occupancy Efficiency', formula: 'usable_area / total_area'},
        {name: 'Net-Floor-Area Ratio', formula: 'net_floor_area / gross_floor_area'},
      ]
    },
    {
      name: 'Sustainability',
      description: 'Environmental performance and long-term resilience',
      icon: 'sustainable.svg',
      metrics: [
        {name: 'Surface-to-Volume Ratio', formula: 'envelope_area / building_volume'},
        {name: 'Carbon Efficiency', formula: '500 / (embodied_carbon / gross_floor_area)'},
      ]
    }
  ],
  promptBar: {
    modelIdLabel: 'Model ID:',
    modelIdPlaceholder: 'Model ID',
    updateBtn: 'Update'
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
