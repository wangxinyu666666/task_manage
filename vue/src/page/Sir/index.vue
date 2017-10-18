<template>
  <div>
    <Hello1>
      <transition name="fade">
          <router-view class="view"></router-view>
        </transition>
    </Hello1>
  </div>
</template>

<script>
   import Hello1 from '@/components/Hello.vue'
   export default {
     name: 'app',
     components: {Hello1},
     data () {
       return{
       }
     }
   }
</script>

<style>
.fade-enter-active, .fade-leave-active {
    transition: all .5s;
  }
  .fade-enter, .fade-leave-active {
    opacity: 0;
  }

  .list-enter-active, .list-leave-active {
    transition: all 1s;
  }
  .list-enter, .list-leave-active {
    opacity: 0;
    transform: translateY(30px);
  }
</style>
