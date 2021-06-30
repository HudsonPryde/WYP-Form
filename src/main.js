import Vue from 'vue';
import {
  BootstrapVue, IconsPlugin, FormSelectPlugin,
} from 'bootstrap-vue';
import VueBootstrapToasts from 'vue-bootstrap-toasts';
import App from './App.vue';
import router from './router';

// Import Bootstrap an BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue);
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin);
Vue.use(FormSelectPlugin);
Vue.use(VueBootstrapToasts);

Vue.config.productionTip = false;

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
