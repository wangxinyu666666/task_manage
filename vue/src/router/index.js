import Vue from 'vue'
import Router from 'vue-router'

import login from '@/page/login/login.vue'


import Sir from '@/page/Sir/index.vue' //一级路由
import AllPeople from '@/page/Sir/AllPeople.vue'
import ManageTask from '@/page/ManageTask.vue'
import NewTask from '@/page/Sir/NewTask.vue'
import OnePerson from '@/page/Sir/OnePerson.vue'
import AllTask from '@/page/AllTask.vue'

import Stu from '@/page/Stu/index.vue'
import MyTask from '@/page/Stu/MyTask.vue'
import Hello from '@/components/Hello.vue'
import SNewTask from '@/page/Stu/NewTask.vue'

import resetPassword from '@/page/resetPassword.vue'
import axios from 'axios'


Vue.use(Router)
Vue.prototype.$ajax = axios

export default new Router({
  routes: [
    {  path:'/login',
      component:login,
    },
    {
      path:'/resetPassword',
      component:resetPassword
    },
    {
      path:'/Sir',
      component:Sir,
      children:[
       {
        path: '', component: AllTask,
    },
    {
        path: 'AllTask', component: AllTask,
    },
        {
        path: 'AllPeople', component: AllPeople,
    },{
        path: 'ManageTask', component: ManageTask
    },{
        path:'NewTask', component: NewTask
    },
    {
        path:'MyTask', component: MyTask
    },
    {
        path:'/OnePerson', component: OnePerson
    },
    {
        path:'MyTask/:username', component: OnePerson
    },
    {
        path:'AllPeople/OnePerson/:username', component: OnePerson
    }

      ]
    },

    {
      path:'/Stu',
      component:Stu,
      children:[
        {path:'',component:AllTask},
        {path:'AllTask',component:AllTask},
        {path:'MyTask',component:MyTask},
        {path:'ManageTask',component:ManageTask},
        {path:'NewTask',component: SNewTask}
      ]
    }
  ]
})
