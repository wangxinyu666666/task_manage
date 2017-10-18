<template>
    <div class="body">
       <Header></Header>
        <div style="margin-top:5px">
            <el-row :gutter="10">
                <el-col :xs="4" :sm="4" :md="4" :lg="4">
                    <div class="menu">
                        <el-menu default-active="1" class="el-menu-vertical-demo" style="min-height:800px;" @select="handleSelect">
                            <el-menu-item index="1"><i class="el-icon-message"></i>任务概览</el-menu-item>
                            <el-menu-item index="2"><i class="el-icon-menu"></i>个人页</el-menu-item>
                            <el-menu-item index="3"><i class="el-icon-setting"></i>任务管理</el-menu-item>
                        </el-menu>
                    </div>
                </el-col>
                <el-col :xs="20" :sm="20" :md="20" :lg="20">
                    <div style="margin-top:20px">
                        <router-view></router-view>
                    </div>
                </el-col>
            </el-row>
        </div>
    </div>
</template>
<script>
    import Header from'@/components/header.vue'
    export default {
       components: {Header},
        data(){
            return {
                searchCriteria: '',
            }
        },

        methods:{
            handleSelect(key, keyPath){
                switch(key){
                    case '1':
                        this.$router.push('/Stu/AllTask');
                        this.breadcrumbItems  = ['任务概览']
                        break;
                    case '2':
                        this.$router.push('/Stu/MyTask')
                        this.breadcrumbItems  = ['个人页']
                        break;
                    case '3':
                        this.$router.push('/Stu/ManageTask')
                        this.breadcrumbItems  = ['任务管理']
                        break;
                }
            },
        }
      }
</script>
<style>
body{
  .body {
  background:url('../images/timg.jpg') repeat 0px 0px;
  height: 100%;
  background-size: cover;
  font-family: 'Open Sans', sans-serif;
  background-attachment: fixed;
  background-position: center;
  }
}
</style>
