import { ReactQueryDevtools } from '@tanstack/react-query-devtools';
import React, { useState } from 'react';
import { Outlet, useSearchParams } from 'react-router-dom';
import { Reset } from 'styled-reset';
// import Home from './pages/Home/Home';

function App() {
	const [toggleSNB, setToggleSNB] = useState(false);

	return (
		<>
			<Reset />
			<Outlet />
			<ReactQueryDevtools initialIsOpen={false} />
		</>
	);
}

export default App;
