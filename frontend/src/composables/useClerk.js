// Minimal Clerk composable for direct JS SDK usage
// Usage: import { useClerk } from '@/composables/useClerk'

export function useClerk() {
  // Wait for Clerk to be loaded
  function getClerk() {
    return new Promise((resolve, reject) => {
      if (window.Clerk) return resolve(window.Clerk);
      const interval = setInterval(() => {
        if (window.Clerk) {
          clearInterval(interval);
          resolve(window.Clerk);
        }
      }, 50);
      setTimeout(() => reject(new Error('Clerk JS not loaded')), 5000);
    });
  }

  async function isSignedIn() {
    const Clerk = await getClerk();
    return Clerk.session && Clerk.session.id;
  }

  async function requireAuth(router, to, next) {
    const Clerk = await getClerk();
    if (Clerk.session && Clerk.session.id) {
      next();
    } else {
      next({ name: 'login', query: { redirect: to.fullPath } });
    }
  }

  return {
    getClerk,
    isSignedIn,
    requireAuth
  };
}
