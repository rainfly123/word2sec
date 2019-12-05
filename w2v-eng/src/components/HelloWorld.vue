<template>
<div>
<div>
<el-row>
  <el-col :span="24"><div ><h2>
  英文语料推荐系统</h2></div></el-col>
  <p>
  <span style="color:gray"> —数据更新于:&nbsp;{{date}}—</span>
  </p>
</el-row>
<el-row>
<el-col :offset="6" :span="12">
  <div>
  <el-input  type="textarea"
  :rows="3" v-model="input" placeholder="请输入内容"></el-input>
  <br>
  <span class="demonstration">相似度阀值</span>
    <el-slider v-model="similarity"></el-slider>
  <el-button @click="query()" style="float:right;"type="primary">开始查询</el-button>
  </div>
 </el-col>
</el-row>
</div>

<div>
<el-row>
<el-col :offset="6" :span="12">
<el-card shadow="hover" v-for="(item, i) in items" :key="i" class="box-card">
  <div slot="header" class="clearfix">
    <span>语料编号:&nbsp;{{item.id}}</span>
    <span style="float:right;">推荐指数:&nbsp{{item.similarity}}</span>
  </div>
  <div class="text item">
    {{item.text}}
  </div>
</el-card>
</el-col>
</el-row>
</div>
<img v-if="btnFlag" class="go-top" src="https://cdncms.qctchina.top/topp.jpg" @click="backTop">
</div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
     items: [
            ], 
       input: '',
       similarity:50,
       date: '',
       btnFlag: false
    }
  },
 methods:{
    query(){console.log(this.input, this.similarity);
     var that = this
     var data = {
          similarity: this.similarity,
          text:this.input 
     }
 
    const qs = require('qs');
    this.axios.post('https://eval.qctchina.top/api/w2v_eng', qs.stringify(data)) 
    .then(function (response) {
         console.log(response.data);
         that.items.length = 0
           response.data.forEach(item=>{  //需要渲染的数组
              that.items.push(item)
                })
    })
    },


    backTop () {
      const that = this
      let timer = setInterval(() => {
        let ispeed = Math.floor(-that.scrollTop / 5)
        document.documentElement.scrollTop = document.body.scrollTop = that.scrollTop + ispeed
        if (that.scrollTop === 0) {
          clearInterval(timer)
        }
      }, 16)
  },
 
  // 为了计算距离顶部的高度，当高度大于60显示回顶部图标，小于60则隐藏
  scrollToTop () {
    const that = this
    let scrollTop = window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop
    that.scrollTop = scrollTop
    if (that.scrollTop > 60) {
      that.btnFlag = true
    } else {
      that.btnFlag = false
    }
  }

},
mounted () {
  window.addEventListener('scroll', this.scrollToTop)
  var date = new Date();
  date.setTime(date.getTime()-24*60*60*1000);
  this.date = date.getFullYear() + '-' + (date.getMonth() + 1) + '-' + date.getDate();
},
destroyed () {
  window.removeEventListener('scroll', this.scrollToTop)
},
 }
</script>
<style>
 .text {
    font-size: 14px;
  }

  .item {
    margin-bottom: 18px;
  }

  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }
  .clearfix:after {
    clear: both
  }

  .box-card {
  margin-top:50px;
  }
  .go-top{
 width: 3rem;height: 3rem;position: fixed;bottom: 20rem;right: 0.5rem;z-index: 99;
 }
</style>
