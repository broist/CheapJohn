FROM composer:2 AS vendor

WORKDIR /app
COPY composer.json composer.lock ./
RUN composer install --no-interaction --no-scripts --prefer-dist

FROM php:8.4-cli

RUN apt-get update && apt-get install -y --no-install-recommends \
        libpq-dev libzip-dev libonig-dev libxml2-dev libcurl4-openssl-dev unzip \
    && docker-php-ext-install pdo pdo_pgsql pgsql mbstring bcmath zip xml dom curl \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .
COPY --from=vendor /app/vendor ./vendor

EXPOSE 8000
CMD ["php", "artisan", "serve", "--host=0.0.0.0", "--port=8000"]
