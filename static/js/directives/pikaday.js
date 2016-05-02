'use strict';

/**
 * @ngdoc function
 * @name desafioApp.directive:Pikdaday
 * @description
 * # Diretiva para ativar o pikaday.js <https://github.com/dbushell/Pikaday>
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
                format: 'YYYY-MM-DD',
            });
		}
    };
  });