<template>
  <div>
     <div id="steps">
       <el-steps :space="400" :active="2" finish-status="success">
          <el-step title="发布任务" ></el-step>
          <el-step title="任务划分"></el-step>
          <el-step title="查看详情"></el-step>
        </el-steps>
     </div>
     <div id="container1" v-if="need">
       <h3 id="h3">{{this.$store.state.taskid}}</h3>
       <div id="base" v-if=base>
       <div class="img-wrapper">
           <img src="https://d13yacurqjgara.cloudfront.net/users/2733/screenshots/741958/dribbble-foxes.jpg" alt="Just Background">
       </div>
       <p class="detail">From {{start}} To {{end}} <br/><br/>组长:{{actor}} <br/><br/>组员:{{groPeo}}</p>
       </div>
       <i  id="icon" v-if="base" class="el-icon-information"  @click="showdetails"></i>

         <div id="change" v-if=change>
         <p class="detail">任务详情:<br/>{{desc}}</p>
        <center><el-button type="primary" @click="edit">编辑任务</el-button></center>
        </div>
        <i id="icon" v-if="change"class="el-icon-information"  @click="returnback"></i>
    </div>

   <!--此处启用编辑模式-->
    <div id="form1" v-if="showform">
      <br/><br/>
       <el-form :inline=true ref="ruleForm" :rules="rules" :model="newform" label-width="80px" >
          <el-form-item label="任务名" prop="misname">
            <el-input v-model="newform.misname"></el-input>
          </el-form-item>

          <el-form-item label="比例" prop="misper">
             <el-select v-model="newform.misper" placeholder="请选择任务比例">
            <el-option
             v-for="item in peroptions"
             :label="item.label"
             :value="item.value">
            </el-option>
          </el-select>%
       </el-form-item>

       <el-form-item  label="负责人" prop="mispeo">
         <el-select v-model="newform.mispeo" placeholder="请选择任务负责人">
           <el-option
            v-for="item in peoptions"
            :label="item"
            :value="item">
           </el-option>
        </el-select>
      </el-form-item>

    <el-form-item  label="任务状态" prop="miscon">
      <el-radio-group v-model="newform.miscon">
        <el-radio label="完成">完成</el-radio>
        <el-radio label="未完成">未完成</el-radio>
      </el-radio-group>
   </el-form-item>

   <el-form-item  label="截止时间" prop="misend">
     <el-date-picker  v-model="newform.misend" type="date" placeholder="选择日期"  :picker-options="pickerOptions0" @change="setMisend">
    </el-date-picker>
  </el-form-item>
    <br/>
     <el-form-item label="任务描述" prop="misdetail">
       <el-input type="textarea" v-model="newform.misdetail"></el-input>
    </el-form-item>
   <center>
    <el-form-item>
       <el-button  @click="insert('ruleForm')">添加</el-button>
       <el-button  @click="resetForm('ruleForm')">重置</el-button>
    </el-form-item>
    </center>
   </el-form>
   </div>
   <!--显示已经有的信息-->
  <div id="taskDetail" v-if="showform">
    <el-row>
       <el-col :span="4" v-for="(showtask, index) in TaskDetail"  :offset="index%5 >0 ? 1:0 ">
            <div style="padding: 14px;" class="onedetail">
              <span>{{showtask.misname}}</span>
              <p>{{showtask.mispeo}}</p>
             <div class="bottom clearfix">
               <button  v-on:click="editTask(index)">编辑</button>
               <button  v-on:click="dele(index)">删除</button>
             </div>
           </div>
     </el-col>
   </el-row>
  </div>
  <div id="submit" v-if="showform">
    <center>
      <el-button type="primary" @click="submitForm()">提交</el-button>
    </center>
  </div>
</div>
</template>

<script>
 import Axios from 'axios'
 export default{
   data(){
     return{
         base:true,
         change:false,
         need:true,
         showform:false,
         start:"", //大任务开始时间
         end:"" ,//大任务结束时间
         actor:"", //组长
         groPeo:"" ,//组员
         desc:"" ,//任务详情
         TaskDetail:[],
         newform:{
           misname:"",
           mispeo:"",
           misper:"",
           miscon:"未完成",
           misend:"",
           misdetail:""
         },
         //填充下拉列表
         peroptions:[{
           value:"5",
           label:"5"
         },
         {
           value:"10",
           label:"10"
         },
         {
           value:"15",
           label:"15"
         },
         {
           value:"20",
           label:"20"
         },
         {
           value:"25",
           label:"25"
         },
         {
           value:"30",
           label:"30"
         },
         {
           value:"35",
           label:"35"
         },
         {
           value:"40",
           label:"40"
         },
         {
           value:"45",
           label:"45"
         },{
           value:"50",
           label:"50"
         },
         {
           value:"55",
           label:"55"
         },{
           value:"60",
           label:"60"
         },{
           value:"65",
           label:"65"
         },
         {
           value:"70",
           label:"70"
         },{
           value:"75",
           label:"75"
         },{
           value:"80",
           label:"80"
         },{
           value: "85",
           label:"85"
         },{
           value:"90",
           label:"90"
         },
         {
           value:"95",
           label:"95"
         }],
         //填充学生的列表,动态列表（组员和组长组成）
         //peoptions:["刘文健","周桐","彭一","陈飞坤","姜金霖","吴炜锋","王心雨","兰子宁","江宇川"],
         peoptions:[],
         //日期选择器
         pickerOptions0: {
             disabledDate(time) {
               return time.getTime() < Date.now() - 8.64e7;
             }
         },
         //学生的表单验证方式
         rules: {
           misname: [
             { required: true, message: '请输入任务名', trigger: 'blur' },
             { min: 1 , message: '长度在至少1个字', trigger: 'blur' }
           ],
           misdetail: [
             { required: true, message: '请填写任务的详细信息', trigger: 'blur' }
           ]
         }
          }
     },
   methods: {
      showdetails() {
        //显示学长的详情
       this.base=false;
       this.change=true;
     },
     returnback(){
       //显示基础页面
       this.base=true;
       this.change=false;
     },
     edit(){
       //点击编辑按钮
       this.need=false;
       this.showform=true;
     },
     setMisend(val){
       //日期格式化
         console.log(val);
         this.newform.misend=val;
     },
     resetForm(formName) {
       //重置表单
        this.$refs[formName].resetFields();
      },
    insert(formName){
      //添加一个选项
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.TaskDetail.push({
               misname:this.newform.misname,
               mispeo:this.newform.mispeo,
               misper:this.newform.misper,
               miscon:this.newform.miscon,
               misend:this.newform.misend,
               misdetail:this.newform.misdetail
           });
             this.$refs[formName].resetFields();
        }
        else {
          console.log('表单填写不完整');
          return false;
        }
      })
    },
    dele(index){
      //删除任务
      if(index !==-1){
           this.TaskDetail.splice(index,1);
      }
    },
    editTask(index){
      //重新编辑任务,先删除
      this.newform=this.TaskDetail[index];
      if(index !==-1){
           this.TaskDetail.splice(index,1);
      }
    },
    submitForm(){
      //向后台提交信息
          var taskname=this.$store.state.taskid;
          var mydata={"TaskDetail":this.TaskDetail};
          var postdata=JSON.stringify(mydata);
          console.log(postdata);
          Axios.post("/api/managetask?task="+taskname,postdata,{ headers: { 'Content-Type': 'application/json' } })
          .then(function(res){
            console.log("success");
          })
          .catch(function(err){
            console.log("fail");
          })
    }
  },
  mounted() {
      //填充信息
     var taskname=this.$store.state.taskid;
     Axios.get('/api/managetask?task='+taskname)
  //   Axios.get('./mock/ManageTask.json')
    .then(function(res){
        this.start=res.data.start;
        this.end=res.data.end;
        this.actor=res.data.actor;
        this.groPeo=res.data.groPeo;
        this.desc=res.data.desc;
        var i;
        //填充人员选择的下拉列表,组长和组员
        this.peoptions.push(res.data.actor);
        var peolen=res.data.groPeo.length;
        for (i=0;i<peolen;i++){
           if(res.data.groPeo[i]!=res.data.actior)
              this.peoptions.push(res.data.groPeo[i]);
           else continue;
        }
      }.bind(this)
     )
     .catch(function(){
       console.log("出现错误");
     })
    }
  }
</script>
<style>
@import url(https://fonts.googleapis.com/css?family=Roboto:400,300);

html {
    height: 100%;
}

body {
    height: 100%;
    padding: 0;
    margin: 0
}

button:focus {
    outline: none;
}

button:hover {
    opacity: .8;
}

.fa {
    font-size: 20px;
}

.fa-info {
    color: white;
}
#steps{

  position: absolute;
  left:28%
}
#container1 {
    width:800px;
    height:620px;
    overflow: auto;
    background:white;
    position: relative;
    top:400px;
    left: 50%;
    box-shadow: 0 5px 15px 0 rgba(0,0,0,0.25);
    transform: translate3d(-50%, -50%, 0);
}

#h3 {
    padding: 20px;
    color: white;
    background: #3E4FB2;
    font-weight: 300;
    text-align: center;
    font-size: 18px;
    font-family: 'Roboto', sans-serif;
}

.detail {
    color: #777;
    padding: 20px;
    line-height: 1.5;
   font-family: 'Roboto', sans-serif;
}

.img-wrapper {
    padding: 0;
    position: relative;
}

.img-wrapper:after {
    content: "";
    position: absolute;
    left: 0;
    top: 0;
    right: 0;
    bottom: 0;
    background: rgba(62, 79, 178, .25);
    width: 100%;
}

.img-wrapper img {
    width: 100%;
    height: 300px;
    -o-object-fit: cover;
    object-fit: cover;
    margin: 0;
    display: block;
    position: relative;
}
#icon{
  position: relative;
  bottom:0px;
  right:-760px;
}
#form1{
      width:700px;
      height:350px;
      overflow: auto;
      position:relative;
      top: 240px;
      left: 50%;
      transform: translate3d(-50%, -50%, 0);
}
#taskDetail{
  position: relative;
  top:80px;
  overflow: auto;
  height:120px;
}
.onedetail{
  background: lightgrey;
}
#submit{
  position: relative;
  top:100px;
}
</style>
