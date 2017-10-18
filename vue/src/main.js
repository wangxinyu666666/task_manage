// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'

import 'element-ui/lib/theme-default/index.css'
import VueRouter from 'vue-router'

import store from './vuex/store'

Vue.config.productionTip = false
Vue.use(ElementUI)
//url权限设置（没有登录信息除了登录界面其他界面全部拦截）
router.beforeEach((to,from,next)=>{
  if(to.path=='/login'){
    sessionStorage.removeItem('user');
  }
  //回到登录页，清除信息
  let user=JSON.parse(sessionStorage.getItem('user'));
  //读取用户信息。没有用户信息去其他页面就拦截，否则就跳转
  if(!user && to.path!='/login'){
    next({path:'/login'});
  }
  else{
      next()

  }
});
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  template: '<App/>',
  components: { App }
})
