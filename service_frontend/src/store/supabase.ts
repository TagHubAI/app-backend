import { defineStore } from 'pinia'
import { createClient } from '@supabase/supabase-js'

const supabaseUrl = import.meta.env.VITE_SUPABASE_URL
const supabaseAnonKey = import.meta.env.VITE_SUPABASE_ANON_KEY

export const useSupabaseStore = defineStore('supabase', () => {
  const supabaseClient = createClient(supabaseUrl, supabaseAnonKey)
  return {
    supabaseClient,
  }
})

