/* POLI-ROUTE device-lab shell-50; only the test PWA scope is affected. */
var CACHE = 'poli-route-shell-50-device-lab';
var APP = './index.html';
function partOfLab(url) {
  if (url.origin !== self.location.origin) return false;
  var scope = new URL(self.registration.scope);
  if (!url.pathname.startsWith(scope.pathname)) return false;
  var file = url.pathname.slice(scope.pathname.length);
  return file === '' || /^(?:index|device-check)\.html$/.test(file) ||
    file === 'manifest.webmanifest' || /^icons\/icon-(?:180|192|512)\.png$/.test(file);
}
self.addEventListener('install', function (event) {
  self.skipWaiting();
  event.waitUntil(caches.open(CACHE).then(function (cache) { return cache.add(APP); }));
});
self.addEventListener('activate', function (event) {
  event.waitUntil(caches.keys().then(function (keys) {
    return Promise.all(keys.filter(function (key) {
      return key !== CACHE && key.indexOf('poli-route-shell-') === 0 && key.endsWith('-device-lab');
    }).map(function (key) { return caches.delete(key); }));
  }).then(function () { return self.clients.claim(); }));
});
self.addEventListener('fetch', function (event) {
  var req = event.request;
  if (req.method !== 'GET') return;
  var u;
  try { u = new URL(req.url); } catch (e) { return; }
  if (!partOfLab(u)) return;
  event.respondWith(fetch(req, {cache:'reload'}).then(function (response) {
    if (response && response.ok) {
      var copy = response.clone();
      caches.open(CACHE).then(function (cache) { return cache.put(req, copy); });
    }
    return response;
  }).catch(function () {
    return caches.match(req).then(function (hit) { return hit || caches.match(APP); });
  }));
});
