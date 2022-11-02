<template>
  <!-- Choose app section -->
  <div class="px-4 py-4">
    <div class="text-lg text-black dark:text-white text-center">
      Choose your app
    </div>
    <div class="flex space-x-4 text-center">
      <router-link class="container" to="apps/clustering">
        <n-card class="bg-white dark:bg-gray-100" title="Clustering" hoverable>
          Card Content
        </n-card>
      </router-link>
      <n-badge class="container" value="WIP" type="info" processing>
        <n-card class="bg-white dark:bg-gray-100" title="Sentiment Analysis">
          Card Content
        </n-card>
      </n-badge>
      <n-badge class="container" value="WIP" type="info" processing>
        <n-card class="bg-white dark:bg-gray-100" title="Entity Extraction">
          Card Content
        </n-card>
      </n-badge>
    </div>
  </div>
</template>
<script setup lang="ts">
</script>


