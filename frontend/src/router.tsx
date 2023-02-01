import { createBrowserRouter } from 'react-router-dom';
import App from './App';
import Home from './pages/Home/Home';
import Detail from './pages/Articles/Detail';
import Article from './components/Article';

const router = createBrowserRouter([
	{
		path: '/',
		element: <App />,
		children: [
			{
				index: true,
				element: <Home />,
			},
			{
				path: 'articles/:articleId',
				element: <Article />,
			},
		],
	},
]);

export default router;
