import { ReactQueryDevtools } from '@tanstack/react-query-devtools';
import React, { useState } from 'react';
import { Outlet, useSearchParams } from 'react-router-dom';
import FloatingBtn from './components/FloatingBtn';
import Header from './components/Header';
import './global.css';
// import Home from './pages/Home/Home';

function App() {
	return (
		<>
			<Header />
			<Outlet />
			<FloatingBtn />
			<ReactQueryDevtools initialIsOpen={false} />
		</>
	);
}

export default App;
