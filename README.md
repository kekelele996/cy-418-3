# LegalScan 法律文书智能审查助手

## 快速启动

```bash
docker compose up -d
curl http://localhost:19418/health
```

LegalScan 是面向律师与企业法务的纯后端 RESTful API 服务，提供用户认证、文档上传、规则审查、风险条目生成和报告导出。

## 主要功能

- JWT + RBAC：注册、登录、当前用户信息。
- 文档管理：上传、列表、状态查询。
- 审查任务：提交审查、查询结果、筛选风险条目。
- 报告导出：按 ReviewTask 生成文本报告。
- 横切能力：操作日志、限流、错误处理、Celery + Redis 异步任务。

## 技术栈

| 分类 | 技术 |
| --- | --- |
| 后端 | FastAPI + Python 3.11 |
| ORM | SQLAlchemy 2.0 |
| 数据库 | PostgreSQL 15 |
| 队列 | Celery + Redis |
| 文档 | PyPDF2 / python-docx |
| 报告 | ReportLab / python-docx |

## 目录结构

```
backend/src/
├── routes/
├── controllers/
├── services/
├── models/
├── schemas/
├── middlewares/
├── utils/
├── types/
├── constants/
├── config/
├── tasks/
└── alembic/
```

## API 示例

- `POST /api/auth/register`
- `POST /api/auth/login`
- `GET /api/auth/me`
- `POST /api/documents`
- `GET /api/reviews/{id}/risks`
- `GET /api/reports/{reviewId}/export`

## 枚举出现位置清单

RiskLevel：
- `backend/src/constants/risk.py`
- `backend/src/models/review_task.py`
- `backend/src/models/risk_item.py`
- `backend/src/schemas/review.py`
- `backend/src/services/review_service.py`
- `backend/src/services/risk_engine.py`
- `backend/src/services/report_generator.py`
- `backend/src/constants/log_templates.py`
- `backend/src/constants/error_codes.py`
- `backend/src/utils/formatters.py`

ClauseType：
- `backend/src/constants/contract.py`
- `backend/src/models/risk_item.py`
- `backend/src/schemas/review.py`
- `backend/src/services/risk_engine.py`
- `backend/src/services/report_generator.py`
- `backend/src/routes/reviews.py`
- `backend/src/constants/log_templates.py`
- `backend/src/utils/formatters.py`

## 环境变量

见 `.env.example`。所有数据库、Redis、JWT、上传目录配置均通过环境变量注入。

## License

MIT

