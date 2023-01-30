import { createRoot } from 'react-dom/client';
import { RouterProvider } from 'react-router-dom';
import { createGlobalStyle, ThemeProvider } from 'styled-components';
import reset from 'styled-reset';
import router from './router';
import { QueryClientProvider, QueryClient } from '@tanstack/react-query';
import './index.css';
import theme from './theme';

const container = document.getElementById('root')!;
const root = createRoot(container);
const queryClient = new QueryClient({
	defaultOptions: {
		queries: {
			staleTime: Infinity,
			cacheTime: Infinity,
			refetchOnWindowFocus: false,
			retry: false,
		},
		mutations: {
			cacheTime: Infinity,
			retry: false,
		},
	},
});

root.render(
	<QueryClientProvider client={queryClient}>
		<ThemeProvider theme={theme}>
			<RouterProvider router={router} />
		</ThemeProvider>
	</QueryClientProvider>
);
