'use strict';

/**
 * @ngdoc function
 * @name desafioApp.directive:Pikdaday
 * @description
 * # Diretiva para ativar o pikaday.js <https://github.com/dbushell/Pikaday>
 * Directive of the desafioApp
 */
angular.module('desafioApp')
  .directive('random', function () {
    return {
 		restrict: 'A',
        link: function($scope, element, attrs) {
            var rand = Math.floor((Math.random()*attrs.random)+1);
            $(element).find('span').append(rand);
        }
    };
  });


