interface IReturn {
	code: number;
	success: boolean;
	message: string;
}
interface IArticle {
	article_id: number;
	book: {
		author: string;
		category: string;
		image_url: string;
		title: string;
	};
	comment_count: number;
	created_at: string;
	like_count: number;
	nickname: string;
	user_id: number;
	content: string;
}

interface IGetArticlesReturn extends IReturn {
	data: IArticle[];
}

interface IPetchArticlesLikeReturn extends IReturn {
	data: { article: IArticle };
}
interface IPostArticlesReturn extends IPetchArticlesLikeReturn {}

interface INewArticle {
	content: String;
	book_title: String;
	book_author: String;
	book_category: String;
	book_image_url?: String;
}

interface IComment {
	comment_id: number;
	content: string;
	created_at: string;
	like_count: number;
}
interface IGetCommentsReturn extends IReturn {
	data: {
		article: IArticle;
		comments: IComment[];
	};
}
interface IPostCommentsReturn extends IReturn {
	data: {
		comment: IComment;
	};
}

interface IPatchCommentsLikeReturn extends IReturn {
	data: {
		comment: IComment;
	};
}
