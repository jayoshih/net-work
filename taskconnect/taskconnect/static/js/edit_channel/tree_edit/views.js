var Backbone = require("backbone");
var _ = require("underscore");
require("content-container.less");
var BaseViews = require("./../views");
/*
var UploaderViews = require("edit_channel/uploader/views");
var PreviewerViews = require("edit_channel/previewer/views");
var ClipboardView = require("edit_channel/clipboard/views");
var DragHelper = require("edit_channel/utils/drag_drop");
*/
var Models = require("./../models");

var TreeEditView = BaseViews.BaseView.extend({
	/*container_index: 0,
	containers:[],
	content: [],
	template: require("./hbtemplates/container_area.handlebars"),
	topictrees: null,
	initialize: function(options) {
		_.bindAll(this, 'copy_content','delete_content' , 'add_container', 'edit_content', 'toggle_details');
		this.topictrees = options.topictrees;
		this.is_edit_page = options.edit;
		this.collection = options.collection;
		this.root = this.topictrees.get({id : window.current_channel.draft}).get_root();

		this.render();
		this.clipboard_view = new ClipboardView.ClipboardList({
	 		el: $("#clipboard-area"),
	 		topictrees: this.topictrees,
	 		collection: this.collection
	 	});
	 	console.log("channel",window.current_channel);
	},
	render: function() {
		this.$el.html(this.template({edit: this.is_edit_page}));
		this.add_container(this.containers.length, this.root);
	},
	events: {
		'click .copy_button' : 'copy_content',
		'click .delete_button' : 'delete_content',
		'click .edit_button' : 'edit_content',
		'click #hide_details_checkbox' :'toggle_details'
	},	
	add_container: function(index, topic){
		if(index < this.containers.length){
			while(this.containers.length > index){
				// TODO: Saving issues? 
				this.containers[this.containers.length-1].delete_view();
				this.containers.splice(this.containers.length-1);
			}
		}
		
		this.$el.find("#container_area").append("<li id='container_" + topic.id + "' class='container content-container "
						+ "pull-left' name='" + (this.containers.length + 1) + "'></li>");
		this.$el.find(".content-container").css("z-index", 10000);
		var container_view = new ContentList({
			el: this.$el.find("#container_area #container_" + topic.id),
			model: topic, 
			index: this.containers.length + 1,
			edit_mode: this.is_edit_page,
			collection: this.collection,
			containing_list_view : this,
			topictrees : this.topictrees
		});
		this.containers.push(container_view);
	},
	delete_content: function (event){
		if(confirm("Are you sure you want to delete the selected files?")){
			var list = this.$el.find('input:checked').parent("li");
			for(var i = 0; i < list.length; i++){
				$(list[i]).data("data").delete();
			}
		}
	},
	copy_content: function(event){
		var clipboard_root = this.topictrees.get({id : window.current_channel.clipboard}).get("root_node");
		var list = this.$el.find('input:checked').parent("li");
		var clipboard_list = new Models.NodeCollection();
		for(var i = 0; i < list.length; i++){
			var content = $(list[i]).data("data").model.duplicate(clipboard_root);
			content.fetch();
			clipboard_list.add(content);
		}
		this.clipboard_view.add_to_clipboard(clipboard_list);
	},	
	edit_content: function(event){
		var list = this.$el.find('input:checked').parent("li");
		var edit_collection = new Models.NodeCollection();
		for(var i = 0; i < list.length; i++){
			var model = $(list[i]).data("data").model;
			model.fetch();
			edit_collection.add(model);
		}
		$("#main-content-area").append("<div id='dialog'></div>");
		var metadata_view = new UploaderViews.EditMetadataView({
			collection: edit_collection,
			parent_view: this,
			el: $("#dialog"),
			allow_add : false,
			main_collection: this.collection,
		});
	},	
	toggle_details:function(event){
		this.$el.find("label").toggleClass("hidden_details");
	}*/
});

/* Open directory view */
/*
var ContentList = BaseViews.BaseListView.extend({
	item_view: "node",
	template: require("./hbtemplates/content_container.handlebars"),
	current_node : null,
	initialize: function(options) {
		_.bindAll(this, 'add_content');	
		this.index = options.index;
		this.edit_mode = options.edit_mode;
		this.containing_list_view = options.containing_list_view;
		this.collection = options.collection.get_all_fetch(this.model.attributes.children);
		this.topictrees = options.topictrees

		this.render();
		this.listenTo(this.collection, "sync", this.render);
        this.listenTo(this.collection, "remove", this.render);
		/* Set up animate sliding in from left */
		/*

		this.$el.animate({'margin-left' : "0px"}, 500);
		$("#container_area").find(".container-interior").css("z-index","0");		
	},
	render: function() {
		this.collection.sort_by_order();
		this.$el.html(this.template({
			topic: this.model, 
			edit_mode: this.edit_mode, 
			index: this.index,
			content_list: this.collection.toJSON(),
		}));

		this.load_content();
		this.$el.data("container", this);
		DragHelper.handleDrop(this, "move");
	},

	events: {
		'click .add_content_button':'add_content',
	},

	load_content : function(){
		var containing_list_view = this;
		var edit_mode = this.edit_mode;
		var el = containing_list_view.$el.find(".content-list");
		var index = 0;
		var current_node = this.current_node;

		this.collection.forEach(function(entry){
			entry.set({sort_order : index++});
			var file_view = new ContentItem({
				el: el.find("#" + entry.id),
				model: entry, 
				edit_mode: edit_mode,
				containing_list_view:containing_list_view,
				allow_edit: false
			});
			if(current_node && entry.id == current_node){
				file_view.set_opened(false);
			}
			containing_list_view.views.push(file_view);
		});
	},

	add_content: function(event){
		$("#main-content-area").append("<div id='dialog'></div>");
		var new_collection = new Models.NodeCollection();
		var add_view = new UploaderViews.AddContentView({
			el : $("#dialog"),
			collection: new_collection,
			main_collection: this.collection,
			parent_view: this,
			root: this.model
		});
	},

	add_container:function(view){
		this.current_node = view.model.id;
		this.containing_list_view.add_container(this.index, view.model);
	},

	close_folders:function(){
		this.$el.find(".folder").css({
			"width": "302px",
			"background-color": "white",
			"border" : "none"
		});

		this.views.forEach(function(entry){
			entry.$el.off("offset_changed");
			entry.$el.attr("draggable", "true");
		});

		this.$el.find(".folder .glyphicon").css("display", "inline-block");
	},

	add_to_container: function(transfer){
		console.log("transferring...",transfer.data);
		transfer.data.model.save({parent: this.model.id});
		transfer.data.containing_list_view.collection.remove(transfer.data.model);
		this.collection.add(transfer.data.model);
	}
});*/

module.exports = {
	TreeEditView: TreeEditView,
}