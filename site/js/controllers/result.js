'use strict';

/**
 * @ngdoc function
 * @name desafioApp.controller:ResultCtrl
 * @description
 * # Controlador responsável pelo resultado da busca da aplicação
 * Controller of the desafioApp
 */
angular.module('desafioApp')
    .controller('ResultCtrl', function ($scope, $http, $location, CONFIG) {

        $scope.page = 1;

        $scope.getPagination = function(total){
            return Math.ceil(total/5);
        };

        $scope.loadData = function(is_append){
            $http.post(CONFIG.url_proxy+'/search', $location.search())
            .success(function(data) {
               if(is_append){
                    $scope.hotels = $scope.hotels.concat(data.results);
               }else{
                    $scope.hotels = data.results;
                    $scope.pages = $scope.getPagination(data.total);
               }
            })
            .error(function(data){
                //@TODO: Retorno falha
                console.info(data)
            });
        };

        $scope.loadData();

        $scope.loadMore = function(page){
            var offset = 5*$scope.page;
            $scope.page += 1;
            $location.search().offset = offset;
            $scope.loadData(true);
        };

    });
