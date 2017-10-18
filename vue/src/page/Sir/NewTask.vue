<template>
    <div>
        <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm" style="margin-left:150px;">
  			<el-form-item label="任务名称" prop="name" style="width: 500px;">
    			<el-input v-model="ruleForm.name"></el-input>
  			</el-form-item>
			<el-form-item label="任务时间" required>
			    <el-col :span="7">
				    <el-form-item prop="date1">
				    	<el-date-picker type="date" placeholder="开始日期" v-model="ruleForm.date1"  style="width: 100%;" @change="dateChange1"></el-date-picker>
				    </el-form-item>
			    </el-col>
			    <el-col class="line" :span="1">---</el-col>
			    <el-col :span="7">
			      	<el-form-item prop="date2">
			        	<el-date-picker type="date" placeholder="截止日期" v-model="ruleForm.date2" style="width: 100%;" @change="dateChange2"></el-date-picker>
			      	</el-form-item>
			    </el-col>
			</el-form-item>
      <el-form-item label="组长" prop="leader" style="width: 500px;">
          <el-select v-model="ruleForm.leader" placeholder="请选择组长">
            <el-option
              v-for="item in options"
              :key="item.label"
              :label="item.label"
              :value="item.label">
            </el-option>
          </el-select>
      </el-form-item>
			<el-form-item  label="成员" prop="member" >
    			<el-select v-model="ruleForm.member" style="width: 400px;" multiple placeholder="请选择组员">
            <el-option
              v-for="item in options"
              :key="item.label"
              :label="item.label"
              :value="item.label">
            </el-option>
      </el-select>
  		</el-form-item>

  		<el-form-item label="目标百分比" prop="goal" style="width: 500px;">
    			<el-input v-model="ruleForm.goal"></el-input>
  		</el-form-item>
	  	<el-form-item label="需求描述" prop="desc" style="width: 500px;">
	    		<el-input type="textarea" v-model="ruleForm.desc" ></el-input>
	  	</el-form-item>
	  	<el-form-item style="margin-left: 120px;">
	    		<el-button type="primary" @click="submitForm('ruleForm')">提交</el-button>
	   			<el-button @click="resetForm('ruleForm')">重置</el-button>
	  		</el-form-item>
		</el-form>
    </div>
</template>
<script>
import Axios from 'axios';
import Moment from 'moment'
    export default {
    data() {
      return {
        ruleForm: {
          name: '',
          date1: '',
          date2: '',
          leader:'',
          member:'',
          goal: '',
          desc: ''
        },
        options: [{
          value: '选项1',
          label: '陈飞坤'
        }, {
          value: '选项2',
          label: '姜金霖'
        }, {
          value: '选项3',
          label: '江宇川'
        }, {
          value: '选项4',
          label: '兰子柠'
        }, {
          value: '选项5',
          label: '彭一'
        }, {
          value: '选项6',
          label: '王心雨'
        },{
          value: '选项7',
          label: '吴炜锋'
        },{
          value: '选项8',
          label: '周桐'
        }
        ],
        rules: {
          name: [
            { required: true, message: '请输入任务名称', trigger: 'blur' },
            { min: 3, max: 10, message: '长度在 3 到 10 个字符', trigger: 'blur' }
          ],

          date1: [
            { type: 'date', required: true, message: '请选择开始日期', trigger: 'change' }
          ],
          date2: [
            { type: 'date', required: true, message: '请选择截止日期', trigger: 'change' }
          ],
          goal: [
            { required: true, message: '请填写目标百分比', trigger: 'blur' }
          ],
          desc: [
            { required: true, message: '请填写需求描述', trigger: 'blur' }
          ]
        }
      };
    },
    methods: {
      dateChange1(val) {
        this.date1=val;

        console.log(this.date1);
        return(this.date1);
      },
      dateChange2(val) {
        this.date2=val;

        console.log(this.date2);
        return(this.date2);
      },
      submitForm(formName) {

        var _this = this;
        this.$refs[formName].validate((valid) => {
          if (valid) {
          var mydata={"name":this.ruleForm.name,"date1":this.date1,"date2":this.date2,"leader":this.ruleForm.leader,"member":this.ruleForm.member,"goal":this.ruleForm.goal,"desc":this.ruleForm.desc};
          console.log(mydata.member);
          Axios.post('/api/NewTask',{mydata})
          //Axios.get('./mock/new.json')
                   .then(function(res){
                    if(res.data.result=="success")
                        {
                          alert('submit!');
                        }
                    else{
                      alert('fail!');
                    }
                   }).catch(function(){
                      console.log("出现错误");
                    })

          } else {
            console.log('error submit!!');
            return false;
          }
        });

        },
      resetForm(formName){
        this.$refs[formName].resetFields();
      }
    }
  }
</script>
