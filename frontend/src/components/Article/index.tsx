import React from 'react';
import { AiFillHeart, AiOutlineBell, AiOutlineComment, AiOutlineDelete, AiOutlineShareAlt } from 'react-icons/ai';
import { useLocation, useParams } from 'react-router-dom';
import { ax } from '../../api/ax';
import Comments from './Comments';
import { useQuery } from '@tanstack/react-query';

const Article = () => {
	const location = useLocation();
	const params = useParams();

	const article: IArticle = location.state.article;
	const { data: comments, isLoading } = useQuery(
		['comment', params.articleId],
		() => ax.getComments(params.articleId),
		{
			onSuccess: () => {
				console.log(`fetched: ${params.articleId}의 댓글`);
			},
		}
	);
	if (comments) console.log(comments[0]);

	return (
		<section className="w-full flex mt-3 px-3  min-h-full">
			<div className="w-full ">
				<header className="flex justify-between  items-center">
					<span className="text-xs text-gray-400">Psosted by {article.nickname} just now</span>
					<AiOutlineBell size="24" className="text-gray-400" />
				</header>
				<h1 className="text-lg font-semibold">{article.book.title}</h1>
				<article className=" mt-3">{article.content}</article>
				<div className="flex w-14 h-14 mx-auto border border-gray-100 justify-center items-center my-5 cursor-pointer text-red-200 hover:border-gray-100 hover:text-red-300">
					<AiFillHeart className=" text-lg w-10 h-10" />
				</div>
				<ul className="flex space-x-7 my-3">
					<li className="flex items-center text-gray-500 space-x-1 cursor-pointer">
						<AiOutlineComment size={22} />
						<span className="text-sm">Comments {article.comment_count}</span>
					</li>
					<li className="flex items-center text-gray-500 space-x-1 cursor-pointer">
						<AiOutlineShareAlt size={22} />
						<span className="text-sm">Share</span>
					</li>
					<li className="flex items-center text-gray-500 space-x-1 cursor-pointer">
						<AiOutlineDelete size={22} />
						<span className="text-sm">Delete</span>
					</li>
				</ul>
				<Comments comments={comments} />
			</div>
		</section>
	);
};

export default Article;
