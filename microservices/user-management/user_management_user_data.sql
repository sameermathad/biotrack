--
-- PostgreSQL database dump
--

-- Dumped from database version 14.13 (Homebrew)
-- Dumped by pg_dump version 16.3 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Data for Name: user_management_user; Type: TABLE DATA; Schema: public; Owner: sam
--

COPY public.user_management_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, role_id) FROM stdin;
2	pbkdf2_sha256$260000$KkVi0ElSHJJPTNQvcmjbpX$pqWJXlUEInf+HlTWWY4O/z33QHeyB883HK3GKKIyNv4=	\N	t	sameermathad	Sameer	Mathad	sameer@vb.in	t	t	2024-08-12 21:24:13.604+05:30	2
3	pbkdf2_sha256$260000$5KxXqswOoih211BadpLykp$1duz8T/FAAT2Txb0n1BKG5pBZJn5LOc7zY11rTinAZc=	\N	t	sam	Test	User	sam@biotrack.com	t	t	2024-08-10 04:05:01.36+05:30	8
7	pbkdf2_sha256$260000$BE0JE1BBx36wXLoj1dFCKF$eRy8icff5D0/ZsGvPwOwbxPsHpINconCIkoHa4LmOus=	\N	t	sameermathad01	fsadf	dfa	dsd@sdfa.com	f	t	2024-08-13 02:21:29.208+05:30	4
9	pbkdf2_sha256$260000$LyGwkq1I7iISXGXIdpDuxc$ouHWfSj46RGc7I/tUmedP36K2wBmom5bjk1Oj6F5J0Y=	\N	t	sameermathad02	fasdf	dadfs	faf@dfsad.com	f	t	2024-08-13 15:16:48.946+05:30	5
10	pbkdf2_sha256$260000$6agYnTn9tIt1L4S9mKCwwq$eUEca8pinw8zALZOOiquhsl9bFyAIfJ1JTNE2+oq00A=	\N	t	sameermathad03	sfad	fadsf	sam@sam.cojm	f	t	2024-08-13 15:42:46.124+05:30	3
1	pbkdf2_sha256$260000$70Y059Qj6bPcF0oqWfSJ4U$cihJAEyZX4HBymq8LLrUDC6Jz8vpfBkJg6Kovdm9RQI=	\N	t	sameermathadbio	Tom	Hardy	sameer@biotrack.in	t	t	2024-08-12 22:37:03.917+05:30	6
12	pbkdf2_sha256$260000$4heON20Cexa0u5LLm8gOjg$wMQWRrUe2q0cljKLChNdicf/2OeyFzpieT4bztk3j74=	\N	t	ashwinsudhini	a	s	ashwinsudhini@gmail.com	f	t	2024-08-14 16:31:24.461152+05:30	2
13	pbkdf2_sha256$260000$uF5X1q6CBj8hAyzeRQZeje$Jj5AuKPRB84MreHUyty6gCMF9e0zSWD2k83DhJ6dPB4=	\N	t	mayuragarwal	Mayur	Agarwal	mayuragarwal@gmail.com	f	t	2024-08-14 20:29:45.369233+05:30	4
\.


--
-- Name: user_management_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: sam
--

SELECT pg_catalog.setval('public.user_management_user_id_seq', 13, true);


--
-- PostgreSQL database dump complete
--

