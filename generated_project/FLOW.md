```mermaid
graph TD
  A[SRS Upload] --> B[Analyze SRS]
  B --> C[Generate Tests]
  C --> D[Generate Code]
  D --> E[Run + Retry Tests]
  E --> F[Package Project]
```