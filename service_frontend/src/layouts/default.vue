<script setup lang="ts">
const auth = useAuthStore()
const { t } = useI18n()
const router = useRouter()
// const toggleLocales = () => {
// change to some real logic
//   const locales = availableLocales
//   locale.value = locales[(locales.indexOf(locale.value) + 1) % locales.length]
// }
const handleLogout = () => {
  auth.logout()
  router.push('/')
}
</script>

<template>
  <main class="dark:text-gray-200">
    <div class="flex text-white bg-black text-xl justify-between">
      <span class="text-white mx-4 my-4 ">
        <router-link to="/apps">
          TagHub.Dev
        </router-link>
      </span>
      <span class="mx-4 my-4">
        <div class="flex">
          <div class="inline-block">
            <span class="inline-block align-middle mt-2">
              <button class="icon-btn mx-2 !outline-none" :title="t('button.toggle_dark')" @click="toggleDark()">
                <div i="carbon-sun dark:carbon-moon" />
              </button>
            </span>
            <span class="inline-block align-middle">
              <span>
                Patrick (Credit left: 10000)
              </span>
            </span>
            <span class="inline-block align-middle pl-2">
              <n-button @click='handleLogout' class="text-white">
                Log out
              </n-button>
            </span>
          </div>
        </div>
      </span>
    </div>
    <div class="px-6 py-6">
      <Breadcrumb />
      <div class="px-4 py-4">
        <RouterView />
      </div>
    </div>
  </main>
</template>


<style>
.full-height {
  height: 100vh;
  max-height: 100vh;
  min-height: -moz-available;
  min-height: -webkit-fill-available;
  min-height: fill-available;
}
</style>
