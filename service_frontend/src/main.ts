import { ViteSSG } from 'vite-ssg'
import { setupLayouts } from 'virtual:generated-layouts'
import Previewer from 'virtual:vue-component-preview'
import { OhVueIcon } from 'oh-vue-icons'
// import {
//   BiTypeH1,
//   BiTypeH2,
//   BiTypeH3,
//   FaUserAstronaut,
//   HiChevronDoubleLeft,
//   HiChevronDoubleRight,
//   HiPlus,
//   HiSolidSearch,
//   HiTrash,
//   MdDragindicator,
// } from 'oh-vue-icons/icons'
import naive from 'naive-ui'
import VueApexCharts from 'vue3-apexcharts'
import App from './App.vue'
import type { UserModule } from './types'
import generatedRoutes from '~pages'

import '@unocss/reset/tailwind.css'
import './styles/main.css'
import './styles/lotion.css'
import 'uno.css'
//
const routes = setupLayouts(generatedRoutes)
// addIcons(
//   MdDragindicator,
//   HiTrash,
//   HiPlus,
//   HiSolidSearch,
//   BiTypeH1,
//   BiTypeH2,
//   BiTypeH3,
//   HiChevronDoubleLeft,
//   HiChevronDoubleRight,
//   FaUserAstronaut,
// )

// https://github.com/antfu/vite-ssg
export const createApp = ViteSSG(
  App,
  { routes, base: import.meta.env.BASE_URL },
  (ctx) => {
    // install all modules under `modules/`
    Object.values(import.meta.glob<{ install: UserModule }>('./modules/*.ts', { eager: true }))
      .forEach(i => i.install?.(ctx))
    ctx.app.use(Previewer)
    ctx.app.use(naive)
    ctx.app.use(VueApexCharts)
    ctx.app.component('v-icon', OhVueIcon)
  },
)

