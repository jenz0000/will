import React from 'react';
import { AiFillPlusCircle } from 'react-icons/ai';

interface IFloatingBtnProps {
	onClick: React.MouseEventHandler<HTMLButtonElement>;
}

const FloatingBtn = ({ onClick }: IFloatingBtnProps) => {
	return (
		<button
			onClick={onClick}
			className="fixed bg-gray-200 text-blue-500 rounded-full right-10 bottom-10 cursor-pointer"
		>
			<AiFillPlusCircle size={50} />
		</button>
	);
};

export default FloatingBtn;
