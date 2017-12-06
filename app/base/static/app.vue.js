var Text = {
	 props: ['todo'],
	  template: '<div class="form-group">\
	  		<label class="control-label col-sm-2"> {{ todo.riskField }} \
			</label>\
			<div class="col-sm-10">\
  				<input type="text" class="form-control" id="email" placeholder="" :name="todo.type.fieldType"> \
  				 \
			</div>\
  		   </div>'
	}    

var Number = {
	 props: ['todo'],
	template: '<div class="form-group">\
	  		<label class="control-label col-sm-2">{{ todo.riskField }}\
		</label>\
		<div class="col-sm-10">\
			<input type="number" class="form-control" id="email" placeholder="" :name="todo.type.fieldType"> \
		</div>\
	   </div>'
	} 

var Date = {
  	  props: ['todo'],
 		template: '<div class="form-group">\
	  		<label class="control-label col-sm-2">{% raw %} {{ todo.riskField }} {% endraw %}\
			</label>\
			<div class="col-sm-10">\
  				<input type="date" class="form-control" id="email" placeholder="" :name="todo.type.fieldType"> \
			</div>\
  		   </div>'
} 

var Enum = {
  		 props: ['todo'],
  		template: '<div class="form-group">\
	  		<label class="control-label col-sm-2">{% raw %} {{ todo.riskField }} {% endraw %}\
			</label>\
			<div class="col-sm-10">\
  				<input type="range" class="form-control" id="email" placeholder="" :name="todo.type.fieldType"> \
			</div>\
  		   </div>'
	}
	var app7 = new Vue({
	  el: '#app-7',
	  data: {
		currentView: 'do-item',
		
		todos: []
	  },
	components: {
	    // <my-component> will only be available in parent's template
	    'text-item': Text,
	    'number-item': Number,
	    'date-item': Date,
	    'enum-item': Enum,    	    
	  },
	  methods: {
		  theValue: function (id) {
		    var value = id + '-item'
		    return value
		  }
		},
	 mounted(){
			axios.get('/base/risktype/all/').then(response => this.todos = response.data);
		}
	});