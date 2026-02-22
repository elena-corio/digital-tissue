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
        site: 'Site',
        project: 'Project',
        metrics: 'Metrics',
        insight: 'Insight'
      },
      site: {
        title: 'Site 3D Model Viewer',
        subtitle: 'Check how your building interacts with its neighbors.'
      },
      project: {
        title: 'Project',
        subtitle: 'Uncover the program, structure, and data behind your project.'
      },
      metrics: {
        title: 'Key Performance Indicators',
        subtitle: 'Assess the stability and health of your building’s core systems.'
      },
      insight: {
        title: 'Metrics Insight',
        subtitle: 'Understand each metric’s impact on your building’s performance.'
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
      metrics: {
        daylight_potential: true,
        green_space_index: true
      }
    },
    {
      name: 'Interconnection',
      description: 'Connections between people and programs',
      icon: 'synapses.svg',
      metrics: {
        program_diversity_index: true,
        circulation_efficiency: true
      }
    },
    {
      name: 'Adaptability',
      description: 'Capacity of spaces and systems to transform over time',
      icon: 'adaptable.png',
      metrics: {
        occupancy_efficiency: true,
        net_floor_area_ratio: true
      }
    },
    {
      name: 'Sustainability',
      description: 'Environmental performance and long-term resilience',
      icon: 'sustainable.svg',
      metrics: {
        envelope_efficiency: true,
        carbon_efficiency: true
      }
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
