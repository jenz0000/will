import axios from 'axios';

const BASE_URL = 'https://ggbc66j5a7.execute-api.ap-northeast-2.amazonaws.com/dev/api';

type TMethod = 'GET' | 'POST';

class Axios {
	axiosClient;
	constructor() {
		this.axiosClient = axios.create({
			baseURL: BASE_URL,
		});
	}
	async getArticles(): Promise<IArticle[]> {
		const result = await this.axiosClient.get('/articles').then((res) => res.data);

		if (!result.success) console.log(result.message);
		return result;
	}
	async postArticles(newArticle: INewArticle): Promise<IPostArticlesReturn> {
		const result = await this.axiosClient
			.post('/articles', newArticle, {
				headers: {
					'Content-Type': 'application/json',
				},
			})
			.then((res) => res.data);

		if (!result.success) console.log(result.message);

		return result;
	}

	async patchArticlesLike(articleId: string): Promise<IPetchArticlesLikeReturn> {
		const result = await this.axiosClient
			.patch(`/articles/${articleId}/like`, {
				headers: {
					'Content-Type': 'application/json',
				},
			})
			.then((res) => res.data);
		if (!result.success) console.log(result.message);
		return result;
	}

	async getComments(articleId: string): Promise<IGetCommentsReturn> {
		const result = await this.axiosClient.get(`/comments/${articleId}`).then((res) => res.data);

		if (!result.success) console.log(result.message);
		return result;
	}
	async postComments(newComment: any): Promise<IPostCommentsReturn> {
		const _result = await this.axiosClient
			.post('/comments', newComment, {
				headers: {
					'Content-Type': 'application/json',
				},
			})
			.then((res) => res.data);

		if (!_result.success) console.log(_result.message);

		return _result;
	}
	async patchCommentsLike(commentId: string): Promise<IPatchCommentsLikeReturn> {
		const _result = await this.axiosClient.patch(`/comments/${commentId}/like`).then((res) => res.data);
		if (!_result.success) console.log(_result.message);
		return _result;
	}
}

export const ax = new Axios();
