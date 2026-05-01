# Coding Agent Session – Automated Debugging & Optimization Assistant

## Overview
This session showcases a coding agent I built to automatically detect, analyze, and fix runtime issues in a web application. The goal was to reduce debugging time and improve system reliability by enabling the agent to reason through problems instead of just reacting to errors.

---

## Problem
The application frequently encountered:
- API timeouts
- Inefficient database queries
- Hard-to-trace runtime errors

Debugging these issues manually was slow and inconsistent.

---

## Approach

I designed the agent with a structured reasoning loop:

1. **Error Ingestion**
   - Collect logs and normalize error messages
   - Parse stack traces into structured data

2. **Context Retrieval**
   - Fetch relevant code snippets
   - Analyze recent commits for potential causes

3. **Hypothesis Generation**
   - Generate multiple possible root causes
   - Avoid premature conclusions

4. **Validation**
   - Run lightweight checks (query analysis, function tracing)
   - Eliminate incorrect hypotheses

5. **Action**
   - Suggest fixes with explanations
   - Automatically patch low-risk issues

---

## Example Session

### Issue Detected
- Repeated API timeout on `/users/profile`

### Agent Analysis
- Identified slow database query
- Traced issue to recent commit modifying query structure

### Root Cause
- Missing database index on a frequently queried column

### Proposed Fix
```sql
CREATE INDEX idx_user_email ON users(email); 