import { createApp } from 'vue'
import App from './App.vue'
import Login from './Login.vue'

import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";

const app = createApp(App)
app.component('login', Login)
app.mount('#app')
