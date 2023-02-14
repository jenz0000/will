import React from 'react';
import { AiOutlineComment, AiOutlineDislike, AiOutlineLike } from 'react-icons/ai';
import ReactTimeago from 'react-timeago';

const Comment = ({ comment }: { comment: IComment }) => {
	return (
		<section>
			<div className="flex items-center space-x-2">
				<ReactTimeago className="text-xs text-gray-400" date={comment.created_at} />
			</div>
			<main className="text-sm my-3">{comment.content}</main>
			<ul className="flex text-gray-500 items-center space-x-3">
				<li className="flex items-center space-x-2">
					<AiOutlineLike size={20} className="cursor-pointer" />
					<span className="text-xs">{comment.like_count}</span>
					<AiOutlineDislike size={20} className="cursor-pointer" />
				</li>
			</ul>
		</section>
	);
};

export default Comment;
