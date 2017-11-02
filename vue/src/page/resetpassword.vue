<template>
  <div>
    <Header></Header>
    <div id="form">
      <h3>修改密码</h3>
      <br/><br/>
     <el-form :model="reset" :rules="rules" ref="reset" label-width="100px" class="demo-ruleForm" >
       <el-form-item prop="name"  required>
         <el-input placeholder="请输入用户名"  v-model="reset.name"></el-input>
       </el-form-item>
       <el-form-item prop="old_pass">
         <el-input placeholder="请输入原始密码" type="password" v-model="reset.old_pass"></el-input>
       </el-form-item>
       <el-form-item  prop="new_pass">
         <el-input placeholder="请输入新密码" type="password"  v-model="reset.new_pass"></el-input>
       </el-form-item>
       <el-form-item  prop="confirm_pass" style="width:500px" >
         <el-input placeholder="请再次输入密码"type="password"  v-model="reset.confirm_pass"></el-input>
       </el-form-item>

       <el-form-item  style="margin-left:150px">
 	    		<el-button type="primary" @click="submitForm('reset')">提交</el-button>
 	   			<el-button @click="resetForm('reset')">重置</el-button>

 	  	</el-form-item>
     </el-form>
  </div>
  </div>
</template>

<script>
import Header from '@/components/header.vue'
import Axios from 'axios';
export default{
  components: {Header},
  data(){
    {
      return{
        reset:{
           name:'',
           old_pass:'',
           new_pass:'',
           confirm_pass:''
        },
        rules: {
          name: { required: true, message: '请输入用户名', trigger: 'blur' },
          old_pass:{required:true,message:"请输入原密码",trigger:'blur'},
          new_pass:{required:true,message:"请输入新密码",trigger:'blur'},
          confirm_pass:{required:true,message:"请再次输入密码",trigger:'blur'},
        }
      }
    }
  },
  methods: {
    resetForm(formName) {
      this.$refs[formName].resetFields();
    },
    submitForm(formName)
    {  this.$refs[formName].validate((valid) =>
       {  if (valid)
         {
             var mydata={"name":this.reset.name,"old_pass":this.reset.old_pass,"new_pass":this.reset.new_pass};
             console.log(mydata);
             //前端验证，新密码输入两次的结果要一样，但是不同于之前的初始密码
             if(this.reset.new_pass==this.reset.confirm_pass && this.reset.new_pass!=this.reset.old_pass){
                Axios.post('/api/resetPassword',mydata)
                //Axios.get('./mock/new.json')
                .then(function(res)
                {
                  if(res.data.info=="success")
                       alert('修改成功');
                  else
                      alert('不允许修改!');
                })
               .catch(function()
                {
                    console.log('error submit!!');
                })
             }
             else if (this.reset.new_pass!=this.reset.confirm_pass) {
               console.log("请确认密码");
             }
             else console.log("未作出修改");
          }
          else
          {console.log('error submit!!');
           return false;
         }
      });
    }
  }
}
</script>

<style>
#form{
  text-align:center;
  color:rgb(65,105,225);
  position:fixed;
    top:20%;
    right:35%;
    background:rgba(220,220,220,0.4);
    -webkit-box-shadow: 10px 10px 5px 0px rgba(0,0,0,0.75);
    -moz-box-shadow: 10px 10px 5px 0px rgba(0,0,0,0.75);
    box-shadow: 10px 10px 5px 0px rgba(0,0,0,0.75);
}
#form .el-input{
  position: relative;
  right:10%;
}
</style>
