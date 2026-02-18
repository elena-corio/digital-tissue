
<template>
  <ClerkProvider>
    <div id="app">
      <Header />
      <main>
        <router-view />
      </main>
    </div>
  </ClerkProvider>
</template>

<script setup>
import Header from '@/components/layout/Header.vue';
import { ClerkProvider } from '@clerk/vue';
</script>

<style>

</style>
