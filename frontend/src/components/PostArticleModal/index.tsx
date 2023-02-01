import React from 'react';

interface IPostArticleModalProps {
	setOpenPostArticleModal: any;
}
const PostArticleModal = ({ setOpenPostArticleModal }: IPostArticleModalProps) => {
	return (
		<section className="fixed w-screen h-screen bg-black/30 left-0 top-0 flex justify-center items-center">
			<div className="bg-white border w-5/6 h-5/6 box-border">
				<div className="flex justify-between items-center border-b h-10 px-3">
					<span className="text-blue-400 cursor-pointer" onClick={() => setOpenPostArticleModal(false)}>
						Cancel
					</span>
					<span className="text-sm">Create a Post</span>
					<span className="text-blue-400 font-semibold cursor-pointer">Post</span>
				</div>
				<div className="">
					<input className="border-b border-r w-1/2 h-8  text-sm px-2" type="text" placeholder="닉네임" />
					<input className="border-b w-1/2 h-8  text-sm px-2" type="password" placeholder="패스워드" />
				</div>
				<div>
					<input type="textarea" className="border-b w-full px-2 h-12 font-semibold" placeholder="제목" />
				</div>
				<textarea className="p-2 w-full h-96 flex grow" placeholder="내용"></textarea>
			</div>
		</section>
	);
};

export default PostArticleModal;
