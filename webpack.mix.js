let mix = require('laravel-mix');

/*
 |--------------------------------------------------------------------------
 | Mix Asset Management
 |--------------------------------------------------------------------------
 |
 | Mix provides a clean, fluent API for defining some Webpack build steps
 | for your Masonite application. By default, we are compiling the Sass
 | file for your application, as well as bundling up your JS files.
 |
 */

mix.js('storage/static/js/app.js', 'storage/compiled/js')
    .sass('storage/static/sass/style.scss', 'storage/compiled/css');

mix.js('storage/static/assets/js/bundle.js', 'storage/compiled/packages/backpack/base/js/');
mix.sass('storage/static/assets/scss/bundle.scss', 'storage/compiled/packages/backpack/base/css/')
	.options({
      processCssUrls: false
    });

// copy the Backstrap CSS
mix.copy('node_modules/@digitallyhappy/backstrap/dist/css', 'storage/compiled/packages/@digitallyhappy/backstrap/css');

// copy fonts and other assets
mix.copy('node_modules/line-awesome/dist/line-awesome', 'storage/compiled/packages/line-awesome')
	.copy('node_modules/source-sans-pro', 'storage/compiled/packages/source-sans-pro')
	.copy('node_modules/animate.css/animate.min.css', 'storage/compiled/packages/animate.css/animate.min.css')
	.copy('node_modules/noty/lib', 'storage/compiled/packages/noty');


// copy CRUD filters JS into packages
mix.copy('node_modules/bootstrap-datepicker/dist', 'storage/compiled/packages/bootstrap-datepicker/dist')
	.copy('node_modules/moment/min', 'storage/compiled/packages/moment/min')
	.copy('node_modules/select2/dist', 'storage/compiled/packages/select2/dist')
	.copy('node_modules/jquery-colorbox', 'storage/compiled/packages/jquery-colorbox')
	.copy('node_modules/jquery-ui-dist', 'storage/compiled/packages/jquery-ui-dist')
	.copy('node_modules/select2-bootstrap-theme/dist', 'storage/compiled/packages/select2-bootstrap-theme/dist')
	.copy('node_modules/bootstrap-daterangepicker/daterangepicker.css', 'storage/compiled/packages/bootstrap-daterangepicker/daterangepicker.css')
	.copy('node_modules/bootstrap-daterangepicker/daterangepicker.js', 'storage/compiled/packages/bootstrap-daterangepicker/daterangepicker.js')
	.copy('node_modules/pc-bootstrap4-datetimepicker/build', 'storage/compiled/packages/pc-bootstrap4-datetimepicker/build')
	.copy('node_modules/cropperjs/dist', 'storage/compiled/packages/cropperjs/dist')
	.copy('node_modules/jquery-cropper/dist', 'storage/compiled/packages/jquery-cropper/dist')
	.copy('node_modules/ckeditor', 'storage/compiled/packages/ckeditor')
	.copy('node_modules/bootstrap-colorpicker/dist', 'storage/compiled/packages/bootstrap-colorpicker/dist')
	.copy('node_modules/bootstrap-iconpicker/bootstrap-iconpicker', 'storage/compiled/packages/bootstrap-iconpicker/bootstrap-iconpicker')
	.copy('node_modules/bootstrap-iconpicker/icon-fonts', 'storage/compiled/packages/bootstrap-iconpicker/icon-fonts')
	.copy('node_modules/simplemde/dist', 'storage/compiled/packages/simplemde/dist')
	.copy('node_modules/easymde/dist', 'storage/compiled/packages/easymde/dist')
	.copy('node_modules/summernote/dist', 'storage/compiled/packages/summernote/dist')
	.copy('node_modules/tinymce', 'storage/compiled/packages/tinymce')
	.copy('node_modules/nestedSortable', 'storage/compiled/packages/nestedSortable')
	.copy('node_modules/datatables.net', 'storage/compiled/packages/datatables.net')
	.copy('node_modules/datatables.net-bs4', 'storage/compiled/packages/datatables.net-bs4')
	.copy('node_modules/datatables.net-fixedheader', 'storage/compiled/packages/datatables.net-fixedheader')
	.copy('node_modules/datatables.net-fixedheader-bs4', 'storage/compiled/packages/datatables.net-fixedheader-bs4')
	.copy('node_modules/datatables.net-responsive', 'storage/compiled/packages/datatables.net-responsive')
	.copy('node_modules/datatables.net-responsive-bs4', 'storage/compiled/packages/datatables.net-responsive-bs4')
	.copy('node_modules/places.js/dist', 'storage/compiled/packages/places.js/dist');

// FOR MAINTAINERS
// copy asset files from Base's public folder the main app's public folder
// so that you don't have to publish the assets with artisan to test them
// mix.copyDirectory('src/public', '../../../public')

// for full API refer to https://laravel-mix.com/docs/main/api
// mix.js(src, output);
// mix.react(src, output); <-- Identical to mix.js(), but registers React Babel compilation.
// mix.preact(src, output); <-- Identical to mix.js(), but registers Preact compilation.
// mix.coffee(src, output); <-- Identical to mix.js(), but registers CoffeeScript compilation.
// mix.ts(src, output); <-- TypeScript support. Requires tsconfig.json to exist in the same folder as webpack.mix.js
// mix.extract(vendorLibs);
// mix.sass(src, output);
// mix.less(src, output);
// mix.stylus(src, output);
// mix.postCss(src, output, [require('postcss-some-plugin')()]);
// mix.browserSync('my-site.test');
// mix.combine(files, destination);
// mix.babel(files, destination); <-- Identical to mix.combine(), but also includes Babel compilation.
// mix.copy(from, to);
// mix.copyDirectory(fromDir, toDir);
// mix.minify(file);
// mix.sourceMaps(); // Enable sourcemaps
// mix.version(); // Enable versioning.
// mix.disableNotifications();
// mix.setPublicPath('path/to/public');
// mix.setResourceRoot('prefix/for/resource/locators');
// mix.autoload({}); <-- Will be passed to Webpack's ProvidePlugin.
// mix.webpackConfig({}); <-- Override webpack.config.js, without editing the file directly.
// mix.babelConfig({}); <-- Merge extra Babel configuration (plugins, etc.) with Mix's default.
// mix.then(function () {}) <-- Will be triggered each time Webpack finishes building.
// mix.override(function (webpackConfig) {}) <-- Will be triggered once the webpack config object has been fully generated by Mix.
// mix.dump(); <-- Dump the generated webpack config object to the console.
// mix.extend(name, handler) <-- Extend Mix's API with your own components.
// mix.options({
//   extractVueStyles: false, // Extract .vue component styling to file, rather than inline.
//   globalVueStyles: file, // Variables file to be imported in every component.
//   processCssUrls: true, // Process/optimize relative stylesheet url()'s. Set to false, if you don't want them touched.
//   purifyCss: false, // Remove unused CSS selectors.
//   terser: {}, // Terser-specific options. https://github.com/webpack-contrib/terser-webpack-plugin#options
//   postCss: [] // Post-CSS options: https://github.com/postcss/postcss/blob/master/docs/plugins.md
// });
