import React from 'react';
import styled from 'styled-components';
import { AiOutlineHome, AiOutlineSearch } from 'react-icons/ai';
import { BsPencilSquare } from 'react-icons/bs';
import { Link } from 'react-router-dom';
// import './global.css';

const Header = () => {
	return (
		<section className="w-full h-10 flex justify-between items-center px-3 bg-gray-800">
			<Link to="/">
				<div className=" font-serif font-bold text-white font-sm cursor-pointer">WILL</div>
			</Link>
			<ul className="flex space-x-4">
				<Link to="/">
					<li className="flex items-center space-x-2 text-white">
						<AiOutlineHome size="24" />
						<span className="">Home</span>
					</li>
				</Link>
				<li className="flex items-center space-x-2 text-white">
					<AiOutlineSearch size="24" /> <span>Search</span>
				</li>
				<li className="flex items-center space-x-2 text-white">
					<BsPencilSquare size="24" /> <span>Write</span>
				</li>
			</ul>
		</section>
	);
};

export default Header;

const Logo = styled.div``;
