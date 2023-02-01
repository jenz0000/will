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
                                "title": "모든 분들께 죄송합니다.",
                                "content": "할 말이 없습니다. 죄송합니다.",
                                "nickname": "수줍은 거북이",
                                "like_count": 0,
                                "comment_couunt": 0,
                            },
                            {
                                "id": 2,
                                "created_at": "2023-01-31T12:08:25.991079Z",
                                "user_id": 13,
                                "title": "가족들은 들으라",
                                "content": "강물이 흘러가는구나\n 내 뼈를 강에 부려다오\n면목이 없다\n강물이여 흘러라",
                                "nickname": "수줍은 거북이",
                                "like_count": 0,
                                "comment_couunt": 0,
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
                "name": "title",
                "type": openapi.TYPE_STRING,
                "description": "제목",
            },
            {
                "name": "content",
                "type": openapi.TYPE_STRING,
                "description": "본문 내용",
            },
        ],
        res=[
            {
                "name": "200",
                "description": "성공",
                "res": {
                    "data": {
                        "article": {
                            "id": 4,
                            "created_at": "2023-02-01T09:33:54.511735Z",
                            "user_id": 7730433416852955556,
                            "title": "테스트",
                            "content": "hhhh",
                            "nickname": "부끄러운 당나귀",
                            "like_count": 0,
                            "comment_couunt": 0,
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
