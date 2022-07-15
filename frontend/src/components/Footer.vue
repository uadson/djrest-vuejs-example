<template>
  <footer id="footer">
    <p>Make Your Burger &copy; 2022 - Made with Django Rest and Vue Js | <a href="https://github.com/uadson/djrest-vuejs-example" target="_blank">Backend</a> made by Uadson Feitosa |
Original Frontend Project <a href="https://github.com/matheusbattisti/curso_vue_yt/tree/main/18_projeto" target="_blank">here</a></p>
  </footer>
</template>

<script>
export default {
    name: 'Footer'
}
</script>

<style scoped>
 #footer {
  height: 200px;
  background-color: #222;
  border-top: 4px solid #111;
  color: #FCBA03;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
 }

 a {
  color: #FCBA03;
 }

 a:hover{
  color: #fff;
  transition: .5s;
 }
</style>