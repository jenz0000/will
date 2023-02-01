import React from 'react';
import { AiFillHeart, AiOutlineBell, AiOutlineComment, AiOutlineDelete, AiOutlineShareAlt } from 'react-icons/ai';
import Comments from './Comments';

const Article = () => {
	return (
		<section className="w-full flex mt-3 px-3  min-h-full">
			<div className="w-full ">
				<header className="flex justify-between  items-center">
					<span className="text-xs text-gray-400">Psosted by 닉네임 just now</span>
					<AiOutlineBell size="24" className="text-gray-400" />
				</header>
				<h1 className="text-lg font-semibold">Article Title</h1>
				<article className=" mt-3">
					Lorem ipsum dolor sit amet consectetur, adipisicing elit. Id quos ex deleniti in hic voluptate tenetur dolore
					quisquam neque est. Cumque veritatis, deleniti unde in provident facilis corrupti suscipit quae.
				</article>
				<div className="flex w-14 h-14 mx-auto border border-gray-100 justify-center items-center my-5 cursor-pointer text-red-200 hover:border-gray-100 hover:text-red-300">
					<AiFillHeart className=" text-lg w-10 h-10" />
				</div>
				<ul className="flex space-x-7 my-3">
					<li className="flex items-center text-gray-500 space-x-1 cursor-pointer">
						<AiOutlineComment size={22} />
						<span className="text-sm">Comments 4</span>
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
				<Comments />
			</div>
		</section>
	);
};

export default Article;
