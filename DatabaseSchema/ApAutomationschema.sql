USE [master]
GO
/****** Object:  Database [apautomation]    Script Date: 12/3/2022 3:11:20 PM ******/
CREATE DATABASE [apautomation]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'apautomation', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\apautomation.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'apautomation_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.MSSQLSERVER\MSSQL\DATA\apautomation_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT
GO
ALTER DATABASE [apautomation] SET COMPATIBILITY_LEVEL = 150
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [apautomation].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [apautomation] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [apautomation] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [apautomation] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [apautomation] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [apautomation] SET ARITHABORT OFF 
GO
ALTER DATABASE [apautomation] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [apautomation] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [apautomation] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [apautomation] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [apautomation] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [apautomation] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [apautomation] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [apautomation] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [apautomation] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [apautomation] SET  DISABLE_BROKER 
GO
ALTER DATABASE [apautomation] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [apautomation] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [apautomation] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [apautomation] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [apautomation] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [apautomation] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [apautomation] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [apautomation] SET RECOVERY FULL 
GO
ALTER DATABASE [apautomation] SET  MULTI_USER 
GO
ALTER DATABASE [apautomation] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [apautomation] SET DB_CHAINING OFF 
GO
ALTER DATABASE [apautomation] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [apautomation] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [apautomation] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [apautomation] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
EXEC sys.sp_db_vardecimal_storage_format N'apautomation', N'ON'
GO
ALTER DATABASE [apautomation] SET QUERY_STORE = OFF
GO
USE [apautomation]
GO
/****** Object:  Table [dbo].[approvals]    Script Date: 12/3/2022 3:11:20 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[approvals](
	[approvalid] [varchar](256) NOT NULL,
	[status] [varchar](64) NULL,
	[approved_by] [varchar](256) NULL,
	[approved_on] [datetime] NULL,
	[billid] [varchar](256) NULL,
	[comments] [text] NULL,
 CONSTRAINT [PK_approvals] PRIMARY KEY CLUSTERED 
(
	[approvalid] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[bills]    Script Date: 12/3/2022 3:11:21 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[bills](
	[billid] [varchar](256) NOT NULL,
	[name] [varchar](126) NULL,
	[amount] [float] NULL,
	[tax] [float] NULL,
	[billdate] [date] NULL,
	[deptname] [varchar](256) NULL,
	[userid] [varchar](256) NULL,
	[filename] [varchar](126) NOT NULL,
 CONSTRAINT [PK_bills] PRIMARY KEY CLUSTERED 
(
	[billid] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[department]    Script Date: 12/3/2022 3:11:21 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[department](
	[deptid] [varchar](256) NOT NULL,
	[name] [varchar](256) NULL,
	[updatedon] [datetime] NULL,
 CONSTRAINT [PK_department] PRIMARY KEY CLUSTERED 
(
	[deptid] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[user]    Script Date: 12/3/2022 3:11:21 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[user](
	[userid] [varchar](256) NOT NULL,
	[name] [varchar](128) NOT NULL,
	[email] [varchar](128) NOT NULL,
	[mobile] [varchar](15) NULL,
	[status] [bit] NOT NULL,
	[usertype] [varchar](50) NOT NULL,
	[password] [varchar](256) NOT NULL,
 CONSTRAINT [PK_user] PRIMARY KEY CLUSTERED 
(
	[userid] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[user_dept]    Script Date: 12/3/2022 3:11:21 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[user_dept](
	[userdeptid] [varchar](256) NOT NULL,
	[userid] [varchar](256) NULL,
	[deptid] [varchar](256) NULL,
 CONSTRAINT [PK_user_dept] PRIMARY KEY CLUSTERED 
(
	[userdeptid] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[department] ADD  CONSTRAINT [DF_department_updatedon]  DEFAULT (getdate()) FOR [updatedon]
GO
ALTER TABLE [dbo].[approvals]  WITH CHECK ADD  CONSTRAINT [FK_approvals_bills] FOREIGN KEY([billid])
REFERENCES [dbo].[bills] ([billid])
GO
ALTER TABLE [dbo].[approvals] CHECK CONSTRAINT [FK_approvals_bills]
GO
ALTER TABLE [dbo].[bills]  WITH CHECK ADD  CONSTRAINT [FK_bills_user] FOREIGN KEY([userid])
REFERENCES [dbo].[user] ([userid])
GO
ALTER TABLE [dbo].[bills] CHECK CONSTRAINT [FK_bills_user]
GO
ALTER TABLE [dbo].[user_dept]  WITH CHECK ADD  CONSTRAINT [FK_user_dept_department] FOREIGN KEY([deptid])
REFERENCES [dbo].[department] ([deptid])
GO
ALTER TABLE [dbo].[user_dept] CHECK CONSTRAINT [FK_user_dept_department]
GO
ALTER TABLE [dbo].[user_dept]  WITH CHECK ADD  CONSTRAINT [FK_user_dept_user] FOREIGN KEY([userid])
REFERENCES [dbo].[user] ([userid])
GO
ALTER TABLE [dbo].[user_dept] CHECK CONSTRAINT [FK_user_dept_user]
GO
USE [master]
GO
ALTER DATABASE [apautomation] SET  READ_WRITE 
GO
