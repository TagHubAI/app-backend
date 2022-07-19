<script setup lang="ts">
import FeatureList from "@/components/core/FeatureList.vue"
import Footer from "@/components/core/Footer.vue";
import Hero from "@/components/core/Hero.vue";
import { ref } from "vue";

const data = ref(true)
const awesome = ref(true)

function toggle() {
    awesome.value = !awesome.value
}
</script>

<template>
    <Hero />

    <va-button-dropdown v-if="awesome" label="label" class="mr-2 mb-2">
        Content
    </va-button-dropdown>
    <button @click="toggle">toggle</button>
    <button></button>

    <FeatureList />
    <Footer />
</template>
