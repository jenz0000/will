interface ImportMetaEnv {
	readonly VITE_API_KEY: string;
}

interface ImportMeta {
	readonly env: ImportMetaEnv;
}

interface IArticle {
	id: number;
	created_at: string;
	user_id: number;
	content: string;
	nickname: string;
	like_count: number;
	comment_count: number;
	book: {
		title: string;
		author: string;
		category: string;
		image_url: string;
	};
}

interface IArticles {
	data: IArticle[];
	code: number;
	success: boolean;
	message: string;
}
interface IComment {
	id: number;
	created_at: string;
	content: string;
}
interface IComments {
	data: {
		article: IArticle;
		comments: IComment[];
	};
	code: number;
	message: string;
	success: boolean;
}
