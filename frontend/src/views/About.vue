<template>
  <div class="page-container">
    <div class="about-content">
      <h1 class="about-title">{{ uiText.pages.about.title }}</h1>
      
      <div class="cards-grid">
        <!-- First row: Title cards -->
        <TitleCard 
          v-for="(card, key) in uiText.cards"
          :key="`title-${key}`"
          :name="card.name"
          :description="card.description"
          :icon="card.icon"
        />
        
        <!-- Second row: Text cards -->
        <TextCard 
          v-for="(card, key) in uiText.cards"
          :key="`text-${key}`"
          :items="card.bullets" 
        />
      </div>
    </div>
  </div>
</template>

<script setup>
import { uiText } from '@/config/uiText.js';
import TitleCard from '@/components/cards/TitleCard.vue';
import TextCard from '@/components/cards/TextCard.vue';
</script>

<style scoped>
.about-content {
  width: 100%;
  max-width: 1400px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: var(--space-xl);
}

.about-title {
  text-align: center;
  margin: 0;
}

.cards-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: var(--space-lg);
  width: 100%;
}
</style>
