import { createRouter, createWebHistory } from 'vue-router'
import { setupLayouts } from 'virtual:generated-layouts'
import generatedRoutes from 'virtual:generated-pages'
import LoginPage from '../views/LoginPage.vue'
import HomePage from '../views/HomePage.vue'
import UserSettingsPage from '../views/UserSettingsPage.vue'

import BuildPage from '../views/BuildPage.vue'
import RunPage from '../views/RunPage.vue'
import AnalyticsPage from '../views/AnalyticsPage.vue'
import NotFoundPage from '../views/NotFoundPage.vue'
import RegisterPage from '../views/RegisterPage.vue'
import "flowbite"

// const routes = setupLayouts(generatedRoutes)
const routes = [
  {
    path: "/",
    name: "Home",
    component: HomePage,
  },
  // Modeling
  {
    path: "/build",
    name: "Build",
    component: BuildPage,
  },
  {
    path: "/run",
    name: "Run",
    component: RunPage,
  },
  {
    path: "/analytics",
    name: "Analytics",
    component: AnalyticsPage,
  },
  {
    path: "/user-settings",
    name: "UserSettings",
    component: UserSettingsPage,
  },
  {
    path: "/login",
    name: "Login",
    component: LoginPage,
  },
  {
    path: "/register",
    name: "Register",
    component: RegisterPage,
  },
  {
    path: "/:pathMatch(.*)*",
    name: "404PageNotFound",
    component: NotFoundPage,
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
  scrollBehavior: (to) => {
    if (to) {
      return { selector: to.hash }
    }

    return { left: 0, top: 0 }
  },
})

export default router
