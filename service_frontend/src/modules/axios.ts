import axios from 'axios'
import { type UserModule } from '~/types'
import VueAxios from 'vue-axios'

 
// interface AxiosOptions {
//     baseUrl?: string
//     token?: string
// }

export const install: UserModule = ({ app }) => {
        axios.defaults.baseURL = import.meta.env.VITE_API_ENDPOINT 
        app.use(VueAxios, axios)
        app.provide('axios', app.config.globalProperties.axios)
    }
