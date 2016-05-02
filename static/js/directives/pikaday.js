'use strict';

/**
 * @ngdoc function
 * @name desafioApp.directive:Pikdaday
 * @description
 * # Diretiva para ativar o pikaday.js
 * Directive of the desafioApp
 */
angular.module('desafioApp')
  .directive('pikaday', function () {
    return {
 		restrict: 'A',
 		scope: true,
		link: function(scope, element, attrs){
            new Pikaday({
                field: document.getElementById(attrs.id),
            });
		}
    };
  });