<template>
  <div class="title-card">
    <img :src="iconSrc" :alt="name" class="card-icon" />
    <h3 class="card-name">{{ name }}</h3>
    <p class="card-description">{{ description }}</p>
  </div>
</template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
  name: {
    type: String,
    required: true
  },
  description: {
    type: String,
    required: true
  },
  icon: {
    type: String,
    required: true
  }
});

// Dynamically import icon from assets - works with GitHub Pages base path
const iconSrc = computed(() => {
  return new URL(`../../assets/images/icons/${props.icon}`, import.meta.url).href;
});
</script>

<style scoped>
.title-card {
  background-color: var(--light-lila-50);
  border-radius: var(--radius-medium);
  padding: var(--space-lg);
  transition: background-color 0.3s ease;
  width: 100%;
  min-height: 200px;
  display: flex;
  flex-direction: column;
  gap: var(--space-sm);
}

.title-card:hover {
  background-color: var(--light-lila-100);
}

.card-icon {
  width: 3rem;
  height: 3rem;
  object-fit: contain;
  margin-bottom: var(--space-sm);
}

.card-name {
  color: var(--navy-blue-100);
  margin: 0;
}

.card-description {
  color: var(--navy-blue-50);
  margin: 0;
  font-size: var(--font-size-body);
  line-height: var(--line-height-relaxed);
}
</style>
