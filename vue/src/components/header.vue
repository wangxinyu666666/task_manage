<template>
  <div id="app">
  <header class="header" :class="{'header-fixed':headerFixed}">
    <el-row>
      <el-col :span="24">
      <el-col :span="10" class="logo">
        {{sysName}}
      </el-col>
      <el-col :span="4" class="userinfo">
        <el-dropdown trigger="hover">
          <span class="el-dropdown-link userinfo-inner"> {{sysUserName}}</span>
          <el-dropdown-menu slot="dropdown">
            <el-dropdown-item @click.native="person" >个人中心</el-dropdown-item>
            <el-dropdown-item  @click.native="logout">退出登录</el-dropdown-item>
          </el-dropdown-menu>
        </el-dropdown>
      </el-col>
    </el-col>
  </el-row>
</header>
</div>
</template>

<script>
export default {
    data(){
        return {
            searchCriteria: '',
            sysName:'实验室任务管理',
            sysUserName: 'hhh',
            headerFixed:true
        }
    },

    methods:{
      logout() {
        var _this = this;
        this.$confirm('确认退出吗?', '提示', {
          //type: 'warning'
        }).then(() => {
          sessionStorage.removeItem('user');
          _this.$router.push('/login');
        }).catch(() => {

        });
      },
      person(){
        //进入到个人页，先判断身份，如果是学长进入到所有学生的管理页，如果是学生进入他的个人页
        var user=JSON.parse(sessionStorage.getItem('user'));
        var _this=this;
        //对user进行验证
        if(user.username=="赵振华"){
          //如果是学长(确定后台学长的username)
          _this.$router.push('/Sir/Allpeople');
        }
        else{
          //是学生
          _this.$router.push('/Stu/Mytask');
        }
      },
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
    mounted(){
        var user = sessionStorage.getItem('user');
        if (user) {
            user = JSON.parse(user);
            this.sysUserName = user.username || '';
        }
    }
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
#app{
	min-width: 1200px;
	margin: 0 auto;
	font-family: "Helvetica Neue","PingFang SC",Arial,sans-serif;
}
header{z-index: 1000;min-width: 1200px;transition: all 0.5s ease;  border-top: solid 4px #3091F2;
	 background-color:#8080FF;  box-shadow: 0 2px 4px 0 rgba(0,0,0,.12),0 0 6px 0 rgba(0,0,0,.04);  }

.userinfo{
   text-align: right;
	 padding-right: 35px;
	 float:right;
}
.userinfo-inner{
	cursor:pointer;
	color:white;
}
//如果后期要加图片的话
img{
	width: 40px;
	height: 40px;
	border-radius: 20px;
	margin: 10px 0px 10px 10px;
	float: right;
}
.logo{
	height: 60px;
	font-size:22px;
	padding-left: 20px;
	padding-right: 20px;
	border-color: rgba(238,241,146,0.3);
	border-right-width: 1px;
	border-right-style: solid;
	width: 230px;
	color:white;
}
#app main .aside .is-active{color: #475669;}
</style>
