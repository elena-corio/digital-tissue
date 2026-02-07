// Simple auth store using localStorage and Vue's reactivity system
import { ref } from 'vue'

export const isLoggedIn = ref(!!localStorage.getItem('speckle_token'))

export function login(token, username) {
  localStorage.setItem('speckle_token', token)
  if (username) localStorage.setItem('speckle_username', username)
  isLoggedIn.value = true
}

export function logout() {
  localStorage.removeItem('speckle_token')
  localStorage.removeItem('speckle_username')
  isLoggedIn.value = false
}
