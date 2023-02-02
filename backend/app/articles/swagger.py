# System
from drf_yasg import openapi

# Project
from config.swagger import Swagger


class ArticleSwagger:
    list = Swagger(
        body=[],
        res=[
            {
                "name": "200",
                "description": "성공",
                "res": {
                    "data": {
                        "articles": [
                            {
                                "id": 1,
                                "created_at": "2023-01-31T11:50:56.877932Z",
                                "user_id": 1,
                                "content": "할 말이 없습니다. 죄송합니다.",
                                "nickname": "수줍은 거북이",
                                "like_count": 0,
                                "comment_couunt": 0,
                                "book": {
                                    "title": "temp-title",
                                    "author": "temp-author",
                                    "category": "temp-category",
                                    "image_url": "http://books.google.com/books/content?id=N8XyDwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api",
                                },
                            },
                            {
                                "id": 2,
                                "created_at": "2023-01-31T12:08:25.991079Z",
                                "user_id": 13,
                                "content": "강물이 흘러가는구나 내 뼈를 강에 부려다오면목이 없다강물이여 흘러라",
                                "nickname": "부끄러운 딱다구리",
                                "like_count": 0,
                                "comment_couunt": 0,
                                "book": {
                                    "title": "title",
                                    "author": "temp-author",
                                    "category": "temp_category",
                                    "image_url": "books.google.com/books/content?id=N8XyDwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api",
                                },
                            },
                        ]
                    },
                    "code": 0,
                    "success": True,
                    "message": "SUCCESS",
                },
            },
        ],
    )

    create = Swagger(
        body=[
            {
                "name": "content",
                "type": openapi.TYPE_STRING,
                "description": "본문 내용",
            },
            {
                "name": "book_title",
                "type": openapi.TYPE_STRING,
                "description": "책 제목",
            },
            {
                "name": "book_author",
                "type": openapi.TYPE_STRING,
                "description": "책 저자",
            },
            {
                "name": "book_category",
                "type": openapi.TYPE_STRING,
                "description": "책 카테고리",
            },
            {
                "name": "book_image_url",
                "type": openapi.TYPE_STRING,
                "description": "책 이미지 URL",
            },
        ],
        required=["content", "book_title", "book_author", "book_category"],
        res=[
            {
                "name": "200",
                "description": "성공",
                "res": {
                    "data": {
                        "article": {
                            "id": 6,
                            "created_at": "2023-02-02T13:00:20.858048Z",
                            "user_id": 5849203113198067822,
                            "content": "hhhh",
                            "nickname": "",
                            "like_count": 0,
                            "comment_couunt": 0,
                            "book": {
                                "title": "테스트 제목",
                                "author": "테스트 저자",
                                "category": "테스트 카테고리",
                                "image_url": None,
                            },
                        }
                    },
                    "code": 0,
                    "message": "SUCCESS",
                    "success": True,
                },
            },
            {
                "name": "400 (1)",
                "description": "부적절한 파리미터 형태로 요청했을 때",
                "res": {
                    "data": {},
                    "code": 1,
                    "message": "INVALID_PARAMETERS",
                    "success": False,
                },
            },
        ],
    )
