import React from 'react';
import { AiOutlineComment, AiOutlineDislike, AiOutlineEnter, AiOutlineLike } from 'react-icons/ai';
import Comment from './Comment';

const Comments = () => {
	return (
		<section className="space-y-8 mt-10">
			<form className="flex items-center w-auto h-10 border">
				<div className="w-5 h-5 rounded-full bg-gray-200 mr-1 border border-blue-400"></div>
				<input type="text" className="border h-7 rounded-l-lg w-full px-2" />
				<button className="h-7 w-9 rounded-r-lg border border-l-0 flex items-center justify-center bg-gray-50 hover:bg-gray-100">
					<AiOutlineEnter className="text-gray-500 " />
				</button>
			</form>
			{[1, 2, 3, 4].map((_, i) => (
				<Comment key={i} />
			))}
		</section>
	);
};

export default Comments;
