<template>
       <div>
       <Header></Header>
        <div style="margin-top:5px">
            <el-row :gutter="10">
                <el-col :xs="4" :sm="4" :md="4" :lg="4">
                    <div>
                        <el-menu default-active="1" class="el-menu-vertical-demo" style="min-height:800px" @select="handleSelect">
                            <el-menu-item index="1"><i class="el-icon-message"></i>任务概览</el-menu-item>
                            <el-menu-item index="2"><i class="el-icon-menu"></i>发布任务</el-menu-item>
                            <el-menu-item index="3"><i class="el-icon-setting"></i>人员管理</el-menu-item>
                        </el-menu>
                    </div>
                </el-col>
                <el-col :xs="20" :sm="20" :md="20" :lg="20">
                    <div>
                        <div style="border: 1px solid #A6A6A6; border-radius:6px; padding:5px; margin:2px; background-color: white">
                            <el-breadcrumb separator="/">
                                <el-breadcrumb-item v-for="item in breadcrumbItems">{{item}}</el-breadcrumb-item>
                            </el-breadcrumb>
                        </div>
                    </div>

                    <div style="margin-top:10px">
                        <router-view></router-view>
                    </div>
                </el-col>
            </el-row>
        </div>
      </div>
</template>

<script>
    import Header from '@/components/header.vue'
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
                        this.$router.push('/Sir/AllTask');
                        this.breadcrumbItems  = ['任务概览']
                        break;
                    case '2':
                        this.$router.push('/Sir/NewTask')
                        this.breadcrumbItems  = ['发布任务']
                        break;
                    case '3':
                        this.$router.push('/Sir/AllPeople')
                        this.breadcrumbItems  = ['人员管理']
                        break;
                }
            },
        },
    }
</script>
<style>
body {
background:url('../images/timg.jpg') repeat 0px 0px;
height: 100%;
background-size: cover;
font-family: 'Open Sans', sans-serif;
background-attachment: fixed;
background-position: center;
}
</style>
