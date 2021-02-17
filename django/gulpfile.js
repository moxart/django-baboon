const gulp = require('gulp');
const autoprefixer = require('autoprefixer');
const browserSync = require('browser-sync').create();
const sass = require('gulp-sass');
const rtlcss = require('gulp-rtlcss');
const minify = require('gulp-minify');
const uglify = require('gulp-uglify');
const imagemin = require('gulp-imagemin');
const postcss = require('gulp-postcss');
const rename = require('gulp-rename');
const sourcemaps = require('gulp-sourcemaps');
const merge = require('merge-stream');
const del = require('del');

function styles() {
    var blog = gulp.src('blog/assets/styles/blog.scss')
        .pipe(sourcemaps.init())
        .pipe(sass({
            includePaths: ['./node_modules'],
            outputStyle: 'compressed'
        }).on('error', sass.logError))
        .pipe(rename({ suffix: '.min'}))
        .pipe(postcss([autoprefixer()]))
        .pipe(rtlcss())
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest('blog/static/styles'))
        .pipe(browserSync.stream());

    var dashboard = gulp.src('dashboard/assets/styles/dashboard.scss')
        .pipe(sourcemaps.init())
        .pipe(sass({
            includePaths: ['./node_modules'],
            outputStyle: 'compressed'
        }).on('error', sass.logError))
        .pipe(rename({ suffix: '.min'}))
        .pipe(postcss([autoprefixer()]))
        .pipe(rtlcss())
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest('dashboard/static/styles'))
        .pipe(browserSync.stream());

    return merge(blog, dashboard);
}

function scripts() {
    var blog = gulp.src([
        'blog/assets/scripts/**/*.js',
        './node_modules/trumbowyg/dist/trumbowyg.js',
        './node_modules/feather-icons/dist/feather.js',
    ])
        .pipe(uglify())
        .pipe(gulp.dest('blog/static/scripts'))
        .pipe(browserSync.stream());

    var dashboard = gulp.src([
        'dashboard/assets/scripts/**/*.js',
        './node_modules/trumbowyg/dist/trumbowyg.js',
        './node_modules/feather-icons/dist/feather.js',
    ])
        .pipe(uglify())
        .pipe(gulp.dest('dashboard/static/scripts'))
        .pipe(browserSync.stream());

    return merge(blog, dashboard);
}

function images() {
    var blog = gulp.src('blog/assets/images/**/*')
        .pipe(imagemin([
            imagemin.gifsicle({interlaced: true}),
            imagemin.mozjpeg({quality: 75, progressive: true}),
            imagemin.optipng({optimizationLevel: 5}),
            imagemin.svgo({
                plugins: [
                    {removeViewBox: true},
                    {cleanupIDs: false}
                ]
            })
        ]))
        .pipe(minify())
        .pipe(gulp.dest('blog/static/images'))
        .pipe(browserSync.stream());

    var dashboard = gulp.src('dashboard/assets/images/**/*')
        .pipe(imagemin([
            imagemin.gifsicle({interlaced: true}),
            imagemin.mozjpeg({quality: 75, progressive: true}),
            imagemin.optipng({optimizationLevel: 5}),
            imagemin.svgo({
                plugins: [
                    {removeViewBox: true},
                    {cleanupIDs: false}
                ]
            })
        ]))
        .pipe(minify())
        .pipe(gulp.dest('dashboard/static/images'))
        .pipe(browserSync.stream());

    return merge(blog, dashboard);
}

function fonts() {
    var blog = gulp.src('blog/assets/fonts/**/*')
        .pipe(gulp.dest('blog/static/fonts'))
        .pipe(browserSync.stream());

    var dashboard = gulp.src('blog/assets/fonts/**/*')
        .pipe(gulp.dest('dashboard/static/fonts'))
        .pipe(browserSync.stream());

    return merge(blog, dashboard);
}

function clean() {
    return del([
            './dashboard/static/styles',
            './dashboard/static/scripts',
            './dashboard/static/images',
            './dashboard/static/fonts',
            './blog/static/styles',
            './blog/static/scripts',
            './blog/static/images',
            './blog/static/fonts',
        ]
    );
}

function watcher() {
    browserSync.init({
        proxy: '127.0.0.1:8002',
        open: false,
        notify: false
    });

    gulp.watch('dashboard/assets/**/*.scss', styles);
    gulp.watch('dashboard/assets/**/*.js', scripts);
    gulp.watch('dashboard/assets/images/**/*', images);
    gulp.watch('dashboard/assets/fonts/**/*', fonts)
    gulp.watch('dashboard/templates/**/*.html').on('change', browserSync.reload);

    gulp.watch('blog/assets/**/*.scss', styles);
    gulp.watch('blog/assets/**/*.js', scripts);
    gulp.watch('blog/assets/images/**/*', images);
    gulp.watch('blog/assets/fonts/**/*', fonts);
    gulp.watch('blog/templates/**/*.html').on('change', browserSync.reload);
}

const build = gulp.series(clean, gulp.parallel(styles, scripts, fonts, images));
const watch = gulp.series(build, gulp.parallel(watcher));

exports.styles = styles;
exports.scripts = scripts;
exports.images = images;
exports.fonts = fonts;
exports.clean = clean;
exports.build = build;
exports.watch = watch;
exports.default = build;