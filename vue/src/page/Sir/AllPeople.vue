<template>
    <div>

        <el-table
          :data="tableData"
          border
          style="margin-left: 200px; width: 58%; text-align:center">
	        <el-table-column
	          prop="name"
	          label="姓名"
	        >
	        </el-table-column>
	        <el-table-column
	            prop="doing"
	            label="当前任务数"
            >
	        </el-table-column>
	        <el-table-column
	          prop="done"
	          label="累计完成任务"
	          >
	        </el-table-column>
            <el-table-column label="操作">
                   <template scope="scope">
                      <el-button @click.native.prevent="test(scope.$index,tableData)" type="text" size="small"> 查看详情 </el-button>
                   </template>
            </el-table-column>
	    </el-table>

    </div>
</template>
<script>
import Axios from 'axios'
    export default {
        data(){
            return {
            	tableData: [
             		],
            	}
        	},
        methods:{
        	 test(index, rows){
                //alert(index);
                var key=rows[index].name;
        		//console.log(key);
                this.$store.state.username = rows[index].name;
                //this.$store.commit("showUserName");
        		this.$router.push({ path: 'MyTask/'+rows[index].name})
            }
        },
        mounted(){
            //Axios.get('./mock/all.json')
            Axios.get('http://39.108.181.155:8009/AllPeople')
            .then(function(res){
            //成功获取json数据信息的话
            var tem=[];
            var len=res.data.tableData.length;
            for (var i = 0; i < len; i++)
            {
                tem.push({
                        name:res.data.tableData[i].name,
                        doing:res.data.tableData[i].doing,
                        done:res.data.tableData[i].done
                })
            }
            this.tableData=tem;
        }.bind(this)
    ).catch(function(){
      console.log("出现错误");
    })
        }
    }
</script>
