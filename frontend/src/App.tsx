import { ReactQueryDevtools } from '@tanstack/react-query-devtools';
import React, { useState } from 'react';
import { Outlet, useSearchParams } from 'react-router-dom';
import FloatingBtn from './components/FloatingBtn';
import Header from './components/Header';
import PostArticleModal from './components/PostArticleModal';
import './global.css';
// import Home from './pages/Home/Home';

function App() {
	const [openPostArticleModal, setOpenPostArticleModal] = useState(false);

	const handleFloatingBtn = () => {
		console.log('floating btn clicked');
		setOpenPostArticleModal((prev) => !prev);
	};
	return (
		<>
			<Header />
			<Outlet />
			<FloatingBtn onClick={handleFloatingBtn} />
			{openPostArticleModal && <PostArticleModal setOpenPostArticleModal={setOpenPostArticleModal} />}
			<ReactQueryDevtools initialIsOpen={false} />
			<div onClick={handleFloatingBtn}></div>
		</>
	);
}

export default App;
