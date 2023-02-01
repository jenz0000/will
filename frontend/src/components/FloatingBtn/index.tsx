import React from 'react';
import { AiFillPlusCircle } from 'react-icons/ai';

const FloatingBtn = () => {
	return (
		<button className="fixed bg-gray-200 text-blue-500 rounded-full right-10 bottom-10 cursor-pointer">
			<AiFillPlusCircle size={50} />
		</button>
	);
};

export default FloatingBtn;
