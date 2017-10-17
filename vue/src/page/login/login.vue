<template>
  <div class="body">
    <h1>实验室管理系统</h1>
    <div class="container w3">
        <h2>现在登录</h2>
        <el-form :model="ruleForm2" :rules="rules2" ref="ruleForm2" label-position="left" label-width="0px"
        class="demo-ruleForm login-container">
           <div class="username">
           <el-form-item prop="account">
             <el-input type="text" v-model="ruleForm2.account" auto-complete="off"  placeholder="账号"></el-input>
           </el-form-item>
           </div>
           <div class="password-agileits">
           <el-form-item prop="checkPass">
                 <el-input type="password" v-model="ruleForm2.checkPass" auto-complete="off" placeholder="密码"></el-input>
             </el-form-item>
           </div>
           <el-checkbox v-model="checked" checked class="remember" style=" color: #FFF;">记住密码</el-checkbox>
           <el-form-item style="width:100% ">
                  <el-button type="primary" style="width:50%;margin-top: 30px;" @click="handleSubmit2" :loading="logining">登录</el-button>
           </el-form-item>
        </el-form>

  </div>
  <div class="footer-w3l">
        <p> 实验室管理系统</p>
  </div>
</div>
</template>
<script type="application/x-javascript"> addEventListener("load", function() { setTimeout(hideURLbar, 0); }, false); function hideURLbar(){ window.scrollTo(0,1); } </script>
<script>
import Axios from 'axios'
export default{
  data() {
         return {
             logining: false,
             ruleForm2: {
                 account: '',
                 checkPass: '123456'
             },
             rules2: {
                 account: [{
                         required: true,
                         message: '请输入账号',
                         trigger: 'blur'
                     },
                     //{ validator: validaePass }
                 ],
                 checkPass: [{
                         required: true,
                         message: '请输入密码',
                         trigger: 'blur'
                     },
                     //{ validator: validaePass2 }
                 ]
             },
             checked: true
         };
     },
     methods: {
         handleSubmit2(ev) {
             var _this = this;
             _this.$refs.ruleForm2.validate((valid) => {
                 if (valid) {
                     _this.logining = true;
                     var loginParams = {
                         username: this.ruleForm2.account,
                         password: this.ruleForm2.checkPass
                     };
                     //表单验证通过axios验证方法实现(这里需要改一下)
                    // if (loginParams.username == "admin" && loginParams.password == "123456")
                //   Axios.get('/api/login?name='+loginParams.username+'&pass='+loginParams.password).
                     Axios.get('./mock/login.json').
                   then(function(res){
                      // console.log(res.data.status);
                       if(res.data.status==1)
                        {
                          _this.logining = false;
                         sessionStorage.setItem('user', JSON.stringify(loginParams));
                         _this.$router.push({ path: '/Sir/AllTask' });
                        }
                       else if (res.data.status==2) {
                         _this.logining = false;
                         sessionStorage.setItem('user', JSON.stringify(loginParams));
                         _this.$router.push({ path: '/stu' });
                       }
                      else {
                          _this.logining = false;
                          _this.$alert('用户名或密码错误！', '提示信息', {
                              confirmButtonText: '确定'
                              });
                          }
                    }).catch(function(){
                      console.log("出现错误");
                    })
                   }
                 else {
                     console.log('error submit!!');
                     return false;
                 }
             });
         }
     }
 }
</script>

<style scoped>
    /* start editing from here */
    a{text-decoration:none;}
    .txt-rt{text-align:right;}/* text align right */
    .txt-lt{text-align:left;}/* text align left */
    .txt-center{text-align:center;}/* text align center */
    .float-rt{float:right;}/* float right */
    .float-lt{float:left;}/* float left */
    .clear{clear:both;}/* clear float */
    .pos-relative{position:relative;}/* Position Relative */
    .pos-absolute{position:absolute;}/* Position Absolute */
    .vertical-base{vertical-align:baseline;}/* vertical align baseline */
    .vertical-top{vertical-align:top;}/* vertical align top */
    nav.vertical ul li{display:block;}/* vertical menu */
    nav.horizontal ul li{display: inline-block;}/* horizontal menu */
    img{max-width:100%;}
/*-- //Reset-Code --*/
.body {
    background:url('../../images/2.jpg') repeat 0px 0px;
    height: 100%;
    background-size: cover;
    font-family: 'Open Sans', sans-serif;
    background-attachment: fixed;
    background-position: center;
}

h1 {
    color: #FFF;
    text-align: center;
    letter-spacing: 6px;
    font-size: 40px;
    margin-top: 1px;
    padding-top: 45px;
}

.container {
    width: 32%;
    margin: 3px auto;
    text-align: center;
    background:rgba(0, 0, 0, 0.43);
    -webkit-box-shadow: 10px 10px 5px 0px rgba(0,0,0,0.75);
    -moz-box-shadow: 10px 10px 5px 0px rgba(0,0,0,0.75);
    box-shadow: 10px 10px 5px 0px rgba(0,0,0,0.75);
}

h2 {
    font-size:  30px;
    color: #FFF;
    padding-top: 45px;
    letter-spacing:3px;
}
form {
    padding-top: 5px;
    padding-right:65px;
    padding-left: 65px;
    padding-bottom: 65px;

}

form span {
    width: 23%;
    float: left;
    background: #fed14e;
    padding: 10.2px 10px;
    position: relative;
    color: #005377;
    font-size: 15px;
    letter-spacing: 1px;
}

form span:after {
    content: '';
    position: absolute;
    width: 0;
    height: 0;
    right: -11px;
    border-top: 6px solid rgba(0, 0, 0, 0);
    border-left: 11px solid #fed14e;
    border-bottom: 6px solid rgba(0, 0, 0, 0);
    top: 14px;
}
input.user {
    width: 65%;
    padding:10px 10px 10px 15px;
    border: none;
    outline: none;
    font-size: 17px;
    letter-spacing: 1px;
    margin-bottom: 35px;
    float:left;
}

input.password {
    width: 65%;
    padding:10px 10px 10px 15px;
    border: none;
    outline: none;
    font-size: 17px;
    letter-spacing: 1px;
    margin-bottom: 35px;
    float:left;
}
.rem-for-agile{
    width:50%;
    float:left;
    text-align:left;
    font-size:13px;
    color:rgb(238, 223, 179);
}
.rem-for-agile a{
    color:rgb(238, 223, 179);
    margin-top:3px;
    display:inline-block;
    padding-left:18px;
}
.rem-for-agile a:hover{
    color: #fff;
}
input[type="checkbox"] {
    margin: 10px 5px 0px 0px;
    vertical-align: sub;
}

.login-w3{
    width:50%;
    float:right;
}
input[type="submit"]{
    background-color:#005377;
    color:#fff;
    padding:11px;
    outline: none;
    border:none;
    font-size: 17px;
    width:50%;
    cursor:pointer;
    margin-top:5px;
        transition: 0.5s all;
    -webkit-transition: 0.5s all;
    -moz-transition: 0.5s all;
    -o-transition: 0.5s all;
    -ms-transition: 0.5s all;
}
input[type="submit"]:hover{
    background:#fed14e;
    color:#000;

}
.footer-w3l{
    margin-top: 150px;
    margin-bottom: 20px;
}
.footer-w3l p {
    color:white;
    text-align:center;
    margin-top: 10px;
    font-size:13px;
    letter-spacing:1px;
}
.footer-w3l a{
    color:white;
    text-decoration:none;
}
.footer-w3l a:hover{
    text-decoration:underline;
}
@media screen and (max-width: 1440px) {
    form span {
        font-size:14px;
        padding:10.5px 10px;
    }
    input.user{
        width: 63%;
    }
    input.password {
        width: 63%;
    }

}
@media screen and (max-width: 1366px) {
    .container {
        width: 37%;
    }

}

@media screen and (max-width: 1080px) {
    .container {
        width: 46%;
    }


}
@media screen and (max-width: 991px) {
    h1{
        margin-top:50px;
    }
    .container {
        width: 52%;
    }

}


@media screen and (max-width: 800px) {
    .container {
        width: 63%;
    }
    form {
        padding: 55px;
    }

}

@media screen and (max-width: 736px) {
    h1 {
        letter-spacing: 4px;
        font-size: 35px;
    }
    h2 {
        font-size: 28px;
        padding-top: 35px;
        letter-spacing: 2px;
    }

}
@media screen and (max-width: 667px) {
    .container {
        width: 66%;
    }
    form {
        padding: 53px;
    }

}
@media screen and (max-width: 640px) {
    form {
        padding: 42px;
    }
}
@media screen and (max-width: 600px) {
    .container {
        width: 70%;
    }
}
@media screen and (max-width: 568px) {
    .container {
        width: 74%;
    }
}
@media screen and (max-width: 480px) {
    h1 {
        letter-spacing: 2px;
        font-size: 31px;
    }
    .container {
        width: 78%;
    }
    form {
        padding: 30px;
    }
    input.user {
        width: 62%;
    }
    input.password{
        width: 62%;
    }
    input[type="submit"] {
        margin-top:8px;
    }
}
@media screen and (max-width: 414px) {
    .container {
        width: 85%;
    }
    form span {
        font-size: 12px;
    }
    input.user {
        width: 58.5%;
        padding: 9px 9px 9px 15px;
    }
    input.password{
        width: 58.5%;
        padding: 9px 9px 9px 15px;
    }
    .footer-w3l p {
        letter-spacing:0;
    }
}

@media screen and (max-width: 384px) {
    form span {
        width: 25%;
    }
    input.user {
        width: 57.5%;
    }
    input.password{
        width: 57.5%;
    }
}

@media screen and (max-width: 375px) {
    h1 {
        font-size: 27px;
    }
    h2 {
        font-size: 24px;
    }
    input.user {
        width: 57%;
    }
    input.password{
        width: 57%;
    }
    form span{
        padding-left:5px;
    }

}
@media screen and (max-width: 320px) {
    h1 {
        font-size: 23px;
        letter-spacing:1px;
    }
    h2 {
        font-size: 19px;
        letter-spacing:1px;
        padding-top:25px;
    }
    form {
        padding: 20px;
    }
    form span {
        font-size: 11px;
        width:27%;
    }
    input.user {
        padding: 8px 9px 8px 15px;
        width:55%;
    }
    input.password {
        padding: 8px 9px 8px 15px;
        width:55%;
    }
    .rem-for-agile{
        font-size:11px;
    }
    input[type="submit"] {
        padding: 9px;
        font-size: 16px;
        width: 60%;
        margin-top:10px;
    }
}

</style>
