'use strict';

/**
 * @ngdoc function
 * @name desafioApp.controller:ResultCtrl
 * @description
 * # Controlador responsável pelo resultado da busca da aplicação
 * Controller of the desafioApp
 */
angular.module('desafioApp')
    .controller('ResultCtrl', function ($scope, $http, CONFIG, Scopes) {
        var teste = [{
                "available": true,
                "date": "2015-05-30",
                "hotel": {
                  "city_id": 2,
                  "id": 2,
                  "name": "Boulevard Higienopolis Residence Hotel"
                },
                "id": 60
              },
              {
                "available": true,
                "date": "2015-05-30",
                "hotel": {
                  "city_id": 2,
                  "id": 47,
                  "name": "Hotel Schloss Lebenberg"
                },
                "id": 1410
              },
              {
                "available": true,
                "date": "2015-05-30",
                "hotel": {
                  "city_id": 2,
                  "id": 68,
                  "name": "Rainhof"
                },
                "id": 2040
              }];

        $scope.results = Scopes.get('result_search') || teste;
        console.log('===ResultCtrl CTRL====');

    });
