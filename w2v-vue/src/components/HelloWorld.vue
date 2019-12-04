<template>
<div style="margin-top:50px">
<el-row>
  <el-col :span="24"><div ><h2>
  试题查重系统</h2></div></el-col>
</el-row>
<el-row>
<el-col :offset="6" :span="12">
  <div>
  <br>
  <el-input  type="textarea"
  :rows="3" v-model="input" placeholder="请输入内容"></el-input>
  <br>
  <span class="demonstration">相似度阀值</span>
    <el-slider v-model="similarity"></el-slider>
  <br>
  <el-button @click="query()" style="float:right;"type="primary">开始查询</el-button>
  </div>
 </el-col>
</el-row>

<el-row>
<el-col :offset="6" :span="12">
<el-divider></el-divider>
</el-col>
</el-row>

<el-row v-for="(item,i) in items" :key="i">
<el-col :offset="6" :span="12">
  <div>
  <p> 题目序号: &nbsp;{{item.id}}</p>
  <p> 相似度: &nbsp; {{item.similarity}}</p>
  <p v-html="item.text"> </p>
  </div>
<el-divider></el-divider>
 </el-col>
</el-row>


</div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
     items: [
{id:1,similarity:30,text:'<h1>$a_{1}>0 $</span>'} 
            ], 
     msg: 'Welcome to Your Vue.js App',
       input: '',
       similarity:50
    }
  },
 methods:{
    query(){console.log(this.input, this.similarity);
  	var that = this
     var data = {
          similarity: 60,
          text: '函数我不知道'
     }
    this.items.push({id:1,similarity:30,text:'<h1>$a_{1}>0 $</span>'} )
    /*
    const qs = require('qs');
    this.axios.post('https://eval.qctchina.top/api/w2v', qs.stringify(data)) 
    .then(function (response) {
         console.log(response.data);
         let arr = []//新数组
           response.data.forEach(item=>{  //需要渲染的数组
            //执行你的操作，最后用放到arr中
            arr.push(item)
                })
        that.items = arr //
    })
    .catch(function (error) {
    console.log(error);
    });
    */
    }
 }
}
</script>
<style>
</style>
