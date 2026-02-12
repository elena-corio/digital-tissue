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
      {name: 'Service Density Index', formula: 'service_area / users_count', benchmark: '0.05'},
      {name: 'Urban Green Space Index', formula: 'residents_close_to_green_count / residents_count', benchmark: '1.00'},
      ]
    },
    {
      name: 'Interconnection',
      description: 'Connections between people and programs',
      icon: 'synapses.svg',
      metrics: [
      {name: 'Program Diversity Index', formula: '1 - (program_frequencies / program_units_count ²)', benchmark: '0.70'},
      {name: 'Circulation Efficiency Index', formula: '1 - (circulation_area / program_area)', benchmark: '0.70'},
      ]
    },
    {
      name: 'Adaptability',
      description: 'Capacity of spaces and systems to transform over time',
      icon: 'adaptable.png',
      metrics: [
        {name: 'Mixed-Use Area Ratio', formula: 'hybrid_program_area / program_area', benchmark: '0.40'},
        {name: 'Column-free Area Ratio', formula: 'net_floor_area / gross_floor_area', benchmark: '0.70'},
      ]
    },
    {
      name: 'Sustainability',
      description: 'Environmental performance and long-term resilience',
      icon: 'sustainable.svg',
      metrics: [
        {name: 'Daylight Potential', formula: 'window_area / net_floor_area', benchmark: '0.20'},
        {name: 'Carbon Efficiency Index', formula: '500 / (embodied_carbon / gross_floor_area)', benchmark: '1.00'},
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
