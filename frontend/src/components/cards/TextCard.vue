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
  background-color: var(--light-grey-50);
  border-radius: var(--radius-medium);
  padding: var(--space-lg);
  transition: background-color 0.3s ease;
  width: 100%;
  min-height: 200px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.text-card:hover {
  background-color: var(--light-grey-100);
}

.card-list {
  list-style-type: disc;
  padding-left: var(--space-lg);
  margin: 0;
  color: var(--navy-blue-100);
  text-align: left;
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
