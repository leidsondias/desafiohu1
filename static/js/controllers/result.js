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
        console.log('===ResultCtrl CTRL====');

        $scope.randomPrice = function(){
            return Math.floor((Math.random()*1000)+1);
        };

        $http.post(CONFIG.url_proxy+'/search', $location.search())
            .success(function(data) {
                //@TODO: Retorno sucesso
                $scope.hotels = data;
            })
            .error(function(data){
                //@TODO: Retorno falha
                console.info(data)
            });

    });
