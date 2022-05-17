let mix = require('laravel-mix');

mix.js('resources/js/app.js', 'static/app').vue()
    .postCss('resources/css/app.css', 'static/app', [
        require('postcss-import'),
        require('tailwindcss'),
    ]);