<template>
  <div>
    <!--el-row :gutter="40" justify>
      <el-col :span="5" :offset="6">
        <el-input placeholder="模糊查询" icon="search" v-model="inputDataForSearch" :on-icon-click="filterByInputDataForSearch">
        </el-input>
      </el-col>
      <el-col :span="3">
        <div style="display:flex">
          <el-button type="primary" icon="search" @click="filterByInputDataForSearch">
            查询
          </el-button>
          <el-button type="primary" icon="delete2" @click="delInputDataForSearch" >
            清空
          </el-button>
        </div>
      </el-col>
    </el-row-->
    <el-row style="margin-top:30px">
      <el-col :span="22" :offset="1">
        <el-table :data="AllTask" height="600" border style="width:100%; text-align:center;">
          <el-table-column prop="num" label="序号" width="50"></el-table-column>
          <el-table-column prop="taskname" label="任务包名" width="200"></el-table-column>
          <el-table-column prop="name" label="负责人名" width="100"></el-table-column>
          <el-table-column prop="start" label="开始时间" width="120"></el-table-column>
          <el-table-column prop="end" label="结束时间" width="120"></el-table-column>
          <el-table-column prop="state" label="状态" width="100"></el-table-column>
          <el-table-column prop="percent" label="任务量百分比" width="150"></el-table-column>
          <el-table-column label="操作">
           <template scope="scope">
              <el-button @click.native.prevent="Detail(scope.$index,AllTask)" type="text" size="small"> 查看详情 </el-button>
           </template>
         </el-table-column>
      </el-table>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import  Axios from 'axios'
export default{
  data(){
    return{
      AllTask:[/*{
        num:1,
        taskname:"实验室任务管理",
        name:'彭一',
        start:'2017-9-5',
        end:'2017-10-1',
        state:'未完成',
        percent:"100%"
      }*/]
    }
  },
  methods: {
  /*  filterByInputDataForSearch() {
      //查询关键字信息
    },
    delInputDataForSearch(){
      //清空搜索条件
    },*/
    Detail(index, rows) {
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
  mounted() {
    //向后台发送axios信息获取登录信息进行表格填充
//   Axios.get('./mock/AllTask.json')
 Axios.get('/api/stu')
  .then(function(res){
      //成功获取json数据信息的话
      //console.log(res.data.AllTask[0]);
      var tem=[];
      var len=res.data.AllTask.length;
      var state_flag;
      for (var i = 0; i < len; i++)
       {
         if(res.data.AllTask[i].state<0) state_flag="结束";
         else state_flag="进行中";
         tem.push({
           num:i+1,
           taskname:res.data.AllTask[i].taskname,
           name:res.data.AllTask[i].name,
           start:res.data.AllTask[i].start,
           end:res.data.AllTask[i].end,
           percent:res.data.AllTask[i].percent,
           state:state_flag,
         });
      }
      this.AllTask=tem;
    }.bind(this)
   ).catch(function(){
     cosole.log("出现错误");
   })
  }
}
</script>

<style>
body{margin: 0}

</style>
