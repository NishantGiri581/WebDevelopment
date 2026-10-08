// app/store.js
import { configureStore } from '@reduxjs/toolkit';
import counterSlice from '../fetures/CounterSlice';

export const store = configureStore({
  reducer: {
    counter: counterSlice, // Add as many reducers as you need here
  },
});