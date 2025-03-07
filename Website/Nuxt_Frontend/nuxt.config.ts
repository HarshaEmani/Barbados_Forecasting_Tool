import Aura from '@primevue/themes/aura';

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },
  modules: [
    '@primevue/nuxt-module',
    "nuxt-plotly",
  ],
  vite: {
    optimizeDeps: {
      include: ["plotly.js-dist-min"],
    },
  },
  css: [
    'primeicons/primeicons.css'
  ],
  primevue: {
    /* Configuration */
    usePrimeVue: true,
    autoImport: true,
    components: {
      include: '*',
    },
    options: {
      theme: {
        preset: Aura,
        options: {
          darkModeSelector: 'light',
        }
      }
    }
  },
})