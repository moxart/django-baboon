const gulp = require('gulp');
const autoprefixer = require('autoprefixer');
const browserSync = require('browser-sync').create();
const sass = require('gulp-sass');
const minify = require('gulp-minify');
const uglify = require('gulp-uglify');
const imagemin = require('gulp-imagemin');
const postcss = require('gulp-postcss');
const rename = require('gulp-rename');
const sourcemaps = require('gulp-sourcemaps');
const del = require('del');

function styles() {
    return gulp.src([
        'blog/assets/blog/styles/blog.scss',
        'blog/assets/dashboard/styles/dashboard.scss'
    ])
        .pipe(sourcemaps.init())
        .pipe(sass({
            includePaths: ['./node_modules'],
            outputStyle: 'compressed'
        }).on('error', sass.logError))
        .pipe(rename({ suffix: '.min'}))
        .pipe(postcss([autoprefixer()]))
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest('blog/static/styles'))
        .pipe(browserSync.stream());
}

function scripts() {
    return gulp.src([
        'blog/assets/blog/scripts/**/*.js',
        'blog/assets/dashboard/scripts/**/*.js',
        './node_modules/trumbowyg/dist/trumbowyg.js',
        './node_modules/feather-icons/dist/feather.js',
    ])
        .pipe(uglify())
        .pipe(gulp.dest('blog/static/scripts'))
        .pipe(browserSync.stream());
}

function images() {
    return gulp.src([
        'blog/assets/blog/images/*',
        'blog/assets/dashboard/images/*'
    ])
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
}

function clean() {
    return del([
        './blog/static/styles',
        './blog/static/scripts',
        './blog/static/images']
    );
}

function watcher() {
    browserSync.init({
        proxy: '127.0.0.1:8000',
        open: false,
        notify: false
    });

    gulp.watch('blog/assets/**/*.scss', styles);
    gulp.watch('blog/assets/**/*.js', scripts);
    gulp.watch('blog/assets/*', images);

    gulp.watch('blog/templates/**/*.html').on('change', browserSync.reload);
}

const build = gulp.series(clean, gulp.parallel(styles, scripts, images));
const watch = gulp.series(build, gulp.parallel(watcher));

exports.styles = styles;
exports.scripts = scripts;
exports.images = images;

exports.clean = clean;
exports.build = build;
exports.watch = watch;
exports.default = build;