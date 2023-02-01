import React from 'react';
import {
	AiFillHeart,
	AiOutlineBell,
	AiOutlineComment,
	AiOutlineDelete,
	AiOutlineDislike,
	AiOutlineLike,
	AiOutlineShareAlt,
} from 'react-icons/ai';

const ArticleCard = () => {
	return (
		<>
			<section className="cursor-pointer w-4/6 bg-white mx-auto my-3 rounded border flex overflow-hidden text-gray-600 hover:border-gray-800">
				<div className="bg-gray-100 w-1/12 flex flex-col items-center pt-3 space-y-1">
					<AiOutlineLike className="cursor-pointer hover:text-blue-500" />
					<span className="text-xs">24 k</span>
					<AiOutlineDislike className="cursor-pointer hover:text-blue-500" />
				</div>
				<div className="w-11/12 p-2">
					<header className="flex justify-between  items-center">
						<span className="text-xs text-gray-400">Psosted by 닉네임 just now</span>
						<AiOutlineBell size="24" className="text-gray-400" />
					</header>
					<h1 className="text-lg font-semibold">Article Title</h1>
					<article className=" mt-3">
						Lorem ipsum dolor sit amet consectetur, adipisicing elit. Id quos ex deleniti in hic voluptate tenetur
						dolore quisquam neque est. Cumque veritatis, deleniti unde in provident facilis corrupti suscipit quae.
					</article>

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
				</div>
			</section>
		</>
	);
};

export default ArticleCard;
