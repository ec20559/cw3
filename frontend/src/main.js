import { createApp } from 'vue';
import App from './App.vue';
import router from './router';  // Updated import to use the router configuration

import "bootstrap/dist/css/bootstrap.min.css";

const app = createApp(App);
app.use(router);  // Use the router configuration
app.mount('#app');

