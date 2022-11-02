<script lang="ts">
import type {AxiosInstance} from 'axios'
import { emojify } from 'emojify-lyrics'
// const replaceWord = require('replace-word');

declare module '@vue/runtime-core' {
  interface ComponentCustomProperties {
    $axios: AxiosInstance
    catTags: string[]
  }
}

</script>
<script setup lang="ts">
import { useLoadingBar } from 'naive-ui'

// Is processed for the first time
const isProcessed = ref(false)

// Is data loading 
const isLoading = ref(false)

// Top loading bar
const loadingBar = useLoadingBar()

// Get axious
const axios = inject("axios")

const processedData = ref({})

function handleSubmitData(){
}

// get processed data after clicking submit button
const getProcessedData = async () => {
  loadingBar.start()
  isLoading.value = true
  axios.post("v1/apps/topic_model/process", {text_data: textData.value}).then((response: any) => {processedData.value = response.data; loadingBar.finish(); isLoading.value = false;isProcessed.value = true})
}

// FOR CHART
const options = {}
const series = [44, 55, 41, 17, 15]
const textData = ref("")

onMounted(()=>{
  const axios: any = inject('axios')  // inject axios
})
</script>

<template>
  <div class="flex justify-between">

    <!-- Data input form -->
    <div class="container w-1/4">
      <div class="text-lg text-black dark:text-white">
        Text data
      </div>
      <div class="color-gray-500" />
      <textarea v-model="textData" id="message" rows="20" class="block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Your text data separate by line:&#10;&#10;Today is a nice day&#10;I don't feel so good today" />
      <div class="py-4 text-black dark:text-white">
        <n-space class="py-2">
            Emojification: <n-switch v-model:value="active" />
        </n-space>
        <n-button
          :loading="isLoading"
          class="bg-white dark:bg-black font-bold  px-4 rounded focus:outline-none focus:shadow-outline border border-black dark:border-white text-lg"
          type="button"
          @click="getProcessedData"
        >
          Process
        </n-button>
      </div>
    </div>

    <!-- Data analytics -->
    <div
      :class="{ 'bg-gray-100 dark:bg-coolGray-700 justify-center items-center': !isProcessed, 'bg-white': isProcessed }"
      class="flex flex-wrap container overflow-auto max-h-150 text-lg text-middle rounded mx-4 border border-gray-300"
    >
      <div v-if="!isProcessed">
        <span class="inline-block text-gray-500 align-middle">
          Your data will appear here
        </span>
      </div>
      <div v-else>
        <div class="p-4 grow">
          <div class="flex w-full flex-wrap flex-row gap-4">
            <!-- Block of chart  -->
            <div v-for="(topicItem, topicKey) in processedData" class="flex p-4 w-full rounded-md	 border border-gray-150 justify-between">
              <div class="w-full mb-4">
                <span class="text-lg p-2 text-black">Topic #{{topicKey}} ({{ topicItem.count }} samples)</span>
                <div class="p-2">
                  <n-space>
                    <n-tag v-for="(t,key) in topicItem.topic" v-bind:key="key">
                      <!-- {{ t[0] }} ({{ t[1] }}%) -->
                      {{ emojify(t[0]) }} ({{ t[1] }}%)
                    </n-tag>
                  </n-space>
                </div>
                <n-collapse class="mt-4 bg-gray-100">
                  <n-collapse-item title="Show example" name="1">
                    <div class="px-4">
                      <span v-for="(textLine,textLineKey) in topicItem.data"> 
                        [{{textLineKey}}] {{emojify(textLine)}}<br><br>
                        <!-- [{{textLineKey}}] {{textLine}}<br><br> -->
                      </span>
                    </div>
                  </n-collapse-item>
                </n-collapse>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.n-card {
}
</style>
