/* eslint-disable no-undef */
importScripts('/workbox/workbox-sw.js');

workbox.setConfig({
  modulePathPrefix: '/workbox',
});

workbox.skipWaiting();
workbox.clientsClaim();

/*
 * Default handler for all other requests (html, json, xml)
 * If your page will be purely static, you could set this to cacheWhileRevalidate()
 */
workbox.routing.setDefaultHandler(workbox.strategies.networkFirst({
  cacheName: 'fallback',
}));

/*
 * Caches static files, responds from network first
 */
workbox.routing.registerRoute(
  /\.(?:css|js|svg)$/,
  workbox.strategies.networkFirst({
    cacheName: 'static-files',
  }),
  'GET',
);

/*
 * Cache images
 */
workbox.routing.registerRoute(
  /\.(?:png|gif|jpg|jpeg)$/,
  workbox.strategies.cacheFirst({
    cacheName: 'images',
    plugins: [
      new workbox.expiration.Plugin({
        maxEntries: 60,
        maxAgeSeconds: 2592000,
      }),
    ],
  }),
  'GET',
);
