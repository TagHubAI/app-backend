import NProgress from 'nprogress'
import { type UserModule } from '~/types'

export const install: UserModule = ({ isClient, router }) => {
  if (isClient) {
    router.beforeEach((to, from) => {
      if (to.path !== from.path)
        NProgress.start()
    })
    // router.afterEach((to, from) => {
    //   const toDepth = to.path.split('/').length
    //   const fromDepth = from.path.split('/').length
    //   to.meta.transitionName = toDepth < fromDepth ? 'slide-right' : 'slide-left'
    // })
    router.afterEach(() => { NProgress.done() })
  }
}
