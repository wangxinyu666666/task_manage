<template>
<div class="mytask">
  <el-row :gutter="40" justify style="color: #FFF; font-size: 20px;">
    <el-col :span="5" :offset="6">
      <p>{{username}}</p>
    </el-col>
    <el-col :span="8">
      <p>任务量累计：{{percent}}</p>
    </el-col>
  </el-row>

  <el-row style="margin-top:10px">
    <el-col :span="22" :offset="1">
      <el-table :data="MyTask" height="600" border style="width:100%">
       <el-table-column label="参与项目" prop="project"></el-table-column>
       <el-table-column label="担任角色" prop="actor"></el-table-column>
       <el-table-column label="所占比例" prop="OnePer"></el-table-column>
     </el-table>
    </el-col>
  </el-row>
</div>
</template>

<script>
import Axios from 'axios'
export default{
  data(){
    return{
      username:this.$store.state.username,
      percent:"",
      MyTask:[/*{
        project:"实验室任务管理",
        actor:"组长",
        OnePer:"60%"
    }*/],
  }},
  methods: {
  Detail(index, rows) {
        //key是得到的单个任务的名字,点击之后向后台发送请求。跳转到单个任务的详情界面
        //现在要进行处理，发送axios请求得到的数据用来渲染任务详情的页面
        var key=rows[index].taskname;
          //  console.log(key);
          //key是单个页面信息，得到之后对应vuex中的taskid存下来
          this.$store.commit("setTaskId", key)
          //console.log(this.$store.state.taskid);
          //跳转到管理界面
         var user=JSON.parse(sessionStorage.getItem('user'));
         if(user.username=="赵振华"){
             this.$router.push('/Sir/ManageTask');
         }
         else{
           this.$router.push('/Stu/ManageTask')
         }

        }
  },
  mounted(){
    //do something after mounting vue instance
    var user=JSON.parse(sessionStorage.getItem('user'));
  //  Axios.get('./mock/MyTask.json')
   Axios.get('api/Stu/MyTask?name='+this.$store.state.username)
   .then(function(res){
       //成功获取json数据信息的话
      // console.log(res.data.percent);
      this.percent=res.data.percent;
       var tem=[];
       var len=res.data.MyTask.length;
       for (var i = 0; i < len; i++)
        {
          tem.push({
            project:res.data.MyTask[i].project,
            actor:res.data.MyTask[i].actor,
            OnePer:res.data.MyTask[i].OnePer
          })
       }
       this.MyTask=tem;
     }.bind(this)
    ).catch(function(){
      console.log("出现错误");
    })
   }
  }
</script>
<style>
body{margin: 0}
.demo-table-expand {
   font-size: 0;
 }
 .demo-table-expand label {
   width: 90px;
   color: #99a9bf;
 }
 .demo-table-expand .el-form-item {
   margin-right: 0;
   margin-bottom: 0;
   width: 100%;
 }
</style>
