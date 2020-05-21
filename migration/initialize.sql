create database if not exists testdb;

create table testdb.members (
  id int not null auto_increment comment '会員ID',
  name varchar(255) not null comment '会員名',
  email varchar(255) not null comment '会員メールアドレス',
  PRIMARY KEY (id)
) comment ='会員一覧';

insert into testdb.members(name, email) values
('テスト太郎', 'taro_test@testmail.com'),
('テスト花子', 'hanako_test@testmail.com')