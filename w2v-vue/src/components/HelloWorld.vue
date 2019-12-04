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

<el-row>
<el-col :offset="6" :span="12">
  <div>
  <p v-html="item"> </p>
  </div>
 </el-col>
</el-row>


</div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
     item: '<h1>$a_{1}>0 $</span>',
     msg: 'Welcome to Your Vue.js App',
       input: '',
       similarity:50
    }
  },
 methods:{
    query(){console.log(this.input, this.similarity)}
 }
}
</script>
<style>
</style>
