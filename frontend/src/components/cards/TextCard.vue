<template>
  <div class="text-card">
    <ul class="card-list">
      <li v-for="(item, index) in items" :key="index" class="card-list-item">
        {{ item }}
      </li>
    </ul>
  </div>
</template>

<script setup>
defineProps({
  items: {
    type: Array,
    required: true
  }
});
</script>

<style scoped>
.text-card {
  background-color: white;
  border-radius: var(--radius-medium);
  padding: var(--space-lg);
  transition: box-shadow 0.3s ease;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: var(--shadow-md);
}

.text-card:hover {
  box-shadow: var(--shadow-lg);
}

.card-list {
  list-style-type: none;
  padding-left: 0;
  margin: 0;
  color: var(--navy-blue-100);
  text-align: center;
}

.card-list-item {
  font-size: var(--font-size-body);
  line-height: var(--line-height-relaxed);
  margin-bottom: var(--space-sm);
}

.card-list-item:last-child {
  margin-bottom: 0;
}
</style>
