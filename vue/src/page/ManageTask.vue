<template>
  <!--这个界面显示详情界面/组长有编辑的权限-->
<div>
    <h2 class="head">{{this.$store.state.taskid}}</h2>
    <div class="left">
      <!--显示学长的需求-->
    <br>
    <p>项目开始时间：{{start}}</p>
    <br>
    <p>项目结束时间:{{end}}</p>
    <br>
    <p>组长：{{actor}}</p>
    <br>
    <p>成员：{{groPeo}}</p>
    <br>
    <p>需求描述:<br><br>
    {{ desc}}</p>
  </div>
  <div class="IP-line"></div>
  <div class="right">
    <br><br>
   <el-table :data="TaskDetail" style="width:100%">
     <el-table-column type="expand">
       <template scope="props">
         <el-form lable-position="left" inline class="demo-table-expand">
           <el-form-item label="详情描述"><span>{{props.row.misdetail}}</span></el-form-item>
         </el-form>
       </template>
     </el-table-column>
     <el-table-column label="任务名" width="80" prop="misname"></el-table-column>
     <el-table-column label="承担成员" width="90" prop="mispeo"></el-table-column>
     <el-table-column label="比例" width="70" prop="misper"></el-table-column>
     <el-table-column label="任务状态" prop="miscon"></el-table-column>
     <el-table-column label="任务截止时间" prop="misend"></el-table-column>
   </el-table>
  </div>
  <el-button v-if="editvisible" @click="dialogFormVisible=true" class="edit-button">编辑任务</el-button>

  <el-dialog title="编辑任务" :visible.sync="dialogFormVisible" style="width:120%">

    <div class="Sir" v-if="ifSir">
      <!--ifsir整个由新建任务的区域引进,区别在于把之前获得的后台信息填充到表格里面（母组件对于子组件的变量的处理）-->

  </div>

  <div class="Stu" v-if="ifStu">
    <el-form
    :inline=true
    ref="c1"
    :rules="rules"
    v-for="(StuForm,index) in StuForms"
    :model="StuForm"
    :key=StuForm.key
    >
      <el-form-item :label="'任务'+(index+1)+'名字'" prop="misname">
        <el-input v-model="StuForm.misname"></el-input>
     </el-form-item>

     <el-form-item :label="'比例'" prop="misper">
       <el-select v-model="StuForm.misper" placeholder="请选择任务比例">
         <el-option
          v-for="item in peroptions"
          :key="item.value"
          :label="item.label"
          :value="item.value">
          </el-option>
      </el-select>%
    </el-form-item>

    <el-form-item  :label="'组长'" prop="mispeo">
      <el-select v-model="StuForm.mispeo" placeholder="请选择组长">
        <el-option
         v-for="item in peoptions"
         :key="item"
         :label="item"
         :value="item">
         </el-option>
     </el-select>
   </el-form-item>

   <el-form-item  :label="'任务状态'" prop="miscon">
     <el-radio-group v-model="StuForm.miscon">
       <el-radio label="完成">完成</el-radio>
       <el-radio label="未完成">未完成</el-radio>
     </el-radio-group>
  </el-form-item>
  <br/>
  <el-form-item  :label="'截止时间'" prop="misend">
    <el-date-picker  v-model="StuForm.misend" type="date" placeholder="选择日期"  :picker-options="pickerOptions0" @change="setMisend">
   </el-date-picker>
 </el-form-item>
  <br/>
    <el-form-item label="任务描述" prop="misdetail">
      <el-input type="textarea" v-model="StuForm.misdetail"></el-input>
   </el-form-item>

   <el-form-item>
      <el-button @click="resetForm(StuForm)">重置任务</el-button>
      <el-button  @click.prevent="removeMission(StuForm)">删除任务</el-button>
   </el-form-item>
  <br/><br/><br/>
  </el-form>
  </div>

   <div slot="footer" class="dialog-footer">
      <el-button  v-if="ifStu" @click="addDomain()">新增任务</el-button>
      <el-button v-if="ifStu" type="primary" @click="submitForm('c1')">提交</el-button>
      <el-button @click="dialogFormVisible = false">取 消</el-button>
    </div>

  </el-dialog>
</div>
</template>

<script>
import Axios from 'axios'
export default{
  data(){
    return{
    start:"",
    end:"",
    actor:"",
    groPeo:"",
    desc:"",
    //表格的填充信息（如果可以这个也做成可编辑的状态）
    TaskDetail:[/*{
      misname:"",
      mispeo:"",
      misper:"",
      miscon:"",
      misend:"",
      misdetail:''
    }*/],
     editvisible:false,   //编辑按钮是否显示，组长和学长才有编辑的权限
     ifSir:false,       //是不是学长启用编辑，是的话显示内容不是的话隐藏
     ifStu:false,
     dialogFormVisible: false,  //对话框是否显示（通过点击编辑触发，通过点取消或者确定关闭，ps点击提交增加一个通知的功能哈）
     //表单信息（学长编辑任务= =等等考虑用路由形式给出）
     sirForm: {
       name: '', //大任务
       start: '', //结束时间
       end: '', //开始时间
       leader:'',  //组长
       member:'',  //成员信息
       goal: '',  //目标值
       desc: ''
     },
    //学生表单的信息
    StuForms:[],
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
      type: [
        { type: 'array', required: true, message: '请至少选择一个活动性质', trigger: 'change' }
      ],
      misdetail: [
        { required: true, message: '请填写任务的详细信息', trigger: 'blur' }
      ]
    }
     }
   },
   methods: {
     //日期选择器格式化
     setMisend(val){
         console.log(val);
     },
     //清空任务
     resetForm(formName) {
         formName.misname="";
         formName.misper='';
         formName.mispeo='',
         formName.miscon='未完成';
         formName.misend='';
         formName.misdetail='';
     },

       submitForm(formName){
          var taskname=this.$store.state.taskid;
          var len=this.$refs[formName].length;
          var flag=true;
          for(var i=0;i<len;i++){
              var form=this.$refs[formName][i];
              form.validate((valid) => {
                if (!valid){
                    flag=false
                 }
              })
              if(flag==false) break;
            }
          if(flag==true){
          //信息验证成功
          this. dialogFormVisible=false;  //关闭表单的信息
          var mydata={"TaskDetail":this.StuForms};
          var postdata=JSON.stringify(mydata);
          console.log(postdata);
          //向后台提交信息
          Axios.post("/api/managetask?task="+taskname,postdata, { headers: { 'Content-Type': 'application/json' } })
           .then(function(res){
            console.log("success");
          })
        .catch(function(err){
             console.log("fail");
         })
        //重新刷新数据
        Axios.get('/api/managetask?task='+taskname)
       .then(function(res){
           var tem=[];
           var axios_stuforms=[];
           var len=res.data.TaskDetail.length;
           for (var i = 0; i < len; i++)
            {
              tem.push({
                misname:res.data.TaskDetail[i].misname,
                mispeo:res.data.TaskDetail[i].mispeo,
                misper:res.data.TaskDetail[i].misper,
                miscon:res.data.TaskDetail[i].miscon,
                misend:res.data.TaskDetail[i].misend,
                misdetail:res.data.TaskDetail[i].misdetail
              })
              axios_stuforms.push({
                misname:res.data.TaskDetail[i].misname,
                mispeo:res.data.TaskDetail[i].mispeo,
                misper:res.data.TaskDetail[i].misper,
                miscon:res.data.TaskDetail[i].miscon,
                misend:res.data.TaskDetail[i].misend,
                misdetail:res.data.TaskDetail[i].misdetail
              })
           }
          this.StuForms=axios_stuforms;
          this.TaskDetail=tem;
         }.bind(this)
        ).catch(function(){
          console.log("出现错误");
        })
       }
       else {
         alert("表单信息不完整");
       }
     },

     //配置到每个表单中，选择性的删除某一个表单
     removeMission(item){
        var index = this.StuForms.indexOf(item)
        if (index !== -1) {
         this.StuForms.splice(index,1);
       }
     },
     //新增信息
     addDomain(){
       this.StuForms.push({
         misname:"",
         misper:'',
         mispeo:'',
         miscon:'未完成',
         misend:'',
         misdetail:'',
       });
    }
  },
mounted() {
    //向后台发送axios信息获取登录信息进行表格填充
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
      //填充下拉列表
      this.peoptions.push(res.data.actor);
      var peolen=res.data.groPeo.length;
      for (i=0;i<peolen;i++){
        this.peoptions.push(res.data.groPeo[i]);
      }
      //this.peoptions.push(res.data.)
      var tem=[];
      var axios_stuforms=[];
      var len=res.data.TaskDetail.length;
      for (i = 0; i < len; i++)
       {
         tem.push({
           misname:res.data.TaskDetail[i].misname,
           mispeo:res.data.TaskDetail[i].mispeo,
           misper:res.data.TaskDetail[i].misper,
           miscon:res.data.TaskDetail[i].miscon,
           misend:res.data.TaskDetail[i].misend,
           misdetail:res.data.TaskDetail[i].misdetail
         })
         axios_stuforms.push({
           misname:res.data.TaskDetail[i].misname,
           mispeo:res.data.TaskDetail[i].mispeo,
           misper:res.data.TaskDetail[i].misper,
           miscon:res.data.TaskDetail[i].miscon,
           misend:res.data.TaskDetail[i].misend,
           misdetail:res.data.TaskDetail[i].misdetail
         })
      }
     this.StuForms=axios_stuforms;
     this.TaskDetail=tem;
     //对登录用户的身份进行处理
     let user=JSON.parse(sessionStorage.getItem('user'));
     let name=user.username;
     //console.log(this.$store.state.Sir==name)
      if(name==this.actor)  {this.editvisible=true;this.ifStu=true}
      if(name==this.$store.state.Sir){this.editvisible=false;this.ifSir=true}
    }.bind(this)
   ).catch(function(){
     console.log("出现错误");
   })
  }
}
</script>

<style>
body{margin:0;}
.head{text-align: center;}
.left{
    width: 35%;
    height: 100%;
    float: left;
  }
  .IP-line{
    height: 400px;
    float: left;
    margin-left: 30px;
    width: 5px;
    margin-top: 40px;
    border-left: 1px solid #cccccc;
  }
.right{
width: 60%;
height: 600px;
float: left;
}
.edit-button{

}
</style>
