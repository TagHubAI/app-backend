<script lang="ts">
import type { Component } from 'vue'
import { defineComponent, h, ref } from 'vue'
import { NIcon } from 'naive-ui'
import type { MenuOption } from 'naive-ui'
import {
  CodeWorkingOutline as CodeIcon,
  CubeOutline as CubeIcon,
  AlbumsOutline as DataIcon,
} from '@vicons/ionicons5'
import { RouterLink } from 'vue-router'

function renderIcon(icon: Component) {
  return () => h(NIcon, null, { default: () => h(icon) })
}

const menuOptions: MenuOption[] = [
  {
    label: () =>
      h(
        RouterLink,
        {
          to: {
            name: 'workflows',
          },
        },
        { default: () => 'Sentiment Analysis' },
      ),
    key: 'go-back-home',
    icon: renderIcon(CodeIcon),
  },
  {
    label: 'Semantic Grouping',
    key: 'hear-the-wind-sing',
    icon: renderIcon(CodeIcon),
  },
  {
    label: 'Entity Extraction',
    key: 'pinball-1973',
    icon: renderIcon(DataIcon),
    // children: [
    //  {
    //    label: 'Rat',
    //    key: 'rat'
    //  }
    // ]
  },
  {
    label: 'Apps',
    key: 'a-wild-sheep-chase',
    icon: renderIcon(CubeIcon),
  },
]

export default defineComponent({
  setup() {
    return {
      activeKey: ref<string | null>(null),
      collapsed: ref(true),
      menuOptions,
    }
  },
})
</script>

<template>
  <n-space vertical>
    <n-layout has-sider>
      <n-layout-sider
        class="sidebar"
        bordered
        collapse-mode="width"
        :collapsed-width="64"
        :width="240"
        :collapsed="collapsed"
        show-trigger
        @collapse="collapsed = true"
        @expand="collapsed = false"
      >
        <div class="column-2 flex place-content-between">
          <n-popover style="padding: 0" placement="bottom" trigger="click">
            <template #trigger>
              <n-button quaternary>
                <v-icon v-if="!collapsed" name="fa-user-astronaut" />
                <div v-if="!collapsed" class="text-right">
                  TagHubSuper
                </div>
              </n-button>
            </template>
            <n-card title="Card Slots Demo">
              <template #header>
                super@taghub.dev
              </template>
              <template #footer>
                Settings
              </template>
              <template #action>
                Logout
              </template>
            </n-card>
          </n-popover>
          <n-button quaternary @click="collapsed = !collapsed">
            <v-icon v-if="!collapsed" name="hi-chevron-double-left" scale="0.75" />
            <v-icon v-if="collapsed" name="hi-chevron-double-right" scale="0.75" />
          </n-button>
        </div>
        <n-menu
          v-model:value="activeKey"
          :collapsed="collapsed"
          :collapsed-width="64"
          :collapsed-icon-size="22"
          :options="menuOptions"
        />
      </n-layout-sider>
      <n-layout>
        <slot />
      </n-layout>
    </n-layout>
  </n-space>
</template>

<style>
.n-layout-toggle-button {
  display:none !important
  }
</style>
