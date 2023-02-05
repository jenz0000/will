import React, { useState, useEffect } from 'react';
import ArticleCard from '../../components/ArticleCard';

const Home = () => {
	return (
		<>
			<main className="bg-gray-50 flex flex-col">
				{[1, 2, 3, 4].map((_, i) => (
					<ArticleCard key={i} />
				))}
			</main>
		</>
	);
};

export default Home;
