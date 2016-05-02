'use strict';

/**
 * @ngdoc function
 * @name desafioApp.controller:SearchCtrl
 * @description
 * # Controlador responsável pela busca da aplicação
 * Controller of the desafioApp
 */
angular.module('desafioApp')
    .controller('SearchCtrl', function ($scope, $http) {
        console.log('===SearchCtrl CTRL====');

        $scope.doSearch = function(){
            console.log('===DO SEARCH====', $scope);
        };

        $scope.autoComplete = function(){
            console.log($scope.search.local)
        };




    });
