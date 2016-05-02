'use strict';

/**
 * @ngdoc overview
 * @name desafioApp
 * @description
 * # Desafio proposto pelo Hotel Urbano mas sobre o projeto no link: https://github.com/leidsondias/desafiohu1
 *
 * Arquivo de inicialização do app
 */
angular
  .module('desafioApp', [
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ui.router',
  ])
  .config(function ($httpProvider, $routeProvider) {

    //
    // Interceptador
    // -------------------------------
    $httpProvider.interceptors.push('HttpInterceptor');

    //
    // Rotas da aplicação
    // -------------------------------
    $routeProvider
      .when('/', {
        templateUrl: 'views/search.html',
        controller: 'SearchCtrl',
        controllerAs: 'search'
      })
//      .when('/result', {
//        templateUrl: 'views/result.html',
//        controller: 'ResultCtrl',
//        controllerAs: 'result'
//      })
      .otherwise({
        redirectTo: '/'
      });

  });
