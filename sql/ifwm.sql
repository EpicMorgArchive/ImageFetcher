-- phpMyAdmin SQL Dump
-- version 3.5.5
-- http://www.phpmyadmin.net
--
-- Хост: localhost
-- Время создания: Сен 06 2013 г., 14:54
-- Версия сервера: 5.5.32-log
-- Версия PHP: 5.4.13--pl0-gentoo

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- База данных: `ifwm`
--

-- --------------------------------------------------------

--
-- Структура таблицы `admin_tools_dashboard_preferences`
--

CREATE TABLE IF NOT EXISTS `admin_tools_dashboard_preferences` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `data` longtext NOT NULL,
  `dashboard_id` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `admin_tools_dashboard_prefer_dashboard_id_374bce90a8a4eefc_uniq` (`dashboard_id`,`user_id`),
  KEY `admin_tools_dashboard_preferences_6340c63c` (`user_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2 ;

--
-- Дамп данных таблицы `admin_tools_dashboard_preferences`
--

INSERT INTO `admin_tools_dashboard_preferences` (`id`, `user_id`, `data`, `dashboard_id`) VALUES
(1, 1, '{}', 'dashboard');

-- --------------------------------------------------------

--
-- Структура таблицы `admin_tools_menu_bookmark`
--

CREATE TABLE IF NOT EXISTS `admin_tools_menu_bookmark` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `url` varchar(255) NOT NULL,
  `title` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `admin_tools_menu_bookmark_6340c63c` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура таблицы `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура таблицы `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_5f412f9a` (`group_id`),
  KEY `auth_group_permissions_83d7f98b` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура таблицы `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_37ef4eb4` (`content_type_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=40 ;

--
-- Дамп данных таблицы `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add permission', 1, 'add_permission'),
(2, 'Can change permission', 1, 'change_permission'),
(3, 'Can delete permission', 1, 'delete_permission'),
(4, 'Can add group', 2, 'add_group'),
(5, 'Can change group', 2, 'change_group'),
(6, 'Can delete group', 2, 'delete_group'),
(7, 'Can add user', 3, 'add_user'),
(8, 'Can change user', 3, 'change_user'),
(9, 'Can delete user', 3, 'delete_user'),
(10, 'Can add content type', 4, 'add_contenttype'),
(11, 'Can change content type', 4, 'change_contenttype'),
(12, 'Can delete content type', 4, 'delete_contenttype'),
(13, 'Can add session', 5, 'add_session'),
(14, 'Can change session', 5, 'change_session'),
(15, 'Can delete session', 5, 'delete_session'),
(16, 'Can add site', 6, 'add_site'),
(17, 'Can change site', 6, 'change_site'),
(18, 'Can delete site', 6, 'delete_site'),
(19, 'Can add log entry', 7, 'add_logentry'),
(20, 'Can change log entry', 7, 'change_logentry'),
(21, 'Can delete log entry', 7, 'delete_logentry'),
(22, 'Can add urls', 8, 'add_urls'),
(23, 'Can change urls', 8, 'change_urls'),
(24, 'Can delete urls', 8, 'delete_urls'),
(25, 'Can add pages', 9, 'add_pages'),
(26, 'Can change pages', 9, 'change_pages'),
(27, 'Can delete pages', 9, 'delete_pages'),
(28, 'Can add images', 10, 'add_images'),
(29, 'Can change images', 10, 'change_images'),
(30, 'Can delete images', 10, 'delete_images'),
(31, 'Can add migration history', 11, 'add_migrationhistory'),
(32, 'Can change migration history', 11, 'change_migrationhistory'),
(33, 'Can delete migration history', 11, 'delete_migrationhistory'),
(34, 'Can add bookmark', 12, 'add_bookmark'),
(35, 'Can change bookmark', 12, 'change_bookmark'),
(36, 'Can delete bookmark', 12, 'delete_bookmark'),
(37, 'Can add dashboard preferences', 13, 'add_dashboardpreferences'),
(38, 'Can change dashboard preferences', 13, 'change_dashboardpreferences'),
(39, 'Can delete dashboard preferences', 13, 'delete_dashboardpreferences');

-- --------------------------------------------------------

--
-- Структура таблицы `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2 ;

--
-- Дамп данных таблицы `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$10000$UjL5oqEaDr4p$X6gBdHYAz+k8fJ3q4pyi6acqu8CS6IIpuXeQQQbflo4=', '2013-09-05 23:55:18', 1, 'kasthack', '', '', 'kasthack@epicm.org', 1, 1, '2013-09-05 23:50:51');

-- --------------------------------------------------------

--
-- Структура таблицы `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_6340c63c` (`user_id`),
  KEY `auth_user_groups_5f412f9a` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура таблицы `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_6340c63c` (`user_id`),
  KEY `auth_user_user_permissions_83d7f98b` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура таблицы `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_6340c63c` (`user_id`),
  KEY `django_admin_log_37ef4eb4` (`content_type_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Структура таблицы `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=14 ;

--
-- Дамп данных таблицы `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `name`, `app_label`, `model`) VALUES
(1, 'permission', 'auth', 'permission'),
(2, 'group', 'auth', 'group'),
(3, 'user', 'auth', 'user'),
(4, 'content type', 'contenttypes', 'contenttype'),
(5, 'session', 'sessions', 'session'),
(6, 'site', 'sites', 'site'),
(7, 'log entry', 'admin', 'logentry'),
(8, 'urls', 'home', 'urls'),
(9, 'pages', 'home', 'pages'),
(10, 'images', 'home', 'images'),
(11, 'migration history', 'south', 'migrationhistory'),
(12, 'bookmark', 'menu', 'bookmark'),
(13, 'dashboard preferences', 'dashboard', 'dashboardpreferences');

-- --------------------------------------------------------

--
-- Структура таблицы `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_b7b81f0c` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('49e4vc9k8kg0adhx88rf7d7l1gbltooo', 'Nzg3NjAxNGVhMjRmNzNkNjJjYWU2M2FhN2U3MWFkOGUzZTlkNzRiZTqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==', '2013-09-19 23:55:18'),
('a9yhs0td0ybj9jh2a7rzradhmeq927gn', 'ODlhODE1NTI3ZTc5ZWE1MWJiZGRkNmY5NTkxODhhOTY2M2FkMWE1OTqAAn1xAS4=', '2013-09-20 08:31:06'),
('rncc2tnmcyjfaahkh4wounrlgsnhkphh', 'ODlhODE1NTI3ZTc5ZWE1MWJiZGRkNmY5NTkxODhhOTY2M2FkMWE1OTqAAn1xAS4=', '2013-09-20 08:31:05');

-- --------------------------------------------------------

--
-- Структура таблицы `django_site`
--

CREATE TABLE IF NOT EXISTS `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2 ;

--
-- Дамп данных таблицы `django_site`
--

INSERT INTO `django_site` (`id`, `domain`, `name`) VALUES
(1, 'example.com', 'example.com');

-- --------------------------------------------------------

--
-- Структура таблицы `images`
--

CREATE TABLE IF NOT EXISTS `images` (
  `url_id` int(11) NOT NULL,
  `ext` varchar(8) NOT NULL,
  `has_s` int(11) NOT NULL,
  `page_id` int(11) NOT NULL,
  PRIMARY KEY (`url_id`),
  KEY `images_3fb9c94f` (`page_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Структура таблицы `pages`
--

CREATE TABLE IF NOT EXISTS `pages` (
  `url_id` int(11) NOT NULL,
  `images_total` int(11) NOT NULL,
  `images_ready` int(11) NOT NULL,
  PRIMARY KEY (`url_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Дамп данных таблицы `pages`
--

INSERT INTO `pages` (`url_id`, `images_total`, `images_ready`) VALUES
(1, 0, 0),
(2, 0, 0);

-- --------------------------------------------------------

--
-- Структура таблицы `south_migrationhistory`
--

CREATE TABLE IF NOT EXISTS `south_migrationhistory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_name` varchar(255) NOT NULL,
  `migration` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=5 ;

--
-- Дамп данных таблицы `south_migrationhistory`
--

INSERT INTO `south_migrationhistory` (`id`, `app_name`, `migration`, `applied`) VALUES
(1, 'menu', '0001_initial', '2013-09-05 23:51:12'),
(2, 'dashboard', '0001_initial', '2013-09-05 23:51:22'),
(3, 'dashboard', '0002_auto__add_field_dashboardpreferences_dashboard_id', '2013-09-05 23:51:22'),
(4, 'dashboard', '0003_auto__add_unique_dashboardpreferences_dashboard_id_user', '2013-09-05 23:51:22');

-- --------------------------------------------------------

--
-- Структура таблицы `urls`
--

CREATE TABLE IF NOT EXISTS `urls` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `urlhash` varchar(32) NOT NULL,
  `url` varchar(512) NOT NULL,
  `status` int(11) NOT NULL,
  `date` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `urlhash` (`urlhash`),
  KEY `date` (`date`),
  KEY `status` (`status`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- Дамп данных таблицы `urls`
--

INSERT INTO `urls` (`id`, `urlhash`, `url`, `status`, `date`) VALUES
(1, 'dd027870deebb7816b5784f2e6c9a65a', 'http://ru.wikipedia.org/wiki/2ch', 0, 0),
(2, '7040d932542ce4a93e866abdc4a947c5', 'http://2ch.hk/b/', 0, 0);

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `admin_tools_dashboard_preferences`
--
ALTER TABLE `admin_tools_dashboard_preferences`
  ADD CONSTRAINT `user_id_refs_id_23127ba7` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Ограничения внешнего ключа таблицы `admin_tools_menu_bookmark`
--
ALTER TABLE `admin_tools_menu_bookmark`
  ADD CONSTRAINT `user_id_refs_id_1dc7bd98` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Ограничения внешнего ключа таблицы `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `group_id_refs_id_f4b32aac` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `permission_id_refs_id_6ba0f519` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Ограничения внешнего ключа таблицы `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `content_type_id_refs_id_d043b34a` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Ограничения внешнего ключа таблицы `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `user_id_refs_id_40c41112` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `group_id_refs_id_274b862c` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Ограничения внешнего ключа таблицы `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `user_id_refs_id_4dc23c39` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `permission_id_refs_id_35d9ac25` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Ограничения внешнего ключа таблицы `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `user_id_refs_id_c0d12874` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `content_type_id_refs_id_93d2d1f8` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Ограничения внешнего ключа таблицы `images`
--
ALTER TABLE `images`
  ADD CONSTRAINT `url_id_refs_id_aaac7f93` FOREIGN KEY (`url_id`) REFERENCES `urls` (`id`),
  ADD CONSTRAINT `page_id_refs_url_id_2a542699` FOREIGN KEY (`page_id`) REFERENCES `pages` (`url_id`);

--
-- Ограничения внешнего ключа таблицы `pages`
--
ALTER TABLE `pages`
  ADD CONSTRAINT `url_id_refs_id_66e61255` FOREIGN KEY (`url_id`) REFERENCES `urls` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
