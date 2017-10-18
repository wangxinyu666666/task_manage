<template>
  <div id="app">
    <transition name="el-fade-in">
        <router-view></router-view>
    </transition>
  </div>
</template>

<script>
export default {
  name: 'app',
  data: function (){
    return {
      active:true,
      headerFixed : true
    }
  },
  created: function(){
    this.$router.push('/login');
  }
  
}
</script>

<style>
body{margin: 0;}
#app {
  min-width: 1200px;
  margin: 0 auto;
  font-family: "Helvetica Neue","PingFang SC",Arial,sans-serif;
}

</style>
