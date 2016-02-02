var Backbone = require("backbone");
var _= require("underscore");

var ChannelModel = Backbone.Model.extend({
	urlRoot: function() {
		return window.Urls["channel-list"]();
	},
	defaults: {
		name: " ",
		editors: [],
		author: "Anonymous",
		license_owner: "No license found",
		description:" "
    },
    get_tree:function(tree_name){
    	var tree = new TopicTreeModel({id : this.get(tree_name)});
    	tree.fetch({async:false});
    	return tree;
    },

    update_root:function(data){
    	var channel = this;
    	$(["clipboard","deleted","draft"/*,"published"*/]).each(function(){
			var node = channel.get_tree(this.toString()).get_root();
			node.save(data);
		});
    },

    delete_channel:function(){
    	/* TODO: parallelize deleting*/
    	var channel = this;
    	var deleted_id = this.get_tree("deleted").id;
    	$(["clipboard","deleted","draft"/*,"published"*/]).each(function() {
		  	var tree = channel.get_tree(this);
		  	//channel.update_root({'parent' : deleted_id})
	    	tree.destroy();
	    	//TODO: Figure out how handling root nodes
	    	//var root = tree.get_root();
	    	//root.destroy();
		});
    	this.destroy();
    }
});

var ChannelCollection = Backbone.Collection.extend({
	model: ChannelModel,

	save: function() {
        Backbone.sync("update", this, {url: this.model.prototype.urlRoot()});
	},
	url: function() {
		return window.Urls["channel-list"]();
	},
	create_channel:function(data, timer){
		var channel_data = new ChannelModel(data);
		channel_data.fetch();
		if(channel_data.get("description").trim() == "")
			channel_data.set({description: "No description available."});
		var container = this;
		
		return this.create(channel_data, {
			async: false,
			success:function(){
				$(["draft","clipboard","deleted"/*,"published"*/]).each(function(){
					container.create_tree(channel_data, this.toString());
				});
   			}
		});
    },
    create_tree:function(channel, tree_name){
    	console.log(tree_name + " tree is being created...");
    	var root_node = new NodeModel();
		return root_node.save({title: channel.get("name")}, {
			async: false,
			success: function(){
				var tree = new TopicTreeModel();
				return tree.save({
					channel: channel.id, 
					root_node: root_node.id,
					name: channel.get("name"),
					kind:"topic"
				}, {
					async: false,
					success: function(){
						console.log(tree_name + " done.");
						return channel.save(tree_name, tree.id);
					}
				});
			}
		});
    }
});



module.exports = {
	NodeModel: NodeModel,
	NodeCollection: NodeCollection,
	TopicTreeModel:TopicTreeModel,
	TopicTreeModelCollection: TopicTreeModelCollection,
	ChannelModel: ChannelModel,
	ChannelCollection: ChannelCollection
}