<template>
  <div class="page-container">
    <div class="grid-content">
      <h1 class="grid-title">{{ uiText.pages.about.title }}</h1>
      
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


