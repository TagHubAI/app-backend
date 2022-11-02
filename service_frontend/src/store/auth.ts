import { defineStore } from 'pinia'
import { isJwtExpired } from 'jwt-check-expiration';
import axios from 'axios'


// Use message to announce login complete

export const useAuthStore = defineStore({
id: 'auth',
state: () => ({
  // initialize state from local storage to enable user to stay logged in
  data: JSON.parse(localStorage.getItem('authData') as string),
  returnUrl: null,
}),
actions: {
  async login(email: string) {
    const supabase = useSupabaseStore().supabaseClient

    const { data, error } = await supabase.auth.signInWithOtp({ email: email })

    // store user details and jwt in local storage to keep user logged in between page refreshes
    localStorage.setItem('authData', JSON.stringify(data))

    // Set to current auth data
    this.data = data

    return {data ,error}
  },
  setCurrentToken(token: string) {
    localStorage.setItem('token', token)
    axios.defaults.headers.common["Authorization"] = `Bearer ${token}`
  },
  isTokenExpired(token: string) {
    if (isJwtExpired(token)) {
      return true
    }
    return false
  },
  isCurrentTokenExpired() {
      if ('token' in localStorage) {
        return this.isTokenExpired(localStorage.getItem('token'))
      }
      return true
  },
  removeCurrentToken(){
    localStorage.removeItem("token")
  },
  async isCurrentTokenValid() {
    const token = localStorage.getItem('token') as string
    // const { data: { user } } = await supabase.auth.getUser(token)
    if (!this.isTokenExpired(token) && user && user.aud == "authenticated"){
      return true
    }
    return false
  },
  logout() {
    const router = useRouter()
    this.data = null
    this.removeCurrentToken()
  },
},
})
