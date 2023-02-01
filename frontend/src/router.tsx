import { createBrowserRouter } from 'react-router-dom';
import App from './App';
import Home from './pages/Home/Home';
import Detail from './pages/Articles/Detail';

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
				element: <Detail />,
			},
		],
	},
]);

export default router;
