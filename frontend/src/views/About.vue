<template>
  <div class="page-container">
    <div class="about-content">
      <h1 class="about-title">{{ uiText.pages.about.title }}</h1>
      
      <div class="cards-grid">
        <!-- First row: Title cards -->
        <TitleCard 
          :name="uiText.cards.card1.name"
          :description="uiText.cards.card1.description"
          :icon="uiText.cards.card1.icon"
        />
        <TitleCard 
          :name="uiText.cards.card2.name"
          :description="uiText.cards.card2.description"
          :icon="uiText.cards.card2.icon"
        />
        <TitleCard 
          :name="uiText.cards.card3.name"
          :description="uiText.cards.card3.description"
          :icon="uiText.cards.card3.icon"
        />
        <TitleCard 
          :name="uiText.cards.card4.name"
          :description="uiText.cards.card4.description"
          :icon="uiText.cards.card4.icon"
        />
        
        <!-- Second row: Text cards -->
        <TextCard :items="uiText.cards.card1.bullets" />
        <TextCard :items="uiText.cards.card2.bullets" />
        <TextCard :items="uiText.cards.card3.bullets" />
        <TextCard :items="uiText.cards.card4.bullets" />
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
.page-container {
  padding: var(--space-lg);
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: calc(100vh - 80px);
}

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
