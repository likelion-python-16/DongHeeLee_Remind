# Personal Habit & Goal Tracker Backend

> 개인 습관과 목표 관리를 위한 백엔드 API 서버  
> AI 추천과 구글 시트 연동 기능을 포함한 통합 습관 관리 플랫폼

---

## 프로젝트 소개

이 프로젝트는 개인의 습관, 운동, 공부, 식단 등 다양한 목표를 기록하고 관리할 수 있는 백엔드 API 서버입니다.  
주요 기능으로는 목표 진행 상황 통계 제공, PDF 리포트 생성, 구글 시트 자동 연동, 그리고 AI 기반 맞춤형 추천 기능이 포함되어 있습니다.

---

## 주요 기능

- 사용자 인증 및 권한 관리 (JWT, 이메일 인증, 비밀번호 재설정)  
- 습관 및 목표 등록, 수정, 삭제  
- 날짜별 기록 입력 및 조회  
- 목표 달성률 자동 계산 및 통계 제공  
- PDF 기반 주간/월간 리포트 자동 생성  
- 구글 시트와의 자동 데이터 동기화 (기록 백업 및 리포트)  
- OpenAI GPT API를 활용한 AI 맞춤형 피드백 및 추천  
- 비동기 작업 처리 (Celery + Redis 기반 알림 및 스케줄링)  
- REST API 문서화 (Swagger)  
- Docker 기반 컨테이너화 및 클라우드 배포 지원  

---

## 사용 기술 스택

| 영역          | 기술                         |
| ------------- | ---------------------------- |
| 백엔드        | Python, Django, Django REST Framework |
| 데이터베이스  | PostgreSQL                   |
| 인증          | JWT (SimpleJWT), 이메일 인증 |
| 비동기 처리   | Celery, Redis                |
| 외부 API 연동 | Google Sheets API, OpenAI GPT API |
| 문서화        | drf-yasg (Swagger)           |
| 배포          | Docker, Railway/AWS          |
| 테스트        | pytest-django                |

---
