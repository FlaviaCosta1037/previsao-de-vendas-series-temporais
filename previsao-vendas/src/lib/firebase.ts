// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";
import { getAuth, GoogleAuthProvider } from "firebase/auth";

// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyClcAffKg4mRZBJSTmcf3Edjfe5DBUAPTo",
  authDomain: "previsao-vendas-e4130.firebaseapp.com",
  projectId: "previsao-vendas-e4130",
  storageBucket: "previsao-vendas-e4130.firebasestorage.app",
  messagingSenderId: "138763141094",
  appId: "1:138763141094:web:56f7e4c3be07815946e027",
  measurementId: "G-95Q5QR9EM7"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
export const db = getFirestore(app);
const auth = getAuth(app);
const provider = new GoogleAuthProvider();
export { app, auth, provider };