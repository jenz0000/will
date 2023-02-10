import React, { useState, useEffect } from 'react';
import { ax } from '../../api/articles';
import ArticleCard from '../../components/ArticleCard';

const testObj = {
	content: 'my 230210 testttt',
	book_title: 'my 230210 testttt',
	book_author: 'my 230210 testttt',
	book_category: 'my 230210 testttt',
	book_image_url: 'my 230210 testttt',
};

const testInput = {
	article_id: 1,
	content: 'myTestInput',
};
const Home = () => {
	useEffect(() => {
		const test = async () => {
			const result = await ax.patchCommentsLike('20');
			console.log(result.data.comment.like_count);
		};
		test();
	}, []);
	// ax.comments('POST', testInput);
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
