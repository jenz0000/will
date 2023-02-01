import React from 'react';
import { AiOutlineComment, AiOutlineDislike, AiOutlineLike } from 'react-icons/ai';

const Comment = () => {
	return (
		<section>
			<div className="flex items-center space-x-2">
				<div className="w-5 h-5 rounded-full bg-gray-300"></div>
				<span className="text-xs">Nickname</span>
				<span className="text-xs text-gray-400">10 hr ago</span>
			</div>
			<main className="text-sm my-3">
				Lorem ipsum dolor sit amet, consectetur adipisicing elit. Nihil qui ea officiis voluptates at illo possimus
				quisquam,
			</main>
			<ul className="flex text-gray-500 items-center space-x-3">
				<li className="flex items-center">
					<AiOutlineLike size={20} className="cursor-pointer" />
					<span className="text-xs">{23}</span>
					<AiOutlineDislike size={20} className="cursor-pointer" />
				</li>
				<li></li>
				<li className="flex items-center space-x-1 cursor-pointer">
					<AiOutlineComment size={20} />
					<span className="text-xs">Reply</span>
				</li>
			</ul>
		</section>
	);
};

export default Comment;
