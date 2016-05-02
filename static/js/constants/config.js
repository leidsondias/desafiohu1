'use strict';

/**
 * @ngdoc function
 * @name desafioApp.constant:CONFIG
 * @description
 * # CONFIG
 * constant of the desafioApp for config
 */
angular.module('desafioApp')
  .constant('CONFIG', {
    "url": "http://localhost:5000",
    "url_proxy": "http://localhost:1337/localhost:5000"
  });