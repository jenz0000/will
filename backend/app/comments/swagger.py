# System
from drf_yasg import openapi

# Project
from config.swagger import Swagger


class CommentSwagger:
    list = Swagger(
        body=[],
        res=[
            {
                "name": "200",
                "description": "성공",
                "res": {
                    "data": {
                        "article": {
                            "id": 1,
                            "created_at": "2023-01-31T11:50:56.877932Z",
                            "user_id": 1,
                            "content": "할 말이 없습니다. 죄송합니다.",
                            "nickname": "수줍은 거북이",
                            "like_count": 0,
                            "comment_count": 1,
                            "book": {
                                "title": "temp-title",
                                "author": "temp-author",
                                "category": "temp-category",
                                "image_url": "http://books.google.com/books/content?id=N8XyDwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api",
                            },
                        },
                        "comments": [
                            {
                                "id": 1,
                                "created_at": "2023-02-03T12:18:58.929997Z",
                                "content": "hohoho",
                            },
                        ],
                    },
                    "code": 0,
                    "message": "SUCCESS",
                    "success": True,
                },
            },
            {
                "name": "400",
                "description": "존재하지 않는 게시물 ID로 요청했을 때",
                "res": {
                    "data": {},
                    "code": 2,
                    "message": "ARTICLE_NOT_FOUND",
                    "success": False,
                },
            },
        ],
    )

    create = Swagger(
        body=[
            {
                "name": "article_id",
                "type": openapi.TYPE_INTEGER,
                "description": "게시물 ID",
            },
            {
                "name": "content",
                "type": openapi.TYPE_STRING,
                "description": "내용",
            },
        ],
        required=["article_id", "content"],
        res=[
            {
                "name": "200",
                "description": "성공",
                "res": {
                    "data": {
                        "comment": {
                            "id": 5,
                            "created_at": "2023-02-03T12:54:51.137138Z",
                            "content": "굳굳!",
                        },
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
            {
                "name": "400 (2)",
                "description": "존재하지 않는 게시물 ID로 요청했을 때",
                "res": {
                    "data": {},
                    "code": 2,
                    "message": "ARTICLE_NOT_FOUND",
                    "success": False,
                },
            },
        ],
    )
