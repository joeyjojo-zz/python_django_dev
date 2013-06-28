//= require libs/jquery-1.10.1
//= require libs/handlebars-1.0.0-rc.4
//= require libs/ember-1.0.0-rc.6

App = Ember.Application.create();

App.Router.map(function() {
  // put your routes here
});

App.IndexRoute = Ember.Route.extend({
    model: function() {
        return ['red', 'yellow', 'blue'];
    }
});