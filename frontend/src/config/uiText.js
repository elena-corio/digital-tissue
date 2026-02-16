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
        metrics: 'Metrics',
        insight: 'Insight'
      },
      viewer: {
        title: 'Model Viewer',
        subtitle: 'View and interact with your project models'
      },
      metrics: {
        title: 'Key Performance Indicators',
        subtitle: 'Track key performance indicators and analytics'
      },
      insight: {
        title: 'Metrics Insight',
        subtitle: 'Visualize and analyze metrics with your model'
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
      metrics: ['daylight_potential',
                'green_space_index']
    },
    {
      name: 'Interconnection',
      description: 'Connections between people and programs',
      icon: 'synapses.svg',
      metrics: ['program_diversity_index',
                'circulation_efficiency']
    },
    {
      name: 'Adaptability',
      description: 'Capacity of spaces and systems to transform over time',
      icon: 'adaptable.png',
      metrics: ['occupancy_efficiency',
                'net_floor_area_ratio']
    },
    {
      name: 'Sustainability',
      description: 'Environmental performance and long-term resilience',
      icon: 'sustainable.svg',
      metrics: ['envelope_efficiency',
                'carbon_efficiency']
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
