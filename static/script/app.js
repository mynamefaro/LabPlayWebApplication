Vue.component('a-button', {
	template: '<a class="a_button"><slot></slot></a>'
});
Vue.component('a-link', {
	template: '<a><h1><slot></slot></h1></a>'
});
Vue.component('level-left', {
	template: '<div class="level is-left"><slot></slot></div>'
});
Vue.component('level-right', {
	template: '<div class="level is-right"><slot></slot></div>'
});
Vue.component('h-title',{
	template: '<h1 class="title"><slot></slot></h1>'
});
Vue.component('page', {
	template: '<div class="page"><slot></slot></div>'
});
Vue.component('container', {
	template: '<div class="container"><slot></slot></div>'
});
Vue.component('navbar', {
	template: '<div class="navbar"><slot></slot></div>'
});
Vue.component('navdown', {
	template: '<div><slot></slot></div>'
});
Vue.component('search', {
	template: `<form class="search" action="." method="get">
					<button type="submit"><span></span></button>
					<input type="textbox" placeholder="ค้นหา" name="search"/>
			    </form>`
});
Vue.component('banner', {
	template: '<div class="banner"></div>'
});
Vue.component('navigation', {
	template: '<div class="navigation"><slot></slot></div>'
});
Vue.component('mini-button', {
	template: '<a><div class="mini-button"><slot></slot></div></a>'
});
Vue.component('box-list', {
	props:['img','name','like','type','play','creator'],
	template: `<a>
			<container class="box-list">
				<figure>
					<label>{{type}}</label>
					<img :src="img"/>
				</figure>
				<div>
					<h3>{{name}}</h3>
				</div>
			</container>
		</a>`
});
Vue.component('dropdown', {
	template: `
		<div class="dropdonw"><slot></slot></div>
		`
});
Vue.component('full-button',{
	template : '<a><button class="a_button is-full"><slot></slot></button></a>'
});
Vue.component('modal',{
	template : '<div class="modal"><slot></slot></div>'
})
/*MAIN*/

new Vue({ 
	delimiters: ['[', ']'],
	el: '#app',
	data:{
		/*NAVBAR */
		navbars:[
			{
				name:"Home",
				href:"{% url 'index' %}"
			},
			{
				name:"Games",
				href:"{% url 'games' %}"
			},
			{
				name:"LabplayEditor",
				href:"LabPlayEditor"
			},
			{
				name:"Contact",
				href:"contact"
			}
		],
		navdown:false,
		modal:false,
		pic:"/static/pic/5.jpg"
	},
	methods:{
		drop : function(){
			this.navdown=!this.navdown;
		},
		showmodal(){
			this.modal = true;
		}
	}
});