// Scripts for firebase and firebase messaging
importScripts('https://www.gstatic.com/firebasejs/8.4.1/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/8.4.1/firebase-messaging.js');

// Initialize the Firebase app in the service worker by passing the generated config
var firebaseConfig = {
  apiKey: "AIzaSyA7OGuIcqhZ4MpqboI7a3yM9ViTbh7efak",
      authDomain: "doorlockapp-6b97f.firebaseapp.com",
      databaseURL: "https://doorlockapp-6b97f-default-rtdb.asia-southeast1.firebasedatabase.app",
      projectId: "doorlockapp-6b97f",
      storageBucket: "doorlockapp-6b97f.appspot.com",
      messagingSenderId: "378668336240",
      appId: "1:378668336240:web:3ab8ca16dcb7da5e1ba0b5",
      measurementId: "G-VFHCDJFYHS"
};

firebase.initializeApp(firebaseConfig);

// Retrieve firebase messaging
const messaging = firebase.messaging();

messaging.onBackgroundMessage(function(payload) {
  console.log('Received background message ', payload);

  const notificationTitle = payload.data.title;
  const notificationOptions = {
    body: payload.data.body,
  };

  self.registration.showNotification(notificationTitle,
    notificationOptions);
});

//open app on notification click
self.addEventListener('notificationclick', function(event) {
  console.log('[Service Worker] Notification click received.');

  event.notification.close();

  event.waitUntil(
    clients.openWindow('/index.html')
  );
});
