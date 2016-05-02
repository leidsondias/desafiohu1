'use strict';

/**
 * @ngdoc function
 * @name desafioApp.controller:SearchCtrl
 * @description
 * # Controlador responsável pela busca da aplicação
 * Controller of the desafioApp
 */
angular.module('desafioApp')
    .controller('SearchCtrl', function ($scope, $http, $location, CONFIG, Scopes) {
        console.log('===SearchCtrl CTRL====');

        var auto_complete_list = angular.element('.auto-complete');

        $scope.autoComplete = function(){
            if($scope.search.local.length > 3){
                $http.get(CONFIG.url_proxy+'/list', {params: {"query": $scope.search.local}})
                    .success(function(data) {
                        //@TODO: Retorno sucesso
                        auto_complete_list.css("display", "block");

                        if(data.length !== 0){
                            $scope.autoCompleteList = data
                        }else{
                            $scope.autoCompleteList = [{"name": "Nenhum resultado para esta pesquisa."}]
                        }
                    })
                    .error(function(data){
                        //@TODO: Retorno falha
                        console.info(data)
                    });
            }else{
                auto_complete_list.css("display", "none");
            }

        };

        $scope.doSearch = function(){
            var params = {"kind": $scope.search.localObj.kind, "id": $scope.search.localObj.id,
                        "start_date": $scope.search.start_date, "end_date": $scope.search.end_date}
            $http.post(CONFIG.url_proxy+'/search', params)
                .success(function(data) {
                    //@TODO: Retorno sucesso
                    Scopes.store('result_search', data);
                    $location.path('/result');
                })
                .error(function(data){
                    //@TODO: Retorno falha
                    console.info(data)
                });
        };

        $scope.setLocal = function(item){
            $scope.search.local = item.name;
            $scope.search.localObj = item;
            auto_complete_list.css("display", "none");
        };

    });
